list1=[1,2,1]
list2=[2,3,4]

list1_copy=list1.copy()
list1_copy.reverse()

if(list1_copy==list1.copy()):
    print("palindrome list")
else:
    print("not a palindrome list")

print("list1")