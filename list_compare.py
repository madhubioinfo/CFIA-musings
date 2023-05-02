# Read the first file and convert its contents to a list
with open('complete_listeria', 'r') as file1:
    list1 = file1.read().split()

# Read the second file and convert its contents to a list
with open('1_2', 'r') as file2:
    list2 = file2.read().split()

# Subtract the two lists and convert the result back to a list
result = list(set(list1) - set(list2))

with open('output.txt', 'w') as f:
    for key in result:
        f.write(key + '\n')
