# p=[[5,6,7],[8,7,9],[0,0,0]]
# sum_dig_elems=0
# # n=len(p)
# for i in range(len(p)):
#     for j in range(len(p[i])):
#         if i+j==len(p)-1:
#             sum_dig_elems+=p[i][j]
# print("sum_sec_diag_elems is:",sum_dig_elems)
# class A:
#  def __init__(self, name, sound="Grrrr"):
#    self.name = name
#    self.sound = sound

#  def make_noise(self):
#    print("{} says, {}".format(self.name,self.sound))

# class B(A):
#  def __init__(self, name="Rachel"):
#    super().__init__(name, "Meow!")

#  def make_noise(self,sound="Grrrr!"):
#    print("{} says, {}".format(self.name, sound))

# pet_cat = B()
# pet_cat.make_noise()
Str=input("enter your string:")
ans=[]
hs={"a","e","i","o","u"}
for ch in Str:
    if ch in hs:
        if ch not in ans:
            ans.append(ch)
            # print(ch,"Vowel found",Str.count(ch), "times")
            print("{} occured {} times".format(ch,Str.count(ch)))
'''
// to count number of character occurances//
hm={}
for ch in Str:
    if ch not in hm:
        hm[ch]=1
    hm[ch]+=1
print(hm)
# print(ch,"occured",Str.count(ch),"times")
'''

            