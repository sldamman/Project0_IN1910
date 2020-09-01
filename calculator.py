
def add(x,y):
    return x+y

def factorial(n):
    assert type(n)==int, "Factorial only defined for integers"
    s = n
    for i in range(1,n-1):
        s *= n-i
    return s

def sin(x, N):
    S = 0
    for n in range(N+1):
        S += ((-1)**n * x**(2*n+1))/factorial(2*n+1)
    return S

def divide(x,y):
    return x/y

def real_roots(a, b, c):
    #Solve second order equation (real roots only)
    r = b**2-4*a*c
    assert r >= 0, "no real roots"
    if r == 0:
        return -b/(2*a)
    else:
        x_1 = (-b + r**(1/2))/(2*a)
        x_2 = (-b - r**(1/2))/(2*a)
        return x_1, x_2

def kinetic_energy(m, h):
    #Calculating the kinetic energy of object with mass m,
    # after fall of h meters from stand-still.
    g = 9.81
    v = ( 2*g*h )**(1/2)
    return 1/2 * m * v**2