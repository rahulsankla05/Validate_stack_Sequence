# Validate_stack_Sequence.py
pushed=[1,2,3,4,5]
popped=[4,5,3,2,1]

# consider an empty stac
stac=[]
# consider a int variable j initially 0 to traverse in Popped array
j=0
# traverse in list pushed and push the element into the stac
for i in range (len(pushed)):
            
            stac.append(pushed[i])
# till stack not empty check stack top elem==popped elem, if both are same then pop
            while len(stac)>0 and stac[-1]==popped[j]:

                stac.pop()
# increment j+=1
                j+=1
# return true if stack== empty otherwise return False
if len(stac)==0:
        print(True)
else:
        print(False)
     