num = int(input("Введи ціле число: "))
for j in range(2, num + 1):
    for i in range(1, j + 1):
        print(i * j, end=" \t" )
    print()
