import source.my_functions as my_functions 

#def test_add():
#    pass

def test_add():
    result = my_functions.add(number_one=1, number_two=2)


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10,0)