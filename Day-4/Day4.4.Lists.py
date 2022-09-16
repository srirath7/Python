# Lists is we call a data structure. Its a way of organising data. 

a = 0
b = 1
c = 2
d = 3

#If you need to store entire countries in USA. so we need to include in a single variable.
# Lists = ["a","b","c","d"]

Lists = ["a","b","c","d"]
#to print (a)
print(Lists[0])
#to print (d)
print(Lists[-1])

# to print a add string "empty" as 1 then
Lists = ["","a","b","c","d"]
#to print (a)
print(Lists[1])
#to print (d)
print(Lists[-1])

# to modify/replace already written name
Lists = ["Chey", "Mango", "Apple"]
Lists[0] = "Cherry"
print(Lists[0])
# to add extra variable at end
Lists.append("Pineapple")
print(Lists)
# to add multiple variables
Lists.extend(["Jack","Grapes"])
print(Lists)

# delete Apple and add at last as a variable
del Lists[2]
print(Lists)
Lists.append("Apple")
print(Lists)

# whether available or not "Apple"
print("Apple" in Lists)
#Lists sort
Lists = sorted(Lists)
print(Lists)

# setting lists individual set of letters
Lists = set(Lists[2])
print(Lists)

#Note Lists cannot mix use like Lists = [123, "Mango"]