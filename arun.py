a = [12,43,3,65,345,36]
x = 0
i=0
for data in a:
    if x<data:
        x = data
        i=i+1
        ind = i
    else:
        i=i+1

print(ind)
