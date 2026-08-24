def list_orders():
    try:
        print('History orders')
        with open('coffe_orders.txt','r',encoding='utf-8') as f:
                orders = f.readlines()
                if orders:
                    for id,caffe in enumerate(orders,start=1):
                        print(f'pedido {id} --> {caffe}')
                else:
                    print('no hay pedidos')
    except FileNotFoundError:
        print('file not exist')