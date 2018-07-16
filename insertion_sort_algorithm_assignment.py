#insertion sort algorithm
A=list(map(int,input("enter the input array:").split(' ')))
n=len(A)
for i in range(1,n):
        hole=i;
        value=A[i]
        while(hole>0 and A[hole-1]>value):
                A[hole]=A[hole-1]
                hole=hole-1
        A[hole]=value

print(A)
                
                
