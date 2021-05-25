vendoGanado = input('Hola, soy bot Granje, deseas que te venda ganado? ')

if vendoGanado == 'si':
    cantidad = int(input('Cuantas vacas quieres? '))
    precio = cantidad * 1000
    print(f'Ok, voy a venderte {cantidad}, cada vaca es a $1000 ')
    confirm = input(f'Confirmas la compra por un total de ${precio}? ')
    if confirm == 'si':
        print('Pago efectuado, gracias por su compra! ')
    else:
        print('Ok, espero vuelva cuando tenga dinero ')
elif vendoGanado == 'no':
    print('Minions, me funarron :( ')


