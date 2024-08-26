import pytest
from yatzy.scorer import Scorer


class TestScorer:
    @pytest.mark.parametrize(
        "input, expected_output", [([1, 2, 3, 4, 5], 15), ([1, 1, 1, 1, 1], 5)]
    )
    def test_score_chance(self, input, expected_output):
        scorer = Scorer(input, "chance")
        assert scorer._score_chance() == expected_output

    @pytest.mark.parametrize(
        "input, expected_output",
        [([1, 1, 1, 1, 1], 50), ([3, 3, 3, 3, 3], 50), ([1, 2, 3, 4, 5], 0)],
    )
    def test_yatzy(self, input, expected_output):
        scorer = Scorer(input, "yatzy")
        assert scorer._score_yatzy() == expected_output

    @pytest.mark.parametrize(
        "input, target, expected_output",
        [
            ([1, 1, 2, 4, 5], 1, 2),
            ([2, 2, 2, 3, 5], 2, 6),
            ([1, 2, 3, 4, 5], 3, 3),
            ([3, 3, 4, 5, 3], 2, 0),
        ],
    )
    def test_score_target(self, input, target, expected_output):
        scorer = Scorer(input, "target")
        assert scorer._score_target(target) == expected_output

    @pytest.mark.parametrize(
        "input, count_target, expected_output",
        [
            ([1, 1, 2, 3, 4], 2, 2),
            ([1, 1, 4, 4, 4], 3, 12),
            ([1, 2, 3, 4, 5], 4, 0),
            ([4, 4, 4, 4, 1], 4, 16),
            ([1, 1, 1, 1, 1], 3, 0),
            ([3, 3, 5, 5, 6], 2, 10),
        ],
    )
    def test_score_target_count(self, input, count_target, expected_output):
        scorer = Scorer(input, "target")
        assert scorer._score_target_count(count_target) == expected_output

    @pytest.mark.parametrize(
        "input, kind, expected_output",
        [
            ([1, 2, 3, 4, 5], "small", 15),
            ([4, 1, 2, 3, 5], "small", 15),
            ([1, 1, 2, 3, 4], "small", 0),
            ([2, 3, 4, 5, 6], "big", 20),
            ([5, 4, 3, 2, 1], "small", 15),
            ([1, 1, 1, 1, 1], "big", 0),
        ],
    )
    def test_score_straight(self, input, kind, expected_output):
        scorer = Scorer(input, kind)
        assert scorer._score_straight(kind) == expected_output

    @pytest.mark.parametrize(
        "input, expected_output",
        [
            ([1, 1, 3, 3, 3], 11),
            ([2, 2, 2, 5, 5], 16),
            ([1, 2, 3, 4, 5], 0),
            ([4, 4, 4, 4, 5], 0),
            ([5, 5, 5, 4, 4], 23),
            ([5, 5, 5, 2, 3], 0),
        ],
    )
    def test_fullhouse(self, input, expected_output):
        scorer = Scorer(input, "fullhouse")
        assert scorer._score_fullhouse() == expected_output
