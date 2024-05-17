import pytest
from lab6 import *


def test_LinkedList_str():
    my_list = LinkedList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    assert my_list.__str__() == '3 1 4 2 '


def test_LinkedList_sorted():
    my_list = LinkedList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.sort_list()
    assert my_list.__str__() == '1 2 3 4 '