from bank import value

def test_value_for_hello():
    assert value("Hello")==0
    assert value(" Hello ")==0
    assert value("Hello, Newman")==0

def test_value_for_h():
    assert value("How you doing?")==20

def test_value_for_():
    assert value("What's happening?")==100
    assert value("What's up?")==100
