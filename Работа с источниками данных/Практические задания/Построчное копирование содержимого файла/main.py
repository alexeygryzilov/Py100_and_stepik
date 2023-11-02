INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open('input.txt') as file_1 :
        line_to_write = ''
        for line in file_1:
            upper_line = line.upper()
            line_to_write += upper_line

        file_2 = open('output.txt', 'w')
        file_2.write(line_to_write)
        file_2.close()




if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
