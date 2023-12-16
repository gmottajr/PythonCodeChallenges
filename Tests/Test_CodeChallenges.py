from CodeChallenges import remove_exclamation_mark
import pytest
import sys
print(sys.path)
sys.path.append('C:\\CodeChallenge\\Python\\PythonCodeChallenge\\PythonCodeChallenge')



class TestCodeChallengeShould:

    @pytest.mark.parametrize("value, expected_resul", [
        ("Hi!", "Hi"),
        ("Hi!!!", "Hi!!"),
        ("!Hi", "!Hi"),
        ("!Hi!", "!Hi"),
        ("Hi! Hi!", "Hi! Hi"),
        ("Hi", "Hi"),
    ])
    def test_remove_exclamation_mark(self, value, expected_result):
        rst = remove_exclamation_mark(value)
        assert rst == expected_result
