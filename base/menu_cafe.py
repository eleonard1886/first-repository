def menu():
    print('Welcome you your brew coffe machine pick a option\n')
    menu = {'1':'Pedir un cafe ','2':'ver historial de pedidos','3':'Salir'}
    
    for id, option in menu.items():
        print(f'{id} --> {option}')
