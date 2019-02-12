p = input("Введіть слово яке потрібно зашифрувати> ")
k= int(input("Введіть ключ"))
Shifr=""
for d in p:
    c = ord (d)
    ci = (c+k)
    if 97<=ci<=122:
        b = chr(ci)

    else:

    if 65<=ci<=90:
        b = chr(ci)

    else:

    else:
        ci = ci-26
        b=chr(ci)
    Shifr+=b
print (Shifr)
