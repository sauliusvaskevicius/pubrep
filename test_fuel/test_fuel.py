from fuel import convert, gauge
import pytest

def test_convert_proper_math():
    assert convert('3/4')==75
    assert convert('1/3')==33

def test_convet_aproximation():
    assert convert('2/3')==67

def test_convert_divisionbyzero():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')

def test_convert_more_than_F():
    with pytest.raises(ValueError):
        convert('10/3')

def test_convert_text():
    with pytest.raises(ValueError):
        convert('three/four')

def test_convert_slash():
    with pytest.raises(ValueError):
        convert('5-7')

def test_gauge_F():
    assert gauge(99)=='F'

def test_gauge_E():
    assert gauge(0)=='E'
    assert gauge(1)=='E'

def test_gauge_m():
    assert gauge(19)=='19%'

