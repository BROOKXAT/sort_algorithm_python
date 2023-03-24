def triSelection(t) :
    for i in range(len(t)) :
        for j in range(i+1,len(t)):
            if t[j]<t[i]:
                t[j],t[i]=t[i],t[j]
t=[12,5,0,0,77,1,-1]
print(t)
triSelection(t)
print(t)






