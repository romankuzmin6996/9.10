list=[ ]
N = int(input("Cik bija cilvēku: "))
for i in range(N):
  mass=int(input("Kādā ir viņu masa: "))
  list.append(mass)
listsum=sum(list)
print(listsum)
listaverage=sum(list)/len(list)
print(listaverage)
if listsum > 300:
  print("Vini nedrikst braukt visi kopa!")
else: 
  print("Vini drikst braukt visi kopa!")