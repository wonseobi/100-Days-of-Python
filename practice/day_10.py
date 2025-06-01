def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return "{formated_f_name} {formated_l_name}"

print(format_name("won", "lee"))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

# the output of function 1 becomes the input of function 2
output = function_2(function_1("hello Python!"))
print(output)
