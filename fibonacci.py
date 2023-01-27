seq = int(input("Enter your sequence number: "))
num1 = 0
num2 = 1
print(f'{num1} - {num2}', end=' ')
for i in range(0,seq -2):
    ressom = num1 + num2
    num1 = num2
    num2 = ressom
    print(f'- {ressom}', end=' ')
