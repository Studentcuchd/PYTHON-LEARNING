import pytest
def fizzbuzz(value):
    return str(value)



def checking_fizzbuzz(value,expected_val):
    result=fizzbuzz(value)
    assert result==expected_val
    

def test_case1():
    checking_fizzbuzz(1,"1")
    
def test_case2():
    checking_fizzbuzz(2,"2")
    
def test_case3():
    checking_fizzbuzz(3,"3")
    
def test_case4():
    checking_fizzbuzz(4,"4")

# Best way
