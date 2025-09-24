# tests/test_tools.py

from tools.arthamatic_op_tool import multiply, add

def test_add():
    assert add.invoke({'a': 2, 'b': 3}) == 5
    assert add.invoke({'a': -1, 'b': 1}) == 0
    assert add.invoke({'a': 0, 'b': 0}) == 0

def test_multiply():
    assert multiply.invoke({'a': 2, 'b': 3}) == 6
    assert multiply.invoke({'a': -1, 'b': 5}) == -5
    assert multiply.invoke({'a': 0, 'b': 100}) == 0


