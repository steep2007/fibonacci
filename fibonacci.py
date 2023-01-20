seq = int(input("Enter your sequence number: "))
numOuro = input("Do you want to see the golden number of the last digit shown in your sequence? Y(yes) or N(no)")
num1 = 0
num2 = 1
print(f'{num1} - {num2}', end=' ')
for i in range(0,seq -2):
    ressom = num1 + num2
    num1 = num2
    num2 = ressom
    print(f'- {ressom}', end=' ')

if numOuro == 'N':
    ('Byebye 😊')
    exit(0)
if numOuro == 'Y':
    sO = ressom - 1
    div = ressom / sO
    print(f'Your golden number is {div}')
