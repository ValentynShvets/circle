tt = tuple()
print(id(tt), tt)
tt+=12, 32, 15
print(id(tt), tt)

#a,b,c=tt
#print(a, b, c)


a, _, _=tt
print(a)

ll = list(tt)
print(ll)

tt2 = tuple(ll)
print(tt2)

print(type(tt))

#for num, item in enumerate(tt):
 #   print(f"{num} ==> {item}")

for t,_ in enumerate(tt):
    print(t)
