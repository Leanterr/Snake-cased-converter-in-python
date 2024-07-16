 
def snake_basic_converter(camel_or_pascal_cased):
    final = ''
    for char in camel_or_pascal_cased:
        if char.isupper():
            char = '_' + char.lower()
            final += char 
        else:
            char = char
            final += char
    productfinal = final.strip('_')
    print(productfinal)
    return final 
snake_basic_converter('IAmAPascalCasedString')


def snake_cased_converter(camel_or_pascal_cased_string):
    snake_list = []
    for char in camel_or_pascal_cased_string:
        if char.isupper():
            converted_char = '_' + char.lower()
            snake_list.append(converted_char)
        else:
            snake_list.append(char)
    final_string = ''.join(snake_list).strip('_')
    
    print(final_string)
    return final_string 

snake_cased_converter('IAmAPascalCasedString')

def snake_cased_converted_list_comp(camel_or_pascal_cased_string):
    snake_list = ['_' + char.lower() if char.isupper() else char for char in camel_or_pascal_cased_string]
    final_string = ''.join(snake_list).strip('_')
    print(final_string)
    return final_string

snake_cased_converted_list_comp('IAmAPascalCasedString')