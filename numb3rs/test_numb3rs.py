from numb3rs import validate


def test_maxval():
    assert validate('255.255.255.255')==True

def test_incorrect_val():
    assert validate('512.512.512.512')==False
    assert validate('112.12.122.51')==True
    assert validate('1.512.0.1')==False
    assert validate('1.1.512.1')==False
    assert validate('1.1.512.1')==False
    assert validate('1.2.3.1000')==False

