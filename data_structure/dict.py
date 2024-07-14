letters = ['a', 'a', 'b', 'c', 'c', 'c']

def simp_dict(lst):
    d = dict()
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
    most = max(d, key=d.get)
    print(most, d[most])
    least = min(d, key=d.get)
    print(least, d[least])

simp_dict(letters)
