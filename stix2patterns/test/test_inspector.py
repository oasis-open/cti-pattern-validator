import pytest

from stix2patterns.inspector import inspect_pattern


@pytest.mark.parametrize(u"pattern,expected_qualifiers", [
    (u"[foo:bar = 1]", set()),
    (u"[foo:bar = 1] repeats 5 times", {u"REPEATS 5 TIMES"}),
    (u"[foo:bar = 1] within 10.3 seconds", {u"WITHIN 10.3 SECONDS"}),
    (u"[foo:bar = 1] within 123 seconds", {u"WITHIN 123 SECONDS"}),
    (u"[foo:bar = 1] start '1932-11-12T15:42:15Z' stop '1964-10-53T21:12:26Z'",
        {u"START '1932-11-12T15:42:15Z' STOP '1964-10-53T21:12:26Z'"}),
    (u"[foo:bar = 1] repeats 1 times repeats 2 times",
        {u"REPEATS 1 TIMES", u"REPEATS 2 TIMES"}),
    (u"[foo:bar = 1] repeats 1 times and [foo:baz = 2] within 1.23 seconds",
        {u"REPEATS 1 TIMES", u"WITHIN 1.23 SECONDS"}),
    (u"([foo:bar = 1] start '1932-11-12T15:42:15Z' stop '1964-10-53T21:12:26Z' and [foo:abc < h'12ab']) within 22 seconds "
     u"or [frob:baz not in (1,2,3)] repeats 31 times",
        {u"START '1932-11-12T15:42:15Z' STOP '1964-10-53T21:12:26Z'",
         u"WITHIN 22 SECONDS", u"REPEATS 31 TIMES"})
])
def test_qualifiers(pattern, expected_qualifiers):
    pattern_data = inspect_pattern(pattern)

    assert pattern_data.qualifiers == expected_qualifiers


@pytest.mark.parametrize(u"pattern,expected_obs_ops", [
    (u"[foo:bar = 1]", set()),
    (u"[foo:bar = 1] and [foo:baz > 25.2]", {u"AND"}),
    (u"[foo:bar = 1] or [foo:baz != 'hello']", {u"OR"}),
    (u"[foo:bar = 1] followedby [foo:baz in (1,2,3)]", {u"FOLLOWEDBY"}),
    (u"[foo:bar = 1] and [foo:baz = 22] or [foo:abc = '123']", {u"AND", u"OR"}),
    (u"[foo:bar = 1] or ([foo:baz = false] followedby [frob:abc like '123']) within 46.1 seconds",
        {u"OR", u"FOLLOWEDBY"})
])
def test_observation_opts(pattern, expected_obs_ops):
    pattern_data = inspect_pattern(pattern)

    assert pattern_data.observation_ops == expected_obs_ops


@pytest.mark.parametrize(u"pattern,expected_comparisons", [
    (u"[foo:bar = 1]", {u"foo": [(u"bar", u"=", u"1")]}),
    (u"[foo:bar=1 and foo:baz=2]", {u"foo": [(u"bar",u"=",u"1"),(u"baz",u"=",u"2")]}),
    (u"[foo:bar=1 or bar:foo<12.3]", {
        u"foo": [(u"bar", u"=", u"1")],
        u"bar": [(u"foo", u"<", u"12.3")]
    }),
    (u"[foo:bar=1] or [foo:baz matches '123\\\\d+']", {
        u"foo": [(u"bar", u"=", u"1"), (u"baz", u"MATCHES", u"'123\\\\d+'")]
    }),
    (u"[foo:bar=1 and bar:foo>33] repeats 12 times or "
     u"  ([baz:bar issubset '1234'] followedby [baz:quux not like 'a_cd'])", {
        u"foo": [(u"bar", u"=", u"1")],
        u"bar": [(u"foo", u">", u"33")],
        u"baz": [(u"bar", u"ISSUBSET", u"'1234'"), (u"quux", u"NOT LIKE", u"'a_cd'")]
    })
])
def test_comparisons(pattern, expected_comparisons):
    pattern_data = inspect_pattern(pattern)

    assert pattern_data.comparisons == expected_comparisons
