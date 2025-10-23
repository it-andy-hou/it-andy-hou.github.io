import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import threading
import os
import re
import base64
import cv2
import zxingcpp
import migration_pb2
import tempfile

class QRCodeScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("2FA 二维码识别工具")
        self.root.geometry("500x500")
        
        # Configure style
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 10))
        style.configure("TLabel", font=('Helvetica', 12))
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="2FA 二维码识别工具",
            font=('Helvetica', 16, 'bold')
        )
        title_label.pack(pady=20)
        
        # Select button
        self.select_button = ttk.Button(
            main_frame,
            text="选择二维码图片",
            command=self.select_image
        )
        self.select_button.pack(pady=10)
        
        # Result text area
        self.result_text = tk.Text(
            main_frame,
            height=10,
            width=50,
            wrap=tk.WORD,
            font=('Helvetica', 10)
        )
        self.result_text.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.pack(pady=5)

        # Menu bar with About
        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="关于", command=self.show_about)
        menubar.add_cascade(label="帮助", menu=helpmenu)
        self.root.config(menu=menubar)

    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.process_image(file_path)

    def process_image(self, image_path):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Processing image... Please wait...")
        self.status_label.config(text="Processing...")
        
        # Run processing in a separate thread
        thread = threading.Thread(
            target=self._process_image_thread,
            args=(image_path,)
        )
        thread.daemon = True
        thread.start()

    def _process_image_thread(self, image_path):
        try:
            # Read the image using OpenCV
            image = cv2.imread(image_path)
            if image is None:
                self._update_ui("Error: Could not read the image file.", error=True)
                return
                
            # Read and decode QR code
            result = zxingcpp.read_barcode(image)
            
            if not result:
                self._update_ui("Error: No QR code found in the image.", error=True)
                return
            
            qr_data = result.text
            
            # 普通 otpauth:// 逻辑
            if qr_data.startswith('otpauth://'):
                secret_match = re.search(r'secret=([A-Z2-7]+)', qr_data)
                if not secret_match:
                    self._update_ui("Error: Could not find secret key in QR code.", error=True)
                    return
                secret = secret_match.group(1)
                try:
                    base64.b32decode(secret)
                    self._update_ui(f"Successfully extracted 2FA secret:\n{secret}")
                except Exception:
                    self._update_ui("Error: Invalid secret key format.", error=True)
                return
            # otpauth-migration:// 逻辑
            elif qr_data.startswith('otpauth-migration://'):
                import urllib.parse
                parsed = urllib.parse.urlparse(qr_data)
                params = urllib.parse.parse_qs(parsed.query)
                data_b64 = params.get('data', [None])[0]
                if not data_b64:
                    self._update_ui("Error: No data field in migration QR code.", error=True)
                    return
                try:
                    data_bytes = base64.urlsafe_b64decode(data_b64 + '==')
                    payload = migration_pb2.MigrationPayload()
                    payload.ParseFromString(data_bytes)
                    if not payload.otp_parameters:
                        self._update_ui("Error: No OTP accounts found in migration QR code.", error=True)
                        return
                    result_lines = ["检测到 Google Authenticator 迁移二维码，解析结果如下：\n"]
                    for idx, otp in enumerate(payload.otp_parameters, 1):
                        secret = base64.b32encode(otp.secret).decode('utf-8')
                        name = otp.name
                        issuer = otp.issuer
                        result_lines.append(f"账号{idx}:\n  账号名: {name}\n  服务商: {issuer}\n  密钥: {secret}\n")
                    self._update_ui("\n".join(result_lines), error=False)
                except Exception as e:
                    self._update_ui(f"Error: Failed to parse migration QR code: {str(e)}", error=True)
                return
            else:
                self._update_ui(
                    "Error: Invalid QR code format. Not a Google Authenticator QR code.",
                    error=True
                )
                return
        except Exception as e:
            self._update_ui(f"Error: An error occurred: {str(e)}", error=True)

    def _update_ui(self, message, error=False):
        def update():
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, message)
            self.status_label.config(
                text="Error" if error else "完成",
                foreground="red" if error else "black"
            )
        self.root.after(0, update)

    def show_about(self):
        about_text = (
            "2FA 二维码识别工具\n\n"
            "【使用说明】\n"
            "本程序用于识别和解析 Google Authenticator 二维码，包括普通 otpauth:// 以及迁移 otpauth-migration:// 类型。\n"
            "选择二维码图片后，程序会自动解析出 2FA 密钥或迁移信息。\n\n"
            "【声明与授权要求】\n"
            "本软件仅供学习、交流与个人正当用途。\n"
            "作者不对因使用本软件造成的任何数据丢失、隐私泄露或其他后果负责。\n"
            "严禁将本软件用于任何非法用途，否则后果自负。\n\n"
            "【作者】\n"
            "🍠小红书：奇技淫巧的安迪\n"
            "🌐网站：hi-andy.com\n"
        )
        messagebox.showinfo("关于", about_text)

def main():
    root = tk.Tk()
    # 用 base64 内嵌方式设置窗口图标
    ico_data = b'''XXXX'''
    with tempfile.NamedTemporaryFile(delete=False, suffix='.ico') as tmp_ico:
        tmp_ico.write(base64.b64decode(ico_data))
        tmp_ico_path = tmp_ico.name
    root.iconbitmap(tmp_ico_path)
    app = QRCodeScanner(root)
    root.mainloop()

if __name__ == '__main__':
    main()
