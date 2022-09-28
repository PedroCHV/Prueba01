def run():
    my_list =[1, "Hello", True, 4.5 ]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"}


super_list = [ 
    {"firstname": "Facundo", "lastname": "Garcia"},
    {"firstname": "Maria", "lastname": "Henriquez"},
    {"firstname": "Marisol", "lastname": "Pimienta"},
    {"firstname": "Diana", "lastname": "Vasquez"},
    {"firstname": "Carlos", "lastname": "Montoya"}
]

super_dict = {
    "Natural_nums" : [1, 2, 5, 3],
    "Integer_nums" : [2, -2, 0, 3],
    "Floating_nums" :[2.23, 5.65, 2.34, 7.87],
}

for key, value in super_dict.items():
    print(key, "-", value)

for key, value in super_list.items():
    print(key, "-", value)




if __name__=='__main__':
    run()
