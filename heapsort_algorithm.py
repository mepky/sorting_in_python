#praveen kumar
#39/cse/16028,0000184
#python_3.6.4
def heapify(list1,n,i):
        small=i
        l=2*i+1
        r=2*i+2
        #if left child is smaller than root
        if(l<n and list1[l]<list1[small]):
           small=l
           #if right child is smaller than root
        if(r<n and list1[r]<list1[small]):
           small=r
           #if smallest is not root
           #cheking this is min heap or not
        if(small!=i):
           (list1[i],list1[small])=(list1[small],list1[i])
           heapify(list1,n,small)


def heapsort(list1,n):
           #building heap 
           for i in range(len(list1)//2,-1,-1):
                   heapify(list1,n,i)
           #one by one extract an element from heap
           for i in range(n-1,-1,-1):
                   (list1[0],list1[i])=(list1[i],list1[0])
                   heapify(list1,i,0)


for i in range(5):
        list1=list(map(int,input("enter the number to be sorted:").split(' ')))
        n=len(list1)
        heapsort(list1,n)
        print(list1[::-1])

           
           
           
           
           
           
           
