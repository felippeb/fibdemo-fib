from nose.tools import *
from fibgen import fibgen 

def test_non_natural_number():
    fibout = fibgen.gen(-1)
    assert 'error: num must be natural number' in fibout

def test_num_0_list():
    fibout = fibgen.gen(0)
    assert isinstance(fibout, list)

def test_num_0_val():
    fibout = fibgen.gen(0)
    assert 0 in fibout

def test_num_1_list():
    fibout = fibgen.gen(1)
    assert isinstance(fibout, list)

def test_num_1_val():
    fibout = fibgen.gen(1)
    assert 1 in fibout

def test_num_10_list():
    fibout = fibgen.gen(10)
    assert isinstance(fibout, list)

def test_nums_correct_to_25():
    fibout = fibgen.gen(25)
    fibseq = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]
    assert cmp(fibout, fibseq) == 0
