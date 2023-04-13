# Lang_module_questions.py
s="hello"
# s[2]="a"
print(s[9])




# s = "My PO Box number is 310"
# print(s.startswith("My P"))

# strOne = str("Scaler Academy")
# strTwo = "Scaler Academy"
# print(strOne == strTwo)
# print(strOne is strTwo)
# print("Data" > "Dtaa", "Science" < "Scien")  return False False


# word = "Scaler Academy"
# n = len(word)
# word1 = word.upper()
# word2 = word.lower()
# converted_word = ""
# for i in range(n):
#      if i % 2 == 0:
#           converted_word += word2[i]
#      else:
#           converted_word += word1[i]
# print(converted_word)  
# ans: sCaLeR AcAdEmY

# input_string="radheenemyequals"
# print(input_string.split('e', maxsplit=2))

# print("python".join("@"))
# ans: @

# str1 = "quick brown fox word!"
# print(str1[12:15], str1[:5], str1[-5:-1], str1[8:110], str1[-4:])
# ans: fox quick word own fox word! ord!

# x=2
# if x > 2:
#     x = x*2
# if x > 4:
#     x = 0
# print(x)

# if False:                                       #1
#     print("Artificial Intelligence")
# elif True:                                      #2
#     print("Machine Learning")                   # this will be executed first
# elif True:                                      #3
#     print("Data Science")
# else:                                           #4
#     print("Deep Learning")     
# if False:
#     print(1 + "Two")
# else:
#     print(1 + 2)

# from array import array
# array2d = [array('i', (i*j for i in range(1,4))) for j in range(1,3)]
# print(array2d[1][2])   ans is 6

# from array import array
# arr = array('i', [1, 2, 3, 1, 4, 7, 9, 12])
# print(arr[1:4][1])   3

# from array import array
# arr= array("i",[2,1,3,4,7,6,4,6,9])
# for i in range(len(arr)+1):
#   if arr[i] in arr[i+1:]:
#     break
#  @ 3rd idx loop will break

# from array import array
# X= [array("i",[2,1,49,8,0]), array("i",[11,24,4,65,5])]
# y= [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
# t=[]
# transpose= [x for x in y]
# print(transpose)