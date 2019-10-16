mkdocs build
del /a /f /s /q D:\site
md D:\site
xcopy site\*.* D:\site /S /F /R /Y /E
cd %~dp0
rd /s /Q site
git checkout master
xcopy D:\site\*.* %~dp0  /S /F /R /Y /E
pause