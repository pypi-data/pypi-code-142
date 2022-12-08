import pytest
import src.autodiffpypi.base_derivatives as bd
from src.autodiffpypi.dual_number import DualNumber
from src.structures.graph import Node
import numpy as np


def test_base_derivatives():
    """
    Test suite for the base derivatives functions.
    Includes tests for the following functions:
    sin, cos, tan, sinh, cosh, tanh, arcsin, arccos,
    arctan, exp, square_root, pow, natural_log, log
    """
    def test_sin():
        # dual number
        x = DualNumber(np.pi, 1)
        result = bd.sin(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.sin(np.pi)
        assert result.dual == np.cos(np.pi)
        assert bd.sin(0.1) == np.sin(0.1)
        # node
        node = Node(np.pi)
        node_result = bd.sin(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.sin(np.pi)
        assert node_result.parent_gradients == [(node, np.cos(np.pi))]
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.sin("2")
    
    def test_cos():
        x = DualNumber(np.pi, 1)
        result = bd.cos(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.cos(np.pi)
        assert result.dual == -np.sin(np.pi)
        assert bd.cos(0.1) == np.cos(0.1)
        # node
        node = Node(np.pi)
        node_result = bd.cos(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.cos(np.pi)
        assert node_result.parent_gradients == [(node, -np.sin(np.pi))]
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.cos("4.5")
    
    def test_tan():
        x = DualNumber(np.pi, 1)
        result = bd.tan(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.tan(np.pi)
        assert result.dual == (1 / (np.cos(np.pi)) ** 2)
        assert bd.tan(0.1) == np.tan(0.1)
        # node
        node = Node(np.pi)
        node_result = bd.tan(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.tan(np.pi)
        assert node_result.parent_gradients == [(node, 1 / (np.cos(np.pi)) ** 2)]
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.tan("5.5")

    def test_arcsin():
        x = DualNumber(np.pi/4, 2)
        result = bd.arcsin(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.arcsin(np.pi/4)
        assert result.dual == (1 / np.sqrt(1 - (np.pi/4)**2)) * 2
        assert bd.arcsin(0.1) == np.arcsin(0.1)
        # node
        node = Node(np.pi/4)
        node_result = bd.arcsin(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.arcsin(np.pi/4)
        assert node_result.parent_gradients == [(node, 1 / np.sqrt(1 - (np.pi/4)**2))]
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.arcsin("5.5")
        with pytest.raises(ValueError):
            bd.arcsin(DualNumber(-5, 1))
        with pytest.raises(ValueError):
            bd.arcsin(Node(-5))            

    def test_arccos():
        x = DualNumber(np.pi / 4, 3)
        result = bd.arccos(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.arccos(np.pi / 4)
        assert result.dual == (-1 / np.sqrt(1 - (np.pi / 4)**2)) * 3
        assert bd.arccos(0.1) == np.arccos(0.1)
        # node
        node = Node(np.pi/4)
        node_result = bd.arccos(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.arccos(np.pi/4)
        assert node_result.parent_gradients == [(node, - 1 / np.sqrt(1 - (np.pi/4)**2))]
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.arccos("5.5")
        with pytest.raises(ValueError):
            bd.arccos(DualNumber(-5, 1))
        with pytest.raises(ValueError):
            bd.arccos(Node(-5))  

    def test_arctan():
        x = DualNumber(np.pi, 2)
        result = bd.arctan(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.arctan(np.pi)
        assert result.dual == (1 / (1 + np.pi**2)) * 2
        assert bd.arctan(0.1) == np.arctan(0.1)
        # node
        node = Node(np.pi)
        node_result = bd.arctan(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.arctan(np.pi)
        assert node_result.parent_gradients == [(node, 1 / (1 + (np.pi ** 2)))]
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.arctan("5.5")
    
    def test_exp():
        x = DualNumber(np.pi, 2)
        result = bd.exp(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.exp(np.pi)
        assert result.dual == np.exp(np.pi) * 2
        assert bd.exp(0.1) == np.exp(0.1)
        # node
        node = Node(np.pi)
        node_result = bd.exp(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.exp(np.pi)
        assert node_result.parent_gradients == [(node, np.exp(np.pi))]
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.exp("5.5")
    
    def test_sinh():
        x = DualNumber(np.pi, 5.5)
        result = bd.sinh(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.sinh(np.pi)
        assert result.dual == np.cosh(np.pi) * 5.5
        assert bd.sinh(0.1) == np.sinh(0.1)
        # node
        node = Node(np.pi)
        node_result = bd.sinh(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.sinh(np.pi)
        assert node_result.parent_gradients == [(node, np.cosh(np.pi))]        
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.sinh("5.5")
    
    def test_cosh():
        x = DualNumber(np.pi/2, 3.8)
        result = bd.cosh(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.cosh(np.pi/2)
        assert result.dual == np.sinh(np.pi/2) * 3.8
        assert bd.cosh(0.1) == np.cosh(0.1)
        # node
        node = Node(np.pi/2)
        node_result = bd.cosh(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.cosh(np.pi/2)
        assert node_result.parent_gradients == [(node, np.sinh(np.pi/2))] 
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.cosh("5.5")
    
    def test_tanh():
        x = DualNumber(np.pi, 2)
        result = bd.tanh(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.tanh(np.pi)
        assert result.dual == (1 - (np.tanh(np.pi))**2) * 2
        assert bd.tanh(0.1) == np.tanh(0.1)
        # node
        node = Node(np.pi)
        node_result = bd.tanh(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.tanh(np.pi)
        assert node_result.parent_gradients == [(node, 1 - (np.tanh(np.pi))**2)] 
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.tanh("5.5")
    
    def test_sqrt():
        x = DualNumber(np.pi/3, 2.6)
        result = bd.sqrt(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.sqrt(np.pi/3)
        assert result.dual == (1 / (2 * np.sqrt(np.pi/3))) * 2.6
        assert bd.sqrt(0.1) == np.sqrt(0.1)
        # node
        node = Node(np.pi/3)
        node_result = bd.sqrt(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.sqrt(np.pi/3)
        assert node_result.parent_gradients == [(node, 1 / (2 * np.sqrt(np.pi/3)))] 
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.sqrt("5.5")
    
    def test_pow():
        x = DualNumber(34, 6.7)
        result = bd.pow(x, 3)
        assert isinstance(result, DualNumber)
        assert result.real == 34 ** 3
        assert result.dual == (3 * (34**2)) * 6.7
        assert bd.pow(3, 2) == 9
        # node
        node = Node(34)
        node_result = bd.pow(node, 3)
        assert isinstance(node_result, Node)
        assert node_result.value == 34 ** 3
        assert node_result.parent_gradients == [(node, 3 * (34**2))] 
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.pow("5.5", 4)
        with pytest.raises(ValueError):
            bd.pow(x, 3.4)
        with pytest.raises(ValueError):
            bd.pow(node, 3.4)

    def test_log():
        x = DualNumber(np.pi, 2)
        result = bd.log(x)
        assert isinstance(result, DualNumber)
        assert result.real == np.log(np.pi) / np.log(np.e)
        assert result.dual == (1 / (x.real * np.log(np.e))) * 2
        result2 = bd.log(x, 3)
        assert isinstance(result2, DualNumber)
        assert result2.real == np.log(np.pi) / np.log(3)
        assert result2.dual == (1 / (np.pi * np.log(3))) * 2
        assert bd.log(0.1) == np.log(0.1) / np.log(np.e)
        # node
        node = Node(np.pi)
        node_result = bd.log(node)
        assert isinstance(node_result, Node)
        assert node_result.value == np.log(np.pi) / np.log(np.e)
        assert node_result.parent_gradients == [(node, 1 / (x.real * np.log(np.e)))] 
        node_result = bd.log(node, 3)
        assert isinstance(node_result, Node)
        assert node_result.value == np.log(np.pi) / np.log(3)
        assert node_result.parent_gradients == [(node, 1 / (np.pi * np.log(3)))] 
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.log("5.5")
        with pytest.raises(ValueError):
            bd.log(34, "5.5")
        with pytest.raises(ValueError):
            bd.log(34, -11)
    
    def test_sigmoid():
        x = DualNumber(np.pi, 2)
        result = bd.sigmoid(x)
        assert isinstance(result, DualNumber)
        assert result.real == 1 / (1 + np.exp(-np.pi))
        assert result.dual == (1 / (1 + np.exp(-np.pi))) * (1 - (1 / (1 + np.exp(-np.pi)))) * 2
        assert bd.sigmoid(0.1) == 1 / (1 + np.exp(-0.1))
        # node
        node = Node(np.pi)
        node_result = bd.sigmoid(node)
        assert isinstance(node_result, Node)
        assert node_result.value ==  1 / (1 + np.exp(-np.pi))
        assert node_result.parent_gradients == [(node, (1 / (1 + np.exp(-np.pi))) * (1 - (1 / (1 + np.exp(-np.pi)))))] 
        # assert that it fails when given non DualNumber input
        with pytest.raises(TypeError):
            bd.sigmoid("5.5")
    

    test_sin()
    test_cos()
    test_tan()
    test_arcsin()
    test_arccos()
    test_arctan()
    test_exp()
    test_sinh()
    test_cosh()
    test_tanh()
    test_sqrt()
    test_pow()
    test_log()
    test_sigmoid()

if __name__ == '__main__':
    test_base_derivatives()
    print("All tests passed!")
