import sys

sys.path.append('C:\\CodeChallenge\\Python\\PythonCodeChallenge\\PythonCodeChallenge')
from CodeChallenges import WordsCounter
import pytest


@pytest.mark.parametrize("text, expected_result", [
    ("Hello world! Hello everyone.", {'hello': 2, 'world': 1, 'everyone': 1}),
    ("It's a test. That's a test.", {"it's": 1, "that's": 1, 'a': 2, 'test': 2}),
    ("Hey dude, you must take care! Hey brother, you must watch out! Hey, brother. There's an endless road to rediscover. Hey, sister. Know the water's sweet",
    {'hey': 4, 'dude': 1, 'you': 2, 'must': 2, 'take': 1, 'care': 1, 'brother': 2, 'watch': 1, 'out': 1, "there's": 1, 'an': 1, 'endless': 1, 'road': 1, 'to': 1, 'rediscover': 1, 'sister': 1, 'know': 1, 'the': 1, "water's": 1, 'sweet': 1}),
    ("kiy' kiy' kiy' coisas de kiy de coisas coisas são dif", {"kiy'": 3, "coiisas": 3, "de": 2})
])
def test_count_words(text, expected_result):
    assert WordsCounter.count_words(text) == expected_result


def test_count_words_with_apostrophes():
    text = "It's a test. That's a test."
    expected = {"it's": 1, "that's": 1, 'a': 2, 'test': 2}
    assert WordsCounter.count_words(text) == expected


def test_top3_ones_basic():
    text = "apple banana apple banana cherry apple"
    expected = ['apple', 'banana', 'cherry']
    assert WordsCounter.top3_ones(text) == expected


def test_top3_ones_with_fewer_words():
    text = "apple banana"
    expected = ['apple', 'banana']
    assert WordsCounter.top3_ones(text) == expected


@pytest.mark.parametrize("text, expected", [
    # Basic case
    ("apple banana apple banana cherry apple", ['apple', 'banana', 'cherry']),

    # Fewer words
    ("apple banana", ['apple', 'banana']),

    # Empty text
    ("", []),

    # Longer text with different frequencies
    ("one two two three three three four four four four", ['four', 'three', 'two']),

    # Text with punctuation and case insensitivity
    ("Hello! Is it me you're looking for? Hello, Lionel! It's me. No it's not.", ['hello', 'me', "it's"]),

    # Text with apostrophes and special characters
    ("It's a brave new world. That's the fact. Brave, brave, brave world! That's something.", ['brave', "world", "that's"]),

    # Text with equal frequencies
    ("Red blue green. Red fish, blue fish, green fish. Bla Bla Bla Bla!", ['bla', 'fish', 'red']),

    # Text with numbers and special characters (which should be ignored)
    ("123 456! 123, 789. Zero, one zero, two zeros.",  ['zero', 'one', 'two'])
])
def test_top3_ones(text, expected):
    assert WordsCounter.top3_ones(text) == expected
