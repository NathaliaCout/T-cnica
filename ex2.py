def fibo(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

num = int(input("Digite um número: "))

if fibo(num):
    print(f" O nº {num} pertence à sequência de Fibonacci. ")
else:
    print(f" O nº {num} não pertence à sequência de Fibonacci.")
