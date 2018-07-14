#Author
#praveen kumar
#Indian institute of information technology kalyani



def merge_sort(l):
    ret = []
    if( len(l) == 1):
        return l;
    mid  = len(l) //2
    lower = merge_sort(l[:mid])
    upper = merge_sort(l[mid:])
    lower_len = len(lower)
    upper_len = len(upper)
    i = 0
    j = 0
    while i != lower_len or j != upper_len:
        if( i != lower_len and (j == upper_len or lower[i] < upper[j])):
            ret.append(lower[i])
            i += 1
        else:
            ret.append(upper[j])
            j += 1

    return ret
print("Enter the unsorted array: ",end="")
l=list(map(int,input().split()))
ar = merge_sort(l)
print("Array after sorting: ",end="")
print(*ar)
