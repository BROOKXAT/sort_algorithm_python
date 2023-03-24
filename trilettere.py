
def triSelection(x) :
    t=list(x)
    z=''
    for i in range(len(t)) :
        for j in range(i+1,len(t)):
            if  t[j].lower()<t[i].lower():
                t[j],t[i]=t[i],t[j]
            elif t[j].lower()==t[i].lower():
                if t[j]<t[i]:
                    print(t[j])
                    t[j],t[i]=t[i],t[j]
    print(t)

    for j in range(len(t)) :
        z=z+t[j]
    return z
print(triSelection("hellLo"))
