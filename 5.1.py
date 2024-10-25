import string
import keyword

def is_valid_variable(name):
    if name in keyword.kwlist:
        return False

    if name[0].isdigit():
        return False

    if any(char in string.punctuation.replace("_", "") for char in name):
        return False

    if any(char.isupper() or char.isspace() for char in name):
        return False

    if name.count("_") > 1:
        return False

    return True

print(is_valid_variable("_"))
print(is_valid_variable("__"))
print(is_valid_variable("___"))
print(is_valid_variable("x"))
print(is_valid_variable("get_value"))
print(is_valid_variable("get value"))
print(is_valid_variable("get!value"))
print(is_valid_variable("some_super_puper_value"))
print(is_valid_variable("Get_value"))
print(is_valid_variable("get_Value"))
print(is_valid_variable("getValue"))
print(is_valid_variable("3m"))
print(is_valid_variable("m3"))
print(is_valid_variable("assert"))
print(is_valid_variable("assert_exception"))