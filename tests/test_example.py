def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"
    
def test_binary():
    assert "1010" == bin(10)[2:]

def test_int():
    assert int("1010", 2) == 10

def test_input(testText: str = "hello"):
    assert testText.upper() == "HELLO"