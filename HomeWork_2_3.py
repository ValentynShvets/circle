Slovo = str(input(" ВВедыть слово > "))
Slovo=Slovo.lower()
vowels= "aeiuoy"
i=0
b=0
for m in range(0, len(vowels)):
    for n in range(0, len(Slovo)):
        2*vowels[i] in Slovo


    if 2*vowels[i] in Slovo:
        print (f"В слові є подвоєння голосних")
        b=1
        break

    i += 1

if b == 0:
    print("В слові немає подвоєння голосних")