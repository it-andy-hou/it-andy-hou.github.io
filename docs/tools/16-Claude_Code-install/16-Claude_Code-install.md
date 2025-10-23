在Windows 上安装Claude Code 需要通过WSL (Windows Subsystem for Linux) 来实现。首先，你需要安装WSL 并启用虚拟化功能。然后，在WSL 环境中安装Node.js 和npm，接着安装Claude Code。最后，你可以在VS Code 等IDE 中配置WSL 插件，并使用Claude Code。?
详细步骤:
1. 启用WSL 和虚拟化:
打开PowerShell 或Windows 终端(管理员模式)。?
输入 wsl --install 命令，系统会自动启用WSL 相关功能并安装Ubuntu。?
重启电脑以完成安装。?
在BIOS/UEFI 中启用虚拟化功能。?
首次启动Ubuntu 后，创建Linux 用户账户和密码。?
2. 安装Node.js 和npm:
在WSL 中，使用以下命令更新系统：sudo apt update && sudo apt upgrade.?
安装Node.js 和npm: curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt install -y nodejs.?
验证安装版本：node -v 和 npm -v。?
3. 安装Claude Code:
在WSL 中，使用npm 安装Claude Code: npm install -g @anthropic-ai/claude-code.?
验证安装: claude -v.?
4. 配置IDE (以VS Code 为例):
安装VS Code WSL 插件。?
在VS Code 中打开你的项目目录。?
打开集成终端。?
运行 claude 命令，扩展将自动安装。?
注意事项:
如果遇到问题，可以尝试在搜索引擎中搜索具体错误信息，或者参考Claude Code 官方文档。?
如果你的IDE 无法检测到Claude Code，可以尝试手动安装VSIX 插件。?
确保你的Windows 系统版本是Windows 10/11 (21H2 以上版本)，并且是专业版、工作站版或企业版。?
如果需要，可能需要配置代理，以便Claude Code 能够访问网络。?
如果你使用Cursor，可以按照 此教程 的方法配置WSL 和Cursor。?
通过以上步骤，你就可以在Windows 上成功安装和使用Claude Code 了。?