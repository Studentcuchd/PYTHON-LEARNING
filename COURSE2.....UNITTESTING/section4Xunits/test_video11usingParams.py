import pytest

@pytest.fixture(params=["Parag","Rahul","Aman"])
def student(request):
    return request.param

def test_student(student):
    print("first student",student)
    assert type(student)==str