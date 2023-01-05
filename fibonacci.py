num = int(input("Enter your number: "))
numOuro = input("Do you want to find out the golden number of your number? Y(yes) ou N(no)")
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
    print('Your golden number is {}' .format(div))
