def countSort(s):
    a=[]
    for i in s:
        a.append(ord(i))
    a.sort()
    z=""
    for j in a:
        z+=chr(j)
    return z