import math
import pytest
import calculator

def test_add_exercise_1():
    '''Testing addition with integers '''
    assert calculator.add(1, 2) == 3, "Integer addition went wrong"

def test_add_exercise_2():
    '''Addition with float accounting for round-off errors with tolerance'''
    tol = 10**(-15)
    exp = 0.3
    assert abs(calculator.add(0.1, 0.2) - exp) < tol, "Floating point addition went wrong"

def test_add_exercise_3():
    '''Testing addition with strings '''
    exp = 'Hello world'
    assert calculator.add('Hello ', 'world') == exp, "String addition went wrong"

def test_factorial_exercise_4():
    '''Testing factorial calculation'''
    tol = 10**(-15)
    exp = math.factorial(10)
    msg = "Factorial calculation went wrong"
    assert abs( calculator.factorial(10) - exp ) < tol, msg

def test_sin_exercise_4():
    '''Testing taylor approx function of sine'''
    tol = 10**(-10)
    exp = math.sin(2.5)
    msg = "Sine calculation went wrong"
    assert abs( calculator.sin(2.5, 20) - exp ) < tol, msg

def test_divide_exercise_4():
    '''Testing division function'''
    tol = 10**(-10)
    exp = 100/3
    msg = "Division went wrong"
    assert abs( calculator.divide(100, 3) - exp ) < tol, msg

def test_quadratic_solver_exercise_4():
    '''Testing quadratic solver'''
    tol = 10**(-10)
    exp = (2, -1)
    msg = "Roots dont match"
    out = calculator.quadratic_solver(1, -1, -1)
    assert abs(out[0] + out[1] - exp[0] - exp[1]) < tol

def test_kinetic_energy_exercise_4():
    '''Testing kinetic energy, by checking equality to potential energy
    at start of fall (neglecting air resistance and assuming conservation of energy) '''
    tol = 10**(-10)
    m = 10
    g = 9.81
    h = 100
    E_pot = m * g * h 
    E_kin = calculator.kinetic_energy(m, h)
    assert abs(E_kin - E_pot) < tol, "Error in energy calculation"

def test_add_exercise_5():
    with pytest.raises(TypeError):
        calculator.add("Hello", 2)

def test_divide_exercise_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3, 0)
    

### Parameterized testing

@pytest.mark.parametrize(
    "input, exp_out", [ [(1,2), 3], [(3,5), 8], [(4.1,1.22),5.32], [("Hello ","world"), "Hello world"]])
def test_add_exercise_6(input, exp_out):
    tol = 10**(-15)

    if type(input[0]) == str:
        assert calculator.add(input[0], input[1]) == exp_out, "String addition went wrong"
    else:
        assert abs(calculator.add(input[0], input[1]) - exp_out) < tol, "Addition went wrong"

@pytest.mark.parametrize("x, y", [ (2,math.factorial(2)), (5,math.factorial(5)), (10,math.factorial(10))])
def test_factorial_exercise_6(x, y):
    tol = 10**(-15)
    assert abs(calculator.factorial(x) - y) < tol, "Error factorial"

@pytest.mark.parametrize("x, y", [ (2,math.sin(2)), (1.5,math.sin(1.5)), (4,math.sin(4))])
def test_sin_exercise_6(x,y):
    tol = 10**(-15)
    assert abs(calculator.sin(x,20) - y) < tol, "Error sin"

@pytest.mark.parametrize("input, exp_out", [ [(1,2), 1/2], [(3,5), 3/5], [(10.3,3.6),10.3/3.6]])
def test_divide_exercise_6(input, exp_out):
    tol = 10**(-15)
    assert abs(calculator.divide(input[0],input[1]) - exp_out) < tol, "Error division"

@pytest.mark.parametrize("input, exp_out", [ [(1,2,1), -1], [(2,5,2), (-1/2,-2)], [(1,-2,1), 1]])
def test_quadratic_solver_exercise_6(input, exp_out):
    tol = 10**(-10)
    if type(exp_out) == tuple:
        x_1, x_2 = calculator.quadratic_solver(input[0], input[1], input[2])
        assert abs( x_1 + x_2 - exp_out[0] - exp_out[1] ) < tol, "Error in roots"
    else:
        x = calculator.quadratic_solver(input[0], input[1], input[2])
        assert abs(x - exp_out) < tol, "Error in roots"

@pytest.mark.parametrize("input, exp_out", [ [(1,2), (1,2)], [(3,5), (3,5)], [(8.4,7.8),(8.4,7.8)]])
def test_kinetic_energy_exercise_6(input, exp_out):
    tol = 10**(-10)
    g = 9.81
    E_pot = exp_out[0] * g * exp_out[1]
    E_kin = calculator.kinetic_energy(input[0], input[1])
    assert abs(E_kin - E_pot) < tol, "Error energy"

    