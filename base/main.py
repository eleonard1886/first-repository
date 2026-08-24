from base.menu_cafe import menu as m
from base.order import coffe_order as ord
from base.history import list_orders as lo


def main():
    
    while True:
        m()
        option = int(input("\nSelecciona una opcion: "))

        if option == 1: 
            ord()
        elif option == 2:
            lo()
        elif option == 3:
            print('THANK YOU')
            break

if __name__ == "__main__":
    main()