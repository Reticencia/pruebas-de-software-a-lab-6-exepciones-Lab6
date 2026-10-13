import pytest

class MyException(Exception):
    pass

class ExceptionsDemo:
    
    def divide(self, a, b):
        result = a / b
        print("Division result:", result)
    
    def access_list(self, lst, index):
        print("Element:", lst[index])
    
    def access_dict(self, dic, key):
        print("Value:", dic[key])
    
    def read_file(self, filename):
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    
    def access_attribute(self, obj):
        print(obj.tnonexistent_attribue)
    
    def check_positive(self, number):
        if number < 0:
            raise MyException("The number must be positive.")
        else:
            print("Valid number:", number)

def test_division_cero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)

def test_division_with_string():
    demo = ExceptionsDemo()
    with pytest.raises((TypeError, ZeroDivisionError)):
        demo.divide('8', 0)

def test_access_list():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([1, 3, 4], 7)

def test_division_dic():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({'color': 'rojo', 'forma': 'redonda'}, 'sabor')

def test_read_file():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file('sabor.txt')

def test_access_attribute():
    demo = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demo)

def test_check_positive():
    demo = ExceptionsDemo()
    with pytest.raises(MyException): 
        result = demo.check_positive(-100)

if __name__ == "__main__":
    demo = ExceptionsDemo()

    demo.divide(10, 0)   
    demo.divide("10", 2)  

    demo.access_list([1, 2, 3], 5)   
    demo.access_list(1, 0)   

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")  
    demo.access_dict("not_a_dict", "b")  

    demo.read_file("text_2.txt") 
    demo.read_file("text.txt") 

    demo.access_attribute(object())  

    try:
        demo.check_positive(-5)
    except MyException as e:
        print(" Custom error:", e)
