# 1. Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop 
# to return a sublist of the input list. The sublist should contain the same values of the original list up until it 
# reaches the number 5 (it should not contain the number 5).

def sublist(input_list):
    output_list = []
    index_num = 0
    while index_num < len(input_list):
        if input_list[index_num] != 5:
            output_list.append(index_num)
            index_num += 1
        else:
            break
    return output_list
lst = [1,2,3,4,5,7]
print(sublist(lst))

# 2. Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once 
# the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.

def check_nums(inputList):
    outputList = []
    indexNum = 0
    while indexNum < len(inputList):
        if inputList[indexNum] != 7:
            outputList.append(inputList[indexNum])
            indexNum += 1
        else:
            break
    return outputList
lst = [1,2,3,4,5,6,7,8,9]
print(check_nums(lst))



# 3. Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return 
# a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” 
# (it should not contain the string “STOP”).

def sublist(inputList):
    outputList = []
    indexNum = 0
    while indexNum < len(inputList):
        if inputList[indexNum] != "STOP":
            outputList.append(inputList[indexNum])
            indexNum += 1
        else:
            break
    return outputList
lst = ["SALMAN", "IS", "FROM", "PAKISTAN", "STOP", "HE", "IS", "GOOD", "MAN"]
print(sublist(lst))

# 4. Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list 
# until the string that appears is “z”. The function should return the new list.

def stop_at_z(inputList):
    outputList = []
    indexNum = 0
    while indexNum < len(inputList):
        if inputList[indexNum] != "z":
            outputList.append(inputList[indexNum])
            indexNum += 1
        else:
            break
    return outputList
lst = ["a", "b", "c", "d", "w", "z", "k", "l", "m", "n"]
print(stop_at_z(lst))

# 5. Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while 
# loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

sum1 = 0
sum2 = 0
index_num = 0
lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
while index_num < len(lst):
    sum2 = sum2 + lst[index_num]
    index_num += 1
print(sum1 == sum2)

# 6. Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the 
# list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. 
# (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) 
# If you want to make this even more of a challenge, do this without slicing

def beginning(inputList):
    outputList = []
    indexNum = 0
    while indexNum < len(inputList):
        if inputList[indexNum] != "bye":
            outputList.append(inputList[indexNum])
            indexNum += 1
        else:
            break
    return outputList
lst = ["SALMAN", "IS", "FROM", "PAKISTAN", "STOP","bye", "HE", "IS", "GOOD", "MAN"]
print(beginning(lst))
