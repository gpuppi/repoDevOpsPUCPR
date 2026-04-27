def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"
    
def test_random():
    assert int(1010, 2) == bin(10)[2:]
