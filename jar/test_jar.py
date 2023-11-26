from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert str(jar) == ""
    assert jar.size==0
    assert jar.capacity==12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

def test_invalid_deposit():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(7)
        jar.deposit(9)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(9)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

def test_invalid_withdraw():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(7)
        jar.withdraw(9)
