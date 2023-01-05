num = int(input("Digite seu número: "))
numOuro = input("Você quer descobrir o número de ouro de seu número? Y(sim) ou N(não)")
if num == 0:
    print('0')
if num == 1 or num == 2:
    print('1')
else:
    s1 = num - 1
    s2 = num - 2
    som = s1 + s2
    print(som)
if numOuro == 'N':
    ('Byebye 😊')
    exit(0)
if numOuro == 'Y':
    sO = num - 1
    div = num / sO
    print('Seu número de ouro é {}' .format(div))