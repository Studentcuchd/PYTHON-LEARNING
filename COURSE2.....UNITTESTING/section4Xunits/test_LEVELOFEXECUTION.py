def setup_module(module):
    print("1. Module Setup")


def teardown_module(module):
    print("8. Module Teardown")


def setup_function(function):
    print("2. Function Setup")


def teardown_function(function):
    print("4. Function Teardown")


def test_add():
    print("3. Executing test_add")


class TestMath: 

    @classmethod
    def setup_class(cls):
        print("5. Class Setup")

    @classmethod
    def teardown_class(cls):
        print("8. Class Teardown")

    def setup_method(self, method):
        print("6. Method Setup")

    def teardown_method(self, method):
        print("7. Method Teardown")

    def test_mul(self):
        print("Executing test_mul")

    def test_div(self):
        print("Executing test_div")