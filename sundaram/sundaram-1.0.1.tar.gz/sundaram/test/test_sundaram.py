import pytest
from sundaram .calculate import calculate_sundaram

def test_calculate_sundaram():
    res = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    func_res = calculate_sundaram(25)
    assert res == func_res
    


if __name__ == "__main__":
   pytest.main()