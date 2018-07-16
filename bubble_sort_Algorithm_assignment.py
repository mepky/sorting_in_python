#praveen kumar
#Indian institute of information technology kalyani
#python_3.6.4
#bubble_sort algorithm
A=list(map(int,input("enter the input array:").split(" ")))
n=len(A)
for k in range(n):
        for i in range(n-1):
                if(A[i]>A[i+1]):
                        temp=A[i]
                        A[i]=A[i+1]
                        A[i+1]=temp

print(A)
                        
