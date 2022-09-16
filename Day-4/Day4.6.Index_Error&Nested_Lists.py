# Index_Error 
#   Lists = ["Cherry", "Mango", "Apple"]
##  print(Lists[3])
# Output we will get like "IndexError: list index out of range"
Lists = ["Cherry", "Mango", "Apple"]
last = (len(Lists)-1)
print(Lists[last])

# Nested_Lists( lists of lists)
X = [1, 2, 3, 4, 5, 6]
Y = [1, 2, 3]
Z = [4, 5, 6]
print([Y,Z])