def is_lucky_number(num: int) -> bool:
     # TODO проверить что число шестизначное и положительное
    if not (num > 0 and len(str(num)) == 6):
        return 'ValueError'
    else:
        str_ = str(num)
        number = [int(element) for element in str_]
        return sum(number[:3]) == sum(number[3:])
      # TODO проверить счастливое число или нет


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
