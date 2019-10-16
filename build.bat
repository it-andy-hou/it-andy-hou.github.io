mkdocs build
del /a /f /s /q D:\site
xcopy site\*.* D:\site
cd %cd%
rd /s /Q site
rem git checkout master
pause