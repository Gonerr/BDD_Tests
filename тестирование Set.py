from paspailleur.pattern_structures.set_ps import SuperSetPS, SubSetPS
from bitarray import frozenbitarray as fbarray
import nltk


def test_intersect_patterns():
    sps = SuperSetPS()
    print (sps.join_patterns({'a', 'b'}, {'c', 'b'}) == {'a', 'b', 'c'})
    print (sps.join_patterns(set(), {'a'}) == {'a'})

    sps = SubSetPS()
    print (sps.join_patterns({'a', 'b'}, {'c', 'd'}) == set())
    print (sps.join_patterns({'a', 'b'}, {'a', 'd'}) == {'a'})
    print (sps.join_patterns(set(), {'a'}) == set())

    print (sps.join_patterns(sps.max_pattern, {'a'}) == {'a'})
    print (sps.join_patterns({'a'}, sps.max_pattern) == {'a'})


def test_bin_attributes():
    data = [{'a'}, {'b'}, {'a', 'c'}]
    patterns_true = ({'a', 'b', 'c'}, {'a', 'b'}, {'a', 'c'}, {'b', 'c'}, {'a'}, {'b'}, {'c'}, set())
    flags_true = (
        '111',  # {'a', 'b', 'c'},
        '110',  # {'a', 'b'},
        '101',  # {'a', 'c'},
        '010',  # {'b', 'c'},
        '100',  # {'a'},
        '010',  # {'b'},
        '000',  # {'c'},
        '000',  # set(),
    )
    flags_true = tuple([fbarray(flag) for flag in flags_true])

    sps = SuperSetPS()
    patterns, flags = list(zip(*list(sps.iter_bin_attributes(data))))
    assert patterns == patterns_true
    assert flags == flags_true

    patterns, flags = list(zip(*list(sps.iter_bin_attributes(data, min_support=0.5))))
    print (set(flags) == {flg for flg in flags_true if flg.count() >= 2})

    patterns, flags = list(zip(*list(sps.iter_bin_attributes(data, min_support=2))))
    print (set(flags) == {flg for flg in flags_true if flg.count() >= 2})

    # SubsetPS
    patterns_true = (set(), {'a'}, {'b'}, {'c'}, {'a', 'b', 'c'})
    flags_true = (
        '111',  # set(),
        '101',  # {'a'}
        '010',  # {'b'}
        '001',  # {'c'}
        '000',  # {'a','b','c'}
    )
    flags_true = tuple([fbarray(flag) for flag in flags_true])

    sps = SubSetPS()
    patterns, flags = list(zip(*list(sps.iter_bin_attributes(data))))
    assert patterns == patterns_true
    assert flags == flags_true

    patterns, flags = list(zip(*list(sps.iter_bin_attributes(data, min_support=0.5))))
    print (set(flags) == {flg for flg in flags_true if flg.count() >= 2})
    print (set(flags))
    print({flg for flg in flags_true if flg.count() >= 2})

    patterns, flags = list(zip(*list(sps.iter_bin_attributes(data, min_support=2))))
    print (set(flags) == {flg for flg in flags_true if flg.count() >= 2})

def test_is_subpattern():
    sps = SuperSetPS()

    print (sps.is_less_precise({'a', 'b', 'c'}, {'a'}))
    print (not sps.is_less_precise({'a'}, {'c'}))

    sps = SubSetPS()
    print (sps.is_less_precise({'a'}, {'a', 'b', 'c'}))
    print (not sps.is_less_precise({'a'}, {'c'}))


def test_n_bin_attributes():
    data = [{'a'}, {'b'}, {'a', 'c'}]

    sps = SuperSetPS()
    print (sps.n_bin_attributes(data) == 8)

    sps = SubSetPS()
    print (sps.n_bin_attributes(data) == 7)


def test_intent():
    data = [{'a'}, {'b'}, {'a', 'c'}]

    sps = SuperSetPS()
    assert sps.intent(data) == {'a', 'b', 'c'}

    sps = SubSetPS()
    assert sps.intent(data) == set()


def test_extent():
    data = [{'a'}, {'b'}, {'a', 'c'}]

    sps = SuperSetPS()
    print(list(sps.extent(data, {'a', 'c'})) == [0, 2])

    sps = SubSetPS()
    print(list(sps.extent(data, {'a'})) == [0, 2])


def test_preprocess_data():
    data = [{'a'},  1, [3, 'x']]

    sps = SuperSetPS()
    assert list(sps.preprocess_data(data)) == [frozenset({'a'}), frozenset({1}), frozenset({3, 'x'})]

    sps = SubSetPS()
    assert list(sps.preprocess_data(data)) == [frozenset({'a'}), frozenset({1}), frozenset({3, 'x'})]


def test_verbalize():
    sps = SubSetPS()
    assert sps.verbalize({'a', 'b', 'c'}) == 'a, b, c'
    assert sps.verbalize({'a', 'bcde', 'f'}, add_curly_braces=True) == '{a, bcde, f}'
    assert sps.verbalize(set()) == '∅'
    assert sps.verbalize(set(), add_curly_braces=True) == '{}'

    sps = SuperSetPS()
    assert sps.verbalize({'a', 'b', 'c'}) == 'a, b, c'
    assert sps.verbalize({'a', 'bcde', 'f'}, add_curly_braces=True) == '{a, bcde, f}'
    assert sps.verbalize(set()) == '∅'
    assert sps.verbalize(set(), add_curly_braces=True) == '{}'

# test_intersect_patterns()
# test_bin_attributes()
# test_is_subpattern()
test_n_bin_attributes()