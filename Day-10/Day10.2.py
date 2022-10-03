# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return formated_f_name+" "+formated_l_name
# print(format_name("SriRath","Reddy"))
    
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return formated_f_name+" "+formated_l_name
# print(format_name(input(),input()))

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return formated_f_name+" "+formated_l_name
# print(format_name(input("what is you first name? "),input("what is you last name? ")))

def format_name(f_name, l_name):
    if f_name== "" or l_name=="":
        return "Result: You have provide any input!"
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return (f"Result: {formated_f_name} {formated_l_name}")
print(format_name(input("what is you first name? "),input("what is you last name? ")))