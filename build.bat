mkdocs build
del /a /f /s /q D:\site
md D:\site
xcopy site\*.* D:\site /s /h /d /y
cd %cd%
rd /s /Q site
git checkout master
pause