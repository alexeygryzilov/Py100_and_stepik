year = 2012

if year % 400 == 0 or year % 4 ==0 and year % 100 != 0:
    print(year, "является високосным годом.")
else:
    print(year, "не является високосным годом.")
