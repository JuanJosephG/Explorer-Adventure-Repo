


def find_second_largest(numbers):
    print(numbers)
    number_array = list(set(numbers))   #Putting numbers into list and using set() to remove repeat numbers/put in order
    if len(number_array) == 1:      #if length of the array is 1 then the array will have no second greatest number
        print("No second largest number")
    else :                           #if array is length greater than 1 then output will be second greatest number
     print(number_array)

     number_array.remove(max(number_array)) #removes current max number
     print(max(number_array)) #prints new max number which is second greatest

#Test Cases
     #uncomment to run test cases!

# numbers1 = [5,2,8,1,9,3]
# print(find_second_largest(numbers1))

# numbers2 = [4,4,4,4]
# print(find_second_largest(numbers2))

# numbers3 = [10,5,10,20,20,15]
# print(find_second_largest(numbers3))