from seasons import tominutes,mintowords
import pytest

def test_tominutes_AND_mintowords():
    assert mintowords(tominutes('1999-01-01')-tominutes('2000-01-01'))=='Five hundred twenty-five thousand, six hundred minutes'
    assert mintowords(tominutes('2001-01-01')-tominutes('2003-01-01'))=='One million, fifty-one thousand, two hundred minutes'
    assert mintowords(tominutes('1995-01-01')-tominutes('2000-01-01'))=='Two million, six hundred twenty-nine thousand, four hundred forty minutes'
    assert mintowords(tominutes('2020-06-01')-tominutes('2032-01-01'))=='Six million, ninety-two thousand, six hundred forty minutes'
    assert mintowords(tominutes('1998-06-20')-tominutes('2000-01-01'))=='Eight hundred six thousand, four hundred minutes'

def test_invalid():
    with pytest.raises(SystemExit):
        tominutes('February 6th, 1998')


