
arraylist=[1,2,3,4,5]
                   #also called python list
print(arraylist)        # for printing the entire list

print(arraylist[4])     #for accessing a particular element in array or simply python list
                                                
print(arraylist[2:4])     #for slicing 
print(arraylist[:])       #for printing the entire list
print(arraylist[-2:])     #  here from 3 to 5 but 3 would not be printed
num=["mohit","ojha","python","developer"]
num.append(9)          #for appending to last
print(num)
arraylist.extend(num)  #for extending something here arraylist is just the initial list to which i added num list at last
                       # and ultimately printed an extended arraylist to get the result
print(arraylist)


print(arraylist.index(2))  # for finding the index of the data in the list enterd by the user
num1=["m","o","p","q","r","s"]
print(num1.insert(2,"intel"))   # for inserting some thing in list  {current list} 
num1.extend(num)
print(num1)
num1.remove(9)                  # for removing any thing in a list
print(num1)
num1.insert(7,"hello")           # for inserting anything in the given list {extended list} with removal of 9
print(num1)
num1.reverse()                  #for reversing any thing in  python 
print(num1)

input()
