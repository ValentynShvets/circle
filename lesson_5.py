Slovo = str(input(" ВВедыть слово > "))
Slovo=Slovo.lower()
vovels= "aeiuoy"
i=0
b=0
for m in range(0, len(vovels)):
    for n in range(0, len(Slovo)):
        vovels[i] in Slovo


    if vovels[i] in Slovo:
        print (f"В слові є голоснa")
        b=1
        break

    i += 1

if b == 0:
    print("в словы немаэ голосних")