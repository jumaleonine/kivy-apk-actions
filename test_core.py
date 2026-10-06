import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from core import Counter


def test_increment_and_decrement():
    c = Counter()
    assert c.increment() == 1
    assert c.increment(5) == 6
    assert c.decrement(2) == 4


def test_minimum_bound():
    c = Counter(minimum=0)
    assert c.decrement() == 0


def test_maximum_bound():
    c = Counter(start=9, maximum=10)
    assert c.increment(5) == 10


def test_reset():
    c = Counter(start=7)
    assert c.reset() == 0
