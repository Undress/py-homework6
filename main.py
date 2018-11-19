def polish_notation(note):
    values = note.split()

    try:
        a = int(values[1])
        b = int(values[2])
    except ValueError:
        print("Вы ввели неверные значения")
    else:
        assert (a > 0 and b > 0), 'значения меньше 0'

        if values[0] == "+":
            return a + b
        elif values[0] == "-":
            return a - b
        elif values[0] == "*":
            return a * b
        elif values[0] == "/":
            return a / b
        else:
            return("Вы ввели неверный оператор")




def main():
    note = input("Введите данные: ")

    try:
        polish_notation(note)
    except AssertionError:
        print('Вы ввели отрицательное число, введите положительное')
    else:
        print(polish_notation(note))


if __name__ == '__main__':
    main()