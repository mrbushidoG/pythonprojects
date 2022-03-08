def create_class(class_name):
    return type(class_name,(object,),{
        "__init__": print("Class created")
    })

user_input = input("Your Class Name")

created_instance = create_class(user_input)

print(created_instance.__name__)
