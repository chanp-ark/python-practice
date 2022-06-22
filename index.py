print("""This is a puzzle favored by Einstein. You will be asked to
 enter a three digit number, where the hundred's digit differs 
 from the one's digit by at least two. The procedure will always yield 1089.""")
print('\n')
# Grab user input and store it in a variable
number = int(input("Enter a three-digit number: "))

def reverseNum(num):
  temp_num = num
  reverse_num = 0
  
  # Check using while loop
  while(temp_num>0):
    remainder = temp_num % 10
    reverse_num = (reverse_num * 10) + remainder
    temp_num = temp_num//10

  return reverse_num

reversed_number=reverseNum(number)

difference = abs(number - reversed_number)

# Display the result
print(f"For the number: {number} the reverse number is : {reversed_number}")
print(f"The difference between {number} and {reversed_number} is {difference}")

reversed_difference = reverseNum(difference)

print(f"The reverse difference is: {reversed_difference}")
print(f"The sum of {difference} and {reversed_difference} is: {difference + reversed_difference}")



