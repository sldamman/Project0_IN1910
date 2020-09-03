def add(x, y):
    ''' Input: x, y - int/float/str
    Returns the sum of inputs x and y'''
    return x + y

def factorial(n):
    '''Input: n - int
    Returns the factorial of input n'''
    assert type(n) == int, "Factorial only defined for integers"
    s = n
    for i in range(1, n-1):
        s *= n - i
    return s

def sin(x, N):
    '''Input: x - float
    N - int
    Returns N'th order taylor approximation to sin of x'''
    S = 0
    for n in range(N+1):
        S += ((-1)**n * x**(2 * n+1)) / factorial(2 * n+1)
    return S

def divide(x,y):
    return x/y

def quadratic_solver(a, b, c):
    '''Input: a,b,c - float
    Solve quadratic equation (real roots only) of form ax^2 + bx + c = 0
    from coefficients a,b,c
    '''
    r = b**2-4*a*c
    assert r >= 0, "no real roots"
    if r == 0:
        return -b/(2*a)
    else:
        x_1 = (-b + r**(1/2))/(2*a)
        x_2 = (-b - r**(1/2))/(2*a)
        return x_1, x_2

def kinetic_energy(m, h):
    '''Input: m,h - float
    Calculating the kinetic energy of object with mass m,
    after fall of h meters from stand-still. '''
    g = 9.81
    v = ( 2*g*h )**(1/2)
    return 1/2 * m * v**2
