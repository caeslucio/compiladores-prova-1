"""
A figura q2.svg mostra uma máquina de estados (ou autômato finito
determinístico, DFA) que reconhece a linguagem formadas por a's e b's. Uma
string é aceita se começando no estado "start" e fazendo apenas as transições
definidas na figura, a string termina no estado "accept".

Dê alguns exemplos de strings que são aceitas e outras que são recusadas nessa
linguagem preenchendo as variáveis abaixo.

Depois crie uma expressão regular que reconheça a mesma linguagem.
"""

# Menor string possível nessa linguagem (0.5pt)
menor = "baa"

# Uma string válida com exatamente 5 caracteres  (0.5pt)
string_5 = "bbbaa"

# Menor string que o número de a's é igual ao número de b's (0.5pt)
menor_ab = "baba"

# 3 exemplos de strings válidas diferentes (exceto as anteriores) (1.0pt)
accept_3 = ["bbbbbaa", "bbbbbbbaa", "bbbbbbbbbaa"]

# Para cada exemplo acima, gere uma string inválida somente rearranjando os
# caracteres da string válida na mesma posição que em accept_3  (1.0pt)
reject_3 = ["abbbbba", "abbbbbbba", "abbbbbbbbba"]

# Regex que descreve a linguagem (1.5pt)
# Dica tente simplificar o grafo tirando transições desnecessárias
regex = r"b((a|b)*ab*)a"
