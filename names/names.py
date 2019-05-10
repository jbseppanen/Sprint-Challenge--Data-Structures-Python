import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Original Solution>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# First pass solution>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# 2nd pass solution>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
names_1.sort()
names_2.sort()
i = 0
j = 0
while i < len(names_1)-1 or j < len(names_2)-1:
    if names_1[i] == names_2[j]:
        duplicates.append(names_1[i])
        i += 1
        j += 1
    elif names_1[i] > names_2[j]:
        j += 1
    else:
        i += 1

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
