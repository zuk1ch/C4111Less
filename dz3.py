def get_input():
    user_input = input("Введіть число: ")
    try:
        num = float(user_input)
        rounded_num = round(num)
        print(f"Ви ввели число: {num}, округлене до: {rounded_num}")
    except ValueError:
        print("Помилка, введене значення не є числом!")

get_input()
