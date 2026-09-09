# Problem 3: Reverse a string using [::-1]

# Step 1: Create a string
s = "HELLO"

# Step 2: Reverse the string using [::-1]
# Explanation:
# [start:stop:step] is the general slicing syntax in Python
# start -> where to start (default is beginning)
# stop  -> where to end (default is end of string)
# step  -> how many steps to move forward (default is 1)
# If we use step = -1, it starts from the end and moves backwards,
# which effectively reverses the string.
reversed_s = s[::-1]

# Step 3: Print the original and reversed strings
print("Original String:", s)
print("Reversed String:", reversed_s)

# Extra Example: Any string can be reversed in the same way
example = "Python"
print("\nOriginal Example String:", example)
print("Reversed Example String:", example[::-1])
