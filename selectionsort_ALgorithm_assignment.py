#python_3.6.4
#SELECTION SORT ALGORITHM
A=list(map(int,input("enter the input array:").split(' ')))
for i in range(len(A)-1):
       min_index=i;
       for j in range(i+1,len(A),1):
               #finding the minimum element
               if(A[min_index]>A[j]):
                       min_index=j
        #swaping the minimum element with index i               
       (A[i],A[min_index])=(A[min_index],A[i])


print(A)
        
