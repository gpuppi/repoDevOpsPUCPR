def test_addition():
    """Test basic addition operation."""
    assert 1 + 1 == 2

def test_string():
    """Test string manipulation."""
    assert "hello".upper() == "HELLO"

def test_binary():
    """Test binary conversion."""
    assert "1010" == bin(10)[2:]

def test_int():
    """Test integer conversion."""
    assert int("1010", 2) == 10

def test_input(test_text: str = "hello"):
    """Test input handling."""
    assert test_text.upper() == "HELLO"
