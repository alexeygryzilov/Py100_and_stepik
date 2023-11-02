INPUT_FILE = "input.txt"

OUTPUT_FILE = "output.txt"


def task():
    with open('input.txt','w') as f:
        for i in range(1, 11):
            f.write('*' * i + '\n')


if __name__ == '__main__':
    # Необходимо для проверки
    task()
    with open('input.txt') as file:
        for line in file:
            print(line, end="")
