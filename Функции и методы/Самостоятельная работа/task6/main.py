ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    return set(str_) == {'0','1'}


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string("  01110  "))
