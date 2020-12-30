# # 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# # Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# def bigsize(arr):
#     for x in range(0, len(arr), 1):
#         if arr[x] > 0:
#             arr[x] = "big"
#     return(arr)
# # print(bigsize([1, -2, -6, 2]))

# 2) Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# # Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# # Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# def countpos(arr):
#     count = 0
#     for x in range(0, len(arr), 1):
#         if arr[x] > 0:
#             count = count + 1 
#         arr[len(arr)-1] = count
#     print(count)
#     return(arr)
# # print(countpos([1, -2, 1, -2, 1]))
# # Note: See how I targeted a value in the list?

# # 3) Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# # Example: sum_total([1,2,3,4]) should return 10
# # Example: sum_total([6,3,-2]) should return 7
# def sum(arr):
#     sum = arr[0] 
#     for x in range(1, len(arr), 1):
#         sum = sum + arr[x]
#     return(sum)
# # print(sum([1, 1, 1, 1, 1]))
# # Note: Dont keep forgetting to print all the values

# 4) Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
# def average(arr):
#     summ = 0
#     ave = 0
#     for x in range(0, len(arr), 1):
#         summ = summ + arr[x]
#     ave = summ / len(arr)
#     return(ave)
# print(average([5, 2, 10, 7, 2]))

# # 5) Length - Create a function that takes a list and returns the length of the list.
# # Example: length([37,2,1,-9]) should return 4
# # Example: length([]) should return 0
# def length(arr):
#     return(len(arr))
# # print(length([1, 2, 3, 4, 5, 1]))

# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# # Example: minimum([37,2,1,-9]) should return -9
# # Example: minimum([]) should return False
# def min(arr):
#     minim = arr[0]
#     for x in range(1, len(arr), 1):
#         if arr[x] < minim:
#             minim = arr[x]
#     return(minim)
# # print(min([5, 0, 2, 6, 1]))
# # NOTE: so it seems that after the if statement the event needs to be indented
# # DO THE FALSE PART

# # 7) Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# # Example: maximum([37,2,1,-9]) should return 37
# # Example: maximum([]) should return False
# def maximum(arr):
#     max = 0
#     for x in range(0, len(arr), 1):
#         if arr[x] > max:
#             max = arr[x]
#     if arr == []:
#         return("False")
#     return(max)
# # print(maximum([5, 7, 3, 8, 2]))
# # # print(maximum([]))
# # NOTE: THEY BOTH WORK!!!

# 8) Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(someList):
#     output = { 'sumTotal': sum_total(someList), 'average': average(someList), 'minimum':minimum(someList), 'length': len(someList) }
#     print(output)
# ultimate_analysis([2,3,5])

# # 9) Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# # Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
# def reverselist(arr):
#     temp = 0 
#     for x in range(0, len(arr)//2, 1):
#         temp = arr[x]
#         arr[x] = arr[len(arr)-1-x] 
#         arr[len(arr)-1-x] = temp
#     return(arr)
# # print(reverselist([2, 2, 3, 1, 2, 3, 4]))
# # float means decimal
# # NOTES: you cannot simply divide in the for loop ranges. You have to use two methods:
# # First way: len(arr)//2
# # Second way: int(len(arr)/2)
# # GO OVER THIS ONE AGAIN
