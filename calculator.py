class Calculator:
    
    def __init__(self):
        pass
    
    def add(self, *args):
        sum = 0
        for values in args:
            number = int(values)
            sum += number
        
        return sum
    
    def multiply(self, *args):
        product = 1
        for values in args:
            number = int(values)
            product *= number
        
        return product
            