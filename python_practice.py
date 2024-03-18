# List of Integers
numbers = [1, 3, 4, 2]

# Sorting list of Integers in asc
numbers.sort()
print(numbers)

# Sorting list of Integers in desc
numbers.sort(reverse=True)
print(numbers)

# List of Floating point numbers
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]

# Sorting list of Floating point numbers
decimalnumber.sort()

print(decimalnumber)

# List of strings
words = ["Geeks", "For", "Geeks"]

# Sorting list of strings
words.sort()

print(words)

a=[19, 23, 73, 14, 15, 87, 54, 23]
l= len(a);
x=input("Enter a number to search in an array")


for check in range(0,l):
    if(a[check]==x):
         count=1;
    # else:
    #     count=0;

if(count==1):
    print("Found")
else:
    print("Not Found")

