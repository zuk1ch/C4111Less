def q_generator(base, max_n):
    n = 0
    while n <= max_n:
        yield base ** n
        n += 1


user_input = float(input("Введіть число: "))
max_n = int(input("Введіть максимальний ступінь: "))


generator = q_generator(user_input, max_n)


for power in generator:
    print(power)
