from plates import is_valid

def test_letters_only():
    assert is_valid('NRVOUS')==True

def test_incorrect_length():
    assert is_valid('H')==False
    assert is_valid('OUTATIME')==False

def test_numbers():
    assert is_valid('CS50')==True
    assert is_valid('ECTO88')==True


def test_incorrect_place_of_letters():
    assert is_valid('CS50P2')==False

def test_incorrect_place_of_numbers():
    assert is_valid('XXXX01')==False
    assert is_valid('XXXX10')==True

def test_not_starting_alphabeticaly():
    assert is_valid('1X')==False
    assert is_valid('X2')==False
    assert is_valid('21')==False
    assert is_valid('XX')==True
    assert is_valid('YX')==True
    assert is_valid('YZ2321')==True

def test_punctuation():
    assert is_valid('PI3.14')==False
