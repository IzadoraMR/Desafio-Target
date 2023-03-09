def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

numero = int(input("Informe um número: "))

pertence = False
i = 0
while fibonacci(i) <= numero:
    if fibonacci(i) == numero:
        pertence = True
        break
    i += 1

if pertence:
    print(numero, "pertence à sequência de Fibonacci!")
else:
    print(numero, "não pertence à sequência de Fibonacci.")