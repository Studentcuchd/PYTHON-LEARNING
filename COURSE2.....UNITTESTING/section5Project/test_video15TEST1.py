from Checkout import Checkout
import pytest
def test_cancreateinstancecheckout():
    checkout_obj=Checkout()
    
def test_canaddprice():
    co=Checkout()
    co.addItemPrice("a",1)
    

def test_addItem():
    co=Checkout()
    co.addItem("a")
    
    
    
    
    
# pytest -v -s test_video15TEST1.py