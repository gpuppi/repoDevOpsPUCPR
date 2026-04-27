def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"
    
def test_random():
    assert "1010" == bin(10)[2:]
