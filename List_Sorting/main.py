import random

def sorter(list):
    print(str(list))
    output = []
    highest = max(list)
    num = min(list)
    if len(list) != len(output):
        while num < highest:
            for item in list:
                i = item
                if i == num:
                    output.append(i)
                    print("Found Number! " + str(num))
            num = num + 1
    print(str(output))
