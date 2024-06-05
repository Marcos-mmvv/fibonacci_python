# Calcular a sequência Fibonacci
def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

 # Programa principal   
n = int(input('Informe o número de sequências a ser calculada: '))
print(f'A sequência é {calcular_fibonacci(n)}.')
