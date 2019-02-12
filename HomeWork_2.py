Slovo = str(input("Введіть слово, я перевірю чи воно паліндром "))
Slovo=Slovo.lower()
Slovo1=Slovo[::-1]



if Slovo1 == Slovo:
    print(f"Cлово {Slovo} паліндром")

else:
    print(f"Cлово {Slovo} не паліндром")