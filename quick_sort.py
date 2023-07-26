def swap(l) :
    pivot = l[-1]
    swap_marker = -1
    for  i,j in enumerate(l) :
        if l[i] > pivot :
            print("curent: ",i," swap marker: ",swap_marker)
            continue
        else :
            swap_marker += 1
            if swap_marker == i :
                print("curent: ",i," swap marker: ",swap_marker)
                continue
            if swap_marker < i :
                l[i] , l[swap_marker] = l[swap_marker] , l[i]
                print("curent: ",i," swap marker: ",swap_marker)
    return l
        
l = [3,2,0,1,5,8,7,6,9,4]
print(swap(l))