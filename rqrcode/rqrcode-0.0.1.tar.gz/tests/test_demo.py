import pytest

def test_demo():
    assert 1 == 1

class TestDemo:
    def test_demo(self):
        assert 1 == 1
    
if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_demo.py"])

