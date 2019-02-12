name = str(input("Введіть ваше ім'я> "))
initials=""

for n in name.upper().split():

    initials += n[0]
print (initials)