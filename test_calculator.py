import calculator, math, pytest

@pytest.mark.parametrize(
    "input, exp_out", [ [(1,2), 3], [(3,5), 8], [(4.1,1.22),5.32], [("Hello ","world"), "Hello world"]])
def test_add(input,exp_out):
    tol = 10**(-15)
    if type(input[0])==str:
        assert calculator.add(input[0],input[1]) == exp_out, "String addition went wrong"
    else:
        assert abs(calculator.add(input[0],input[1])-exp_out)<tol, "Addition went wrong"

@pytest.mark.parametrize("x, y", [ (2,math.factorial(2)), (5,math.factorial(5)), (10,math.factorial(10))])
def test_factorial(x,y):
    tol = 10**(-15)
    assert abs(calculator.factorial(x) - y) < tol, "Error factorial"

@pytest.mark.parametrize("x, y", [ (2,math.sin(2)), (1.5,math.sin(1.5)), (4,math.sin(4))])
def test_sin(x,y):
    tol = 10**(-15)
    assert abs(calculator.sin(x,20) - y) < tol, "Error sin"

@pytest.mark.parametrize("input, exp_out", [ [(1,2), 1/2], [(3,5), 3/5], [(10.3,3.6),10.3/3.6]])
def test_divide(input, exp_out):
    tol = 10**(-15)
    assert abs(calculator.divide(input[0],input[1]) - exp_out) < tol, "Error division"

@pytest.mark.parametrize("input, exp_out", [ [(1,2,1), -1], [(2,5,2), (-1/2,-2)], [(1,-2,1), 1]])
def test_real_roots(input, exp_out):
    tol = 10**(-10)
    if type(exp_out)==tuple:
        x_1, x_2 = calculator.real_roots(input[0],input[1],input[2])
        assert abs( x_1 + x_2 - exp_out[0] - exp_out[1] ) < tol, "error roots"
    else:
        x = calculator.real_roots(input[0],input[1],input[2])
        assert abs(x - exp_out) < tol, "Error roots"

@pytest.mark.parametrize("input, exp_out", [ [(1,2), (1,2)], [(3,5), (3,5)], [(8.4,7.8),(8.4,7.8)]])
def test_kinetic_energy(input,exp_out):
    #Kinetic energy after a fall of x meters from stand-still \
    #should equal the potential energy at height x (neglecting friction)
    tol = 10**(-10)
    g = 9.81
    E_pot = exp_out[0] * g * exp_out[1]
    E_kin = calculator.kinetic_energy(input[0], input[1])
    assert abs(E_kin - E_pot) < tol, "Error energy"

def test_add_TypeError():
    with pytest.raises(TypeError):
        calculator.add("Hello", 2)

def test_add_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3, 1)
