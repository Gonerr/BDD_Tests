from paspailleur.pattern_structures import CartesianPS, IntervalPS, SuperSetPS, SubSetPS, NgramPS
from bitarray import frozenbitarray as fbarray
import math

def test_intersect_patterns():
    a = ((1, 2), (3, 5))
    b = ((0, 2), (3, 5))
    cps = CartesianPS(basic_structures=[IntervalPS(), IntervalPS()])
    assert cps.join_patterns(a, b) == b
    assert cps.join_patterns(b, a) == b

    assert cps.join_patterns(cps.max_pattern, a) == a
    assert cps.join_patterns(a, cps.max_pattern) == a

def test_preprocess_data():
    data = [
        [(0, 1), 'x', 'hello world'],
        [(0, 3), 'y', 'hello']
    ]

    cps = CartesianPS(basic_structures=[IntervalPS(), SuperSetPS(), NgramPS()])
    assert list(cps.preprocess_data(data)) == [
        ((0., 1.), frozenset({'x'}), frozenset({('hello', 'world')})),
        ((0., 3.), frozenset({'y'}), frozenset({('hello',)}))
    ]

def test_binarize():
    data = [
        ((0, 1), (10, 20)),
        ((1, 2), (10, 20))
    ]
    patterns_true = [
        (0, (0, 2)), (0, (1, 2)), (0, (0, 1)), (0, (math.inf, -math.inf)),
        (1, (10, 20)), (1, (math.inf, -math.inf)),
    ]
    itemsets_true = [
        '101010',
        '110010',
    ]
    itemsets_true = [fbarray(itemset) for itemset in itemsets_true]

    cps = CartesianPS(basic_structures=[IntervalPS(), IntervalPS()])
    patterns, itemsets = cps.binarize(data)
    assert patterns == patterns_true
    assert itemsets == itemsets_true