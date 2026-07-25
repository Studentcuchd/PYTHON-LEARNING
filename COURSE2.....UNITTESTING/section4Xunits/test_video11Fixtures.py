import pytest

@pytest.fixture
def student():
    print("creating student")
    return "Parag"

def test_parag(student):
    print("current student=",student)
    assert student=="Parag"
    

@pytest.fixture
def database():
    print("opening database")
    yield "Running test"
    print("closing database")

def test_database(database):
    print(database)
    
    
@pytest.fixture
def login():
    print("login success")

@pytest.mark.usefixtures("login")
def test_dashboard():
    print("dashboard opened")


@pytest.fixture(autouse=True)
def bowser():
    print("open browser")
    yield
    print("close browser")
    
def test_browser1():
    print("running test 1")

def test_browser2():
    print("running test 2")
    

@pytest.fixture
def connection(request):
    print("connecting")

    def cleanup():
        print("disconnecting")
    
    request.addfinalizer(cleanup)
    return "executing test"   
  
def test_connection(connection):
    print(connection)