mkdocs build
del /a /f /s /q D:\site
md D:\site
xcopy site\*.* D:\site /s /h /d /y
cd %~dp0
rd /s /Q site
git checkout master
xcopy D:\site\*.* %~dp0
pause