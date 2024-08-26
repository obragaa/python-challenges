import re
import unicodedata

def eh_palindromo(s):
    # Normaliza a string para remover acentuação
    s = unicodedata.normalize('NFD', s)
    s = ''.join([c for c in s if unicodedata.category(c) != 'Mn'])
    
    # Converter a string para minúsculas
    s = s.lower()
    
    # Remover todos os caracteres que não são letras
    s = re.sub(r'[^a-z]', '', s)
    
    # Verificar se a string é igual a ela mesma invertida
    return s == s[::-1]

# Testando a função
print(eh_palindromo("Olá mundo!"))  # Saída: False
print(eh_palindromo("Socorram-me, subi no ônibus em Marrocos!"))  # Saída: True
