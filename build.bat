mkdocs build
del /a /f /s /q D:\site
md D:\site
xcopy site\*.* D:\site /S /F /R /Y /E
xcopy CNAME D:\site /S /F /R /Y /E
xcopy README.md D:\site /S /F /R /Y /E
cd D:\github\it-andy-hou.github.io\
rd /s /Q site
echo ping -n 5 127.0.0.1 ^> nul > D:\test.bat
echo xcopy D:\site\*.* D:\github\it-andy-hou.github.io\  /S /F /R /Y /E >> D:\test.bat
start /min cmd /c D:\test.bat
git checkout master
pause