def create_file():
    try:
        with open('archivo.txt','w',encoding=('utf-8')) as f:
            f.write('me eh creado por python file ')
    except FileNotFoundError:
        print('Not allow to create a file')
    finally:
        print('script finished')


try:
    with open('archivo.txt','r',encoding=('utf-8')) as f:
        print(f.readline())
except FileNotFoundError:
    print('File not found in this directory')
    create_file()
finally:
    print('I am finished here')