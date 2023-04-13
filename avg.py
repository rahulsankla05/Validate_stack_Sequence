# def getstrings(self,n,i,output):
#         # base case
#     if i==n:
#         print(output)
#         return
#     # // Rec case//
#     output[i]="4"
#     self.getstrings(n,i+1,output)
#     output[i]="5"
#     self.getstrings(n,i+1,output)

#     def string_num(self,output):
#         output=[]*3
#         return self.getstrings(3,0,output)
        
    # print(3,0,output)
# A=[1,2,3,1]
# s,e=0,len(A)-1
# while s<e:
#     mid=(s+e)//2
#     if A[mid]>A[mid+1]:
#         e=mid
#     else:
#         s=mid+1
# print("Peak element is:", A[s])
s="...."
n=[]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        s[i-1]="--"
        n.append("--"+"..")
        x=s[i]
    else:
        n.append("..")
print(n)



