def reverse(string):
    return string[::-1]

def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack

import pytest

def test_pop_with_empty_stack():
    stack = []
    stack.pop()
