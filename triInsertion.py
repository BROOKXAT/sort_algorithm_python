def triInsertion(t) :
    for i in range(1,len(t)) :
        x = t[i]
        j = i-1
        while x < t[j] and j >= 0 :
            t[j+1] = t[j]
            j = j-1
        t[j+1] = x
    return t

print(triInsertion([3,-1,9,0]))
        