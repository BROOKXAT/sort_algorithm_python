def swap(l,start, end) :
    '''
    this function take the last element (pivot) and place it at the right index
    every element at the right of pivot is lesser then him 
    and the elements at the left of pivot are greather then him 
    and return the index of the pivot
    '''
    # pivot is the last element 
    pivot = l[end]
    swap_marker = start -1
    for  i in range(start,end+1) :
        if l[i] > pivot :

            continue
        else :
            swap_marker += 1
            if swap_marker == i :
    
                continue
            if swap_marker < i :
                l[i] , l[swap_marker] = l[swap_marker] , l[i]
    return swap_marker

def quick_sort(l,start,end) :
    if start < end :
        pivot_index = swap(l,start,end)
        quick_sort(l,start,pivot_index-1)
        quick_sort(l,pivot_index+1,end)


l = [3,2,0,1,5,8,7,6,9,4]
print(quick_sort(l,0,9))
print(l)