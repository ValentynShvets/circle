from random import randint

number = randint(1,10)
user_number = 0
trys = 0
while user_number != number and trys < 4:
        print("Введіть число", end=" ")
        user_number = int(input())

        trys +=1

        if user_number < number:
            print("Ви не вгадали число")
            print(f"Загадане число більше!!! залишилось {4-trys} спроби")
        elif user_number > number:
            print("Ви не вгадали число")
            print(f"Загадане число менше!!! залишилось {4-trys} спроби")

        else:
            print("Вітаємо ви вгадали")

        if trys == 4:
            print(f"Ви не вгадали! Загадане число {number}")


