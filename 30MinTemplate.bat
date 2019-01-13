@echo off

xcopy /s _template %1

echo - [%1](/%1) : >> README.md