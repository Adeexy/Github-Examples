from main import add_numbers

def test_addition():
    assert add_numbers(2, 3) == 5

def test_addition_with_negative_number():
    assert add_numbers(2, -3) == -1
