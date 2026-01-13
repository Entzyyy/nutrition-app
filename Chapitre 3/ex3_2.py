def collatz_rec(u,n):
    if n==0:
        return u
    else:
        if u % 2 == 0:
            unext=u // 2
        else:
            unext = 3 * u + 1
        return collatz_rec(unext,n-1)
    
u0 = int(input("Premier terme: "))
un = collatz_rec(u0,100)
print(un)

def collatz_it(u,n):
    for i in range (n):
        if u%2 == 0:
            u = u // 2
        else:
            u = u*3+1
    return u

u0 = int(input("Premier terme: "))
un_rec = collatz_rec(u0, 100)
print(un_rec)
un_it = collatz_it(u0,100)
print(un_it)

def collatz_check(u):
    count=0
    while u != 1:
        u = collatz_it(u,1)
        count += 1
    return count

print(collatz_check(10))

for i in range(1,10):
    n = collatz_check(i)
    print(f"{i}: {n}")





