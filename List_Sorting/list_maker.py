import random
import main

def listMake():
    min = int(input("min: "))
    max = int(input("max: "))
    size = int(input("size: "))
    num = 0
    list = []

    while num < size:
        i = random.randint(min, max)
        list.append(i)
        num = num + 1

    main.sorter(list)

listMake()
