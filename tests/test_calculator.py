from calculator_simple.calculator import Calculator

calculator = Calculator()

def test_add_two_numbers():
    assert calculator.add(1,2) == 3

def test_add_many_numbers():
    assert calculator.add(1,6,3,9,7,) == 26

def test_product_of_two_numbers():
    assert calculator.multiply(2,7) == 14

def test_product_of_many_numbers():
    assert calculator.multiply(1,7,1) == 7

# def test_divide_two_numbers():
#     assert calculator.divide(1,2) == 0.5

# def tets_divide_many_numbers():
#     assert calculator.divide(2,1) == 2
    
    

