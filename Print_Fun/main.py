def print_fun(n):
    if n == 0:
        return 0
    if n == 1:
        return 11
    tracker = n  # number
    periodlen = (tracker * 2) - 2 # number (tracks how many periods to place)
    while tracker > 0:
        for i in range(n - tracker + 1):
            print(n - i, end = '')  # 8-0,8-1,8-2
        print(periodlen * '.', end = '')
        for i in range(tracker-1, n):
            print(i + 1, end = '') #0+1,0+2,0+3
        print("")
        periodlen -= 2
        tracker -= 1
    print("")

num = int(input())
print_fun(num)
