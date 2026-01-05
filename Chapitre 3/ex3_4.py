def pascal_r(n,k):
    if k == 0 or k == n:
        return 1
    else: 
        return pascal_r(n-1,k-1) + pascal_r(n-1,k)

pascal_cache = {} # dictionnaire vide

def pascal_rc(n, k):
    global pascal_cache

    if k == 0 or k == n:
        return 1
    if (n,k) in pascal_cache:
        return pascal_cache[(n,k)]
    else:
        temp = pascal_rc(n-1,k-1) + pascal_rc(n-1,k)
        pascal_cache[(n,k)] = temp
        return temp
    
print(pascal_r(5,2))

for i in range(10+1):
    for j in range(i+1):
        print(pascal_rc(i,j), end =" ")
    print()

def pascal_i(n,k):
    if k == 0 or k == n:
        return 1
    else:
        t = {} # t va contenir des éléments du triangle
        for i in range(n+1):
            t[(i,0)] = 1
            t[(i,i)] = 1
            for j in range (1,i):
                t[(i,j)] = t[(i-1, j-1)] + t[(i-1,j)]
    return t[(n,k)]

print(pascal_i(5,2))

# maxi = 0
# for elemen in pascal_cache:
#     if pascal_cache[elemen] > maxi:
#         maxi = pascal_cache[elemen]

# print(maxi)