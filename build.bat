mkdocs build
del /a /f /s /q D:\site
xcopy site D:\site
cd %cd%
del /a /f /s /q site
rem git checkout master
pause