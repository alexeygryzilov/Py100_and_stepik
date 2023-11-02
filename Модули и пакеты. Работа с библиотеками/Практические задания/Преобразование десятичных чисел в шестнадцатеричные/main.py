# TODO Напишите функцию decimal_to_hex
def decimal_to_hex():
    dict_ = {number: hex(number) for number in range(0,16)}
    return dict_

if __name__ == '__main__':
    print(decimal_to_hex())

