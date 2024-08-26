def fatores_primos(n):
    fatores = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return list(set(fatores))

# Testando a função com o número 630
print(fatores_primos(630))  # Saída: [2, 3, 5, 7]

# Testando a função com um número primo como 13
print(fatores_primos(13))  # Saída: [13]
