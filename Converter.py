num = int(input('Insert a integer number: '))
print('''Choose one of the bases for convert:
[1] Binary
[2] Octal
[3] Hexadecimal''')
opção = int(input('Your Choose: '))
if opção == 1:
    print('{} Converted to Binary is {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Converted to Octal is {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Converted to Hexadecimal is {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')
