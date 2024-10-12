import random


class Character:
    def __init__(self, money):
        self.money = money
        self.satisfaction = 50
        self.hunger = 50
        self.sleepiness = 50




    def display_status(self, days):
        print(f"Дні: {days}")
        print(f"Гроші: {self.money} гривень")
        print(f"Задоволеність: {self.satisfaction}")
        print(f"Голод: {self.hunger}")
        print(f"Втома: {self.sleepiness}")



    def go_to_cafe(self):
        if self.money >= 1000:
            self.money -= 1000
            satisfaction_change = random.randint(5, 15)
            hunger_change = random.randint(-25, -15)
            self.satisfaction += satisfaction_change
            self.hunger += hunger_change
            self.sleepiness += 5
            print(f"Ви сходили в кафе. Задоволеність змінилась на {satisfaction_change}, голод на {hunger_change}.")
        else:
            print("Недостатньо коштів!")




    def go_shopping(self):
        if self.money >= 3000:
            self.money -= 3000
            satisfaction_change = random.randint(15, 25)
            hunger_change = random.randint(5, 15)
            self.satisfaction += satisfaction_change
            self.hunger += hunger_change
            self.sleepiness += 10
            print(f"Ви сходили на шоппінг. Задоволеність змінилась на {satisfaction_change}, голод на {hunger_change}.")
        else:
            print("Недостатньо коштів!")




    def go_on_date(self):
        if self.money >= 2000:
            self.money -= 2000
            satisfaction_change = random.randint(20, 30)
            hunger_change = random.randint(0, 10)
            self.satisfaction += satisfaction_change
            self.hunger += hunger_change
            self.sleepiness += 15
            print(f"Ви сходили на побачення. Задоволеність змінилась на {satisfaction_change}, голод на {hunger_change}.")
        else:
            print("Недостатньо коштів!")





    def do_nothing(self):
        self.satisfaction += 5
        self.hunger += 5
        self.sleepiness += 5
        print("Ви вирішили нічого не робити.")



    def walk(self):
        self.satisfaction += 15
        self.sleepiness += 10
        print("Ви прогулялись.")



    def sleep(self):
        self.satisfaction += 10
        self.sleepiness -= random.randint(15, 25)
        self.hunger += 5
        print("Ви поспали.")


    def eat(self):
        self.satisfaction += 5
        self.hunger -= random.randint(15, 25)
        self.sleepiness += 5
        print("Ви поїли.")




    def work(self):
        self.money += 1500
        self.satisfaction -= 10
        self.hunger += 5
        self.sleepiness += 10
        print("Ви попрацювали.")





    def clamp_status(self):
        self.satisfaction = max(0, min(100, self.satisfaction))
        self.hunger = max(0, min(100, self.hunger))
        self.sleepiness = max(0, min(100, self.sleepiness))





def main():
    character = Character(money=10000)
    days = 0




    while True:
        character.display_status(days)
        print("Що ви хочете зробити?")
        print("1. Сходити в кафе (-1000 гривень, 'від +5 до +15' задоволеності, 'від -15 до -25' голоду)")
        print("2. Сходити на шопінг (-3000 гривень, 'від +15 до +25' задоволеності, 'від +5 до +15' голоду)")
        print("3. Сходити на побачення (-2000 гривень, 'від +20 до +30' задоволеності, 'від +0 до +10' голодуу)")
        print("4. Нікуди не йти (зберегти кошти, +5 задоволеності, +5 голоду, +5 втоми)")
        print("5. Прогулятися (+15 задоволеності, +10 втоми)")
        print("6. Лягти спати (+10 задоволеності, 'від -15 до -25' втоми, +5 голоду)")
        print("7. Поїсти (+5 задоволеності, 'від -15 до -25' голоду, +5 втоми)")
        print("8. Попрацювати (+1500 гривень, -10 задоволеності, +5 голоду, +10 втоми)")




        choice = input("Виберіть дію: (1-8): ")



        if choice == '1':
            character.go_to_cafe()
        elif choice == '2':
            character.go_shopping()
        elif choice == '3':
            character.go_on_date()
        elif choice == '4':
            character.do_nothing()
        elif choice == '5':
            character.walk()
        elif choice == '6':
            character.sleep()
        elif choice == '7':
            character.eat()
        elif choice == '8':
            character.work()
        else:
            print("Некоректне введення. Спробуйте ще раз.")



        character.clamp_status()
        days += 1





        if character.satisfaction <= 0:
            print("Ваш персонаж втратив задоволення від життя... Гра закінчена.")
            break
        elif character.hunger >= 100:
            print("Ваш персонаж надто зголоднів... Гра закінчена.")
            break
        elif character.sleepiness >= 100:
            print("Ваш персонаж надто втомився... Гра закінчена.")
            break
        elif character.money <= 0:
            print("У вас більше немає грошей... Гра закінчена.")
            break




if __name__ == "__main__":
    main()
