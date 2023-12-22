import sys

sys.path.append('C:\\CodeChallenge\\Python\\PythonCodeChallenge\\PythonCodeChallenge')
import pytest
from CodeChallenges import NoMore5sEver


class TestNoMore5sEver:

    @pytest.mark.parametrize("input_numbers, expected_result", [
        (1, True),
        (0, True),
        (32, True),
        (243, True),
        (1024, True),
        (3125, True),
        (7776, True),
        (300, False),
        (12345, False),
        (9, False),
        (32768, True),
        (59049, True),
        (-1001, False),
        (100000, True),
        (-1, True),
        (-100000, True),
        (-7776, True),
        (59050, False)
    ])
    def test_is_perfect_fifth_power(self, input_numbers, expected_result):
        result = NoMore5sEver.is_perfect_fifth_power(input_numbers)
        assert result == expected_result
    @pytest.mark.parametrize("input_numbers, expected_result", [
        ([12, 45, 23, 175, 6, 42, 333], [12, 23, 6, 42, 333]),
        ([5, 15, 25, 35, 45], []),
        ([555, 5555, 55555], []),
        ([1, 2, 3, 4, 5], [ 2, 3, 4]),
        ([0], []),
        ([-59049, -1024, -32, -1], []),
        ([], []),
        ([100, 200, 300, 89, 178], [89, 178]),
        ([555555, 12345, 67890], []),
        ([9, 49, 81, 121], [9, 49, 81, 121]),
        ([55, 505, 5555, 55555], []),
        ([125, 135, 145, 155], []),
        ([-1001, -555, -11, 0, 7, 11, 1234, 5555, 10002], [-1001, -11, 7, 11, 1234]),
        ([-6, -5, -4, 0, 4, 5, 6], [-6, -4, 4, 6]),
        ([99993, 99995, 99996, 100002, 100003, 100005], [100002, 100003]),
        ([-100003, -100000, -99996, -99995, -99993], [-100003]),
        ([12341, 12342, 12343, 12344, 12345, 12346], []),
        ([3126, 7776, 16808, 32769, 59050], [3126])
    ])
    def test_filter_fives_out(self, input_numbers, expected_result):
        result = NoMore5sEver.filter_fives_out(input_numbers)
        assert result == expected_result

    @pytest.mark.parametrize("a, b, expected_result", [
        (1, 5, 3),
        (-42884, 83064, 11654),
        (-16042, 66356, 11654),
        (-25442, 13818, 11654),
        (-40149, 36707, 11654),
        (-2801, 70141, 7624)
    ])
    def test_no_5s(self, a, b, expected_result):
        rst = NoMore5sEver.no_5s(a, b)
        assert rst == expected_result


