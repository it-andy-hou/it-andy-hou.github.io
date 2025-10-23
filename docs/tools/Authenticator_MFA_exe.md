# Google_Authenticator_MFA Windows 计算工具自动粘贴板

<img src="/imgs/tools/2021-12-30_142233.png">

## 下载

工具打包下载 [Google_Authenticator_MFA Windows 计算工具自动粘贴板工具V1.0](../files/Authenticator_MFA Windows.zip)

GitHub 项目地址：[https://github.com/robbiev/two-factor-auth](https://github.com/robbiev/two-factor-auth)


## go 代码
```GO
package main

import (
	"crypto/hmac"
	"crypto/sha1"
	"encoding/base32"
	"fmt"
	"os"
	"strings"
	"time"
	"atotto/clipboard"
)

func toBytes(value int64) []byte {
	var result []byte
	mask := int64(0xFF)
	shifts := [8]uint16{56, 48, 40, 32, 24, 16, 8, 0}
	for _, shift := range shifts {
		result = append(result, byte((value>>shift)&mask))
	}
	return result
}

func toUint32(bytes []byte) uint32 {
	return (uint32(bytes[0]) << 24) + (uint32(bytes[1]) << 16) +
		(uint32(bytes[2]) << 8) + uint32(bytes[3])
}

func oneTimePassword(key []byte, value []byte) uint32 {
	// sign the value using HMAC-SHA1
	hmacSha1 := hmac.New(sha1.New, key)
	hmacSha1.Write(value)
	hash := hmacSha1.Sum(nil)

	// We're going to use a subset of the generated hash.
	// Using the last nibble (half-byte) to choose the index to start from.
	// This number is always appropriate as it's maximum decimal 15, the hash will
	// have the maximum index 19 (20 bytes of SHA1) and we need 4 bytes.
	offset := hash[len(hash)-1] & 0x0F

	// get a 32-bit (4-byte) chunk from the hash starting at offset
	hashParts := hash[offset : offset+4]

	// ignore the most significant bit as per RFC 4226
	hashParts[0] = hashParts[0] & 0x7F

	number := toUint32(hashParts)

	// size to 6 digits
	// one million is the first number with 7 digits so the remainder
	// of the division will always return < 7 digits
	pwd := number % 1000000

	return pwd
}

// all []byte in this program are treated as Big Endian
func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "must specify key to use")
		os.Exit(1)
	}

	input := os.Args[1]

	// decode the key from the first argument
	inputNoSpaces := strings.Replace(input, " ", "", -1)
	inputNoSpacesUpper := strings.ToUpper(inputNoSpaces)
	key, err := base32.StdEncoding.WithPadding(base32.NoPadding).DecodeString(inputNoSpacesUpper)
	if err != nil {
		fmt.Fprintln(os.Stderr, err.Error())
		os.Exit(1)
	}

	// generate a one-time password using the time at 30-second intervals
	epochSeconds := time.Now().Unix()
	pwd := oneTimePassword(key, toBytes(epochSeconds/30))

	secondsRemaining := 30 - (epochSeconds % 30)
	fmt.Printf("%06d (%d 秒有效期)\n", pwd, secondsRemaining)
	pwd_key := fmt.Sprintf("%06d", pwd)
	// 复制内容到剪切板
    clipboard.WriteAll(pwd_key)
}
```

## 调用方法

已经将代码打包成 **key.exe**文件，调用的时候直接在**key.exe** 后面传参 **secret值**，传入对应的 secret值
> 如何获取secret值 参考历史文章 [https://hi-andy.com/note/2021/2021-12-29-cloud_tencent/](https://hi-andy.com/note/2021/2021-12-29-cloud_tencent/)

<img src="/imgs/tools/2021-12-30_150640.png">
<img src="/imgs/tools/2021-12-30_142233.png">

<hr>

<script src="https://utteranc.es/client.js"
        repo="it-andy-hou/it-andy-hou.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
