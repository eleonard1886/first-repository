def coffe_order():

    coffes = {'1':'Moca','2':'Late','3':'American','4':'Expresso'}
    print('\n Pick your option')
    for id,coffe in coffes.items():
        print(f'{id} : {coffe}')

    option = input('Option:')

    if option in coffes:
        kafe = coffes[option]
        print(f'Enjoy your : {kafe}')
        coffe_history(kafe)
    else:
        print('Please choose at valid option')
## ! fin coffe order function

def coffe_history(coffe):
    try:
        with open('coffe_orders.txt','a',encoding=('utf-8')) as f:
            f.write(f'client drink {coffe} \n')
    except Exception as e:
        print('Error: {error}'.format(error=e))
## ! fin coffe_history