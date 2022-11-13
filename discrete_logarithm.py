import math

def baby_step_giant_step(g, h, p):
    #  h = g^x mod p
    m = math.ceil(math.sqrt(p - 1))

    tbl = {pow(g, i, p): i for i in range(m)}

    c = pow(g, m * (p - 2), p)

    for j in range(m):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * m + tbl[y]

def ext_euclid(a, b):
    if b == 0:
        return a, 1, 0
    
    else:
        d, xx, yy = ext_euclid(b, a % b)
        x = yy
        y = xx - (a / b) * yy

        return d, x, y

def inverse(a, n):
    return ext_euclid(a, n)[1]

def xab(x, a, b, G, H, P, Q):
    sub = x % 3

    if sub == 0:
        x = x*G % P
        a = (a+1) % Q

    if sub == 1:
        x = x * H % P
        b = (b + 1) % Q

    if sub == 2:
        x = x*x % P
        a = a*2 % Q
        b = b*2 % Q

    return x, a, b

def pollard(G, H, P):
    # P: prime
    # H:
    # G: generator
    Q = (P - 1) / 2  # sub group

    x = G * H
    a = 1
    b = 1

    X = x
    A = a
    B = b

    for i in range(1, P):
        x, a, b = xab(x, a, b, G, H, P, Q)

        X, A, B = xab(X, A, B, G, H, P, Q)
        X, A, B = xab(X, A, B, G, H, P, Q)

        if x == X:
            break


    nom = a - A
    denom = B - b

    return int(inverse(denom, int(Q) * nom) % int(Q))

if __name__ == '__main__':
    print(f"355407489 = 7894352216^{baby_step_giant_step(7894352216, 355407489, 604604729)} (mod 604604729)")
    print(f"22 = 5^{pollard(5, 22, 53)} (mod 53)")
