#python_3.6.4
#quick sort algorithm
def quick_sort(A,start,end):
        
        if(start<end):
                pindex=partition(A,start,end)
                quick_sort(A,start,pindex-1)
                quick_sort(A,pindex+1,end)


def partition(A,start,end): 
        pivot=A[end]
        pindex=start
        for i in range(start,end):
                if(A[i]<=pivot):
                        (A[i],A[pindex])=(A[pindex],A[i])
                        pindex=pindex+1
        (A[pindex],A[end])=(A[end],A[pindex])
        return pindex
#input list
for i in range(5):
        nlist=list(map(int,input("enter the input array:").split()))
        quick_sort(nlist,0,len(nlist)-1)
        print('output is:', nlist)


#programm end
