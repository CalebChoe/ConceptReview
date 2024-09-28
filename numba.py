import random
import time
from numba import njit

# sleptime = input("How fast do you want to run, fast, medium, instant, or slow? ")
'''
options = ["fast", "medium", "instant", "slow"]
if sleptime not in options:
    print(f"bro choose a value, '{sleptime}' isn't one of the options.")
    quit()

speed = 0.3
if sleptime == "fast":
    speed = 0.1
elif sleptime == "medium":
    speed = 0.3
elif sleptime == "instant":
    speed = 0
else:
    speed = 0.5
'''

rows = int(input("how many rows: "))
columns = int(input("how many columns: "))

start = time.time()
def run():
    speed = 0

    def lazyslep():
        time.sleep(speed)

    x = []
    y = []
    for i in range(rows):
        x.append([])

    for i in range(rows):
        y.append([])

    result = x

    for i in x:
        for j in range(columns):
            i.append(random.randint(1, 10))

    for i in y:
        for j in range(columns):
            i.append(random.randint(1, 10))

    print("matrix X")
    for i in x:
        print(i)
        lazyslep()

    print("matrix Y")

    for i in y:
        print(i)
        lazyslep()

    addresulthelp = x
    subresulthelp = y
    for i in range(rows):
        for j in range(columns):
            a = x[i][j]
            b = y[i][j]
            # addresult[i][j] = a + b
            addresulthelp[i][j] = f"index[{i}][{j}] result for addition: {a}+{b}={a + b}"
            # subresult[i][j] = a - b
            subresulthelp[i][j] = f"index[{i}][{j}] result for subtraction: {a}-{b}={a - b}"

    '''
    addresult = [[X[row][column] + Y[row][column]
                   for column in range(len(X[0]))]
                  for row in range(len(X))]
    subresult = [[X[row][column] - Y[row][column]
                   for column in range(len(X[0]))]
                  for row in range(len(X))]
    '''

    print("\nMatrix Addition")
    for i in addresulthelp:
        for j in i:
            print(j)
            lazyslep()

    print("\nMatrix Subtraction")
    for i in subresulthelp:
        for j in i:
            print(j)
            lazyslep()

end = time.time()

print(end - start)
