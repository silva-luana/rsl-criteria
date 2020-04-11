@ECHO OFF
ECHO -----------------------------------------------------------
ECHO Revisao Sistematica de Literatura - Pesquisa em CI / PPGICN
ECHO -----------------------------------------------------------
ECHO Este programa foi desenvolvido por Luana da Silva
ECHO Programa de Pos-Graduacao em Ciencia da Informacao - 2019/1
ECHO -----------------------------------------------------------

PAUSE

ECHO Verificando as dependencias...
ECHO -----------------------------------------------------------
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37\python.exe -m pip install -r requirements.txt
ECHO -----------------------------------------------------------
ECHO Dependencias satisfeitas..
ECHO -----------------------------------------------------------
ECHO Comecando o programa... (CTRL+C para terminar)
ECHO -----------------------------------------------------------
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37\python.exe C:\Users\%USERNAME%\Desktop\rsl_main\main.py

PAUSE