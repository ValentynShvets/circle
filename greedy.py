price = float(input("O hi! How much change is owed==> "))
list = [0.01, 0.05, 0.1, 0.25]
a = 0

while price > 0:
    if price >= 0.25:
        price-=list[3]
        a+=1
    elif 0.1<=price<0.25:
        price-=list[2]
        a += 1
    elif 0.05<=price<0.1:
        price-=list[1]
        a += 1
    else:
        price -=list[0]
        a += 1
print(f"Продавець видав {a} монети")


