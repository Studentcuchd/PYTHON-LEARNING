def setup_module(module):
    print("Module Setup")

def teardown_module(module):
    print("Module Teardown")

def setup_function(function):
    if function==test1:
        print("setup test 1")
    elif function==test2:
        print("setup test 2")
    else:
        print("another test setup")
  
def teardown_function(function):
    if function==test1:
        print("tearing test 1")
    elif function==test2:
        print("tearing test 2")
    else:
        print("another test tearing")  
        
def test1():
    print("executing test 1")
    assert True
    
def test2():
    print("executing test 2")
    assert True