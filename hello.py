#!/usr/bin/env python3
# Especificando o interpretador na linha de comando
"""
Hello World Multi Liguas.

Dependendo da ligua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada exemplo:

    export LANG=pt_BR

Execução:

    pythons3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Erick MOura"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG","en_US")[:5]

msg = "Hello, World!" 

if current_language == "pt_BR":
   msg = "Olá, Mundo!"
elif current_language == "it_IT":
   msg = "Ciao, Mondo"

print(msg)

# Dar  permissão de execução ao script na linha de comando do terminal.
# "chmod +x hello.py"

# ./hello.py = python3 hello.py
# ou executando comando  "mv hello.py hello" ou "mv hello.py hello.e"
# ./hello = python3 hello.py
