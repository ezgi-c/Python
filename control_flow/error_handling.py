nums = [5, 2, 3, 10]

try:
    avg = sum(nums) / len(nums)
    print('The average of the list is:', avg)

except: # this runs if the try fails. e.g., when the array includes strings
    print('Cannot compute average - make sure you enter a list of integers')

finally:
    print('Feel free to return the code with another list of integers')