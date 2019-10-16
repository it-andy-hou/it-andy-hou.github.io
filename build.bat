mkdocs build
del /a /f /s /q D:\site
md D:\site
xcopy site\*.* D:\site /S /F /R /Y /E
cd D:\Documents\GitHub\it-andy-hou.github.io\
rd /s /Q site
start /min cmd /c D:\test.bat
git checkout master
pause