def bubble_sort(l) :
    for k  in l :
        for i,k in enumerate(l[:-1]) :
            if l[i] > l[i+1] :
                l[i] , l[i+1] = l[i+1] , l[i]

    return l

print(bubble_sort([3,-1,9,0]))