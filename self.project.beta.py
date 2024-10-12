
class Character:
    def __init__(self, money):
        self.money = money
        self.satisfaction = 50
        self.hunger = 50
        self.sleepiness = 50





    def display_status(self):
        print(f"Гроші: {self.money} гривень")
        print(f"Задоволеність: {self.satisfaction}")
        print(f"Голод: {self.hunger}")
        print(f"Втома: {self.sleepiness}")




    def go_to_cafe(self):
        if self.money >= 1000:
            self.money -= 1000
            self.satisfaction += 10
            self.hunger -= 20
            self.sleepiness += 5
            print("Ви сходили в кафе.")
        else:
            print("Недостатньо коштів!")




    def go_shopping(self):
        if self.money >= 3000:
            self.money -= 3000
            self.satisfaction += 20
            self.hunger += 10
            self.sleepiness += 10
            print("Ви сходили на шоппінг.")
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
        self.sleepiness -= 20
        self.hunger += 5
        print("Ви поспали.")




    def eat(self):
        self.satisfaction += 5
        self.hunger -= 20
        self.sleepiness += 5
        print("Ви поїли.")




    def clamp_status(self):
        self.satisfaction = max(0, min(100, self.satisfaction))
        self.hunger = max(0, min(100, self.hunger))
        self.sleepiness = max(0, min(100, self.sleepiness))




def main():
    character = Character(money=10000)



    while True:
        character.display_status()
        print("Що ви хочете зробити?")
        print("1. Сходити у кафе (-1000 гривень)")
        print("2. Сходити на шопінг (-3000 гривень)")
        print("3. Нікуди не йти (зберегти гроші)")
        print("4. Прогулятися (+задоволеність, +втома)")
        print("5. Легти поспати (+задоволеність, -втома)")
        print("6. Поїсти (+задоволеність, -голод)")

        choice = input("Виберіть дію (1-6): ")

        if choice == '1':
            character.go_to_cafe()
        elif choice == '2':
            character.go_shopping()
        elif choice == '3':
            character.do_nothing()
        elif choice == '4':
            character.walk()
        elif choice == '5':
            character.sleep()
        elif choice == '6':
            character.eat()
        else:
            print("Некоректне введення. Спробуйте ще раз.")




        character.clamp_status()




        if character.satisfaction <= 0:
            print("Ваш персонаж впав у депресію... Гра закінчена.")
            break
        elif character.hunger >= 100:
            print("Ваш персонаж надто зголоднів... Гра закінчена.")
            break
        elif character.sleepiness >= 100:
            print("Ваш персонаж надто втомився... Гра закінченаа.")
            break




if __name__ == "__main__":
    main()
