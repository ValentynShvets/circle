Piramida = int(input("Введіть висоту піраміди> "))
block = "#"
n=Piramida-1
probil = " "
print(n * probil, end="")
for j in range(1, Piramida + 1):
    for i in range(0, j + 1):

        print(block, end="")

    print()

    print((n-1)* probil, end="")
    n -= 1
