info_users = {
    'leo':{
        'middle_name':'Manuel',
        'last_name':'Velasquez',
        'edad':'39',
        'pais':'Colombia',
        'ciudad':'Bogota'
    },
    'andrea':{
        'middle_name':'Francedy',
        'last_name':'Garcia',
        'edad':'38',
        'pais':'Colombia',
        'ciudad':'Bogota'
    },
    'sultan':{
        'middle_name':'Aurelio',
        'last_name':'Velasquez Garcia',
        'edad':'4',
        'pais':'Colombia',
        'ciudad':'Bogota'
    }
}


for key ,user in info_users.items():
    for info in user :
#       print(user[info])
        continue


my_list = list(range(1,10))

my_iter = iter(my_list)

#print(next(my_iter))



# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# for value in my_generator():
#     print(value)



def get_numbers_yield(n):
    for i in range(n):
        yield i  # Pauses here and hands over 'i'

# Calling the function returns a generator object, not a list
generator = get_numbers_yield(3)

print(next(generator))  # Output: 0 (function pauses at yield)
print(next(generator))  # Output: 1 (function resumes, then pauses again)
# Output: 2 (function resumes, then finishes)