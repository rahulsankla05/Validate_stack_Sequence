# Sorting_Array_linear.py
A=[2,0,0,1,1,2]
i,mid,high=0,0,len(A)-1
# Dutch national Flag Approach
while mid<=high:
    if A[mid]==0:
        temp=A[i]
        A[i]=A[mid]
        A[mid]=temp
        i+=1
        mid+=1
    elif A[mid]==1:
        mid+=1
# if A[mid]==2 then replace it high idx
    else:
        temp=A[mid]
        A[mid]=A[high]
        A[high]=temp
        high-=1
print(A)

