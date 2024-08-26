class Scorer:
    def __init__(self, dice_roll, choice):
        self.dice_roll = dice_roll
        self.choice = choice

    def score(self):
        match self.choice:
            case "chance":
                self._score_chance()
            case "yatzy":
                self._score_yatzy
            case "ones":
                self._score_target(1)
            case "twos":
                self._score_target(2)
            case "threes":
                self._score_target(3)
            case "fours":
                self._score_target(4)
            case "fives":
                self._score_target(5)
            case "sixes":
                self._score_target(6)
            case "pair":
                self._score_target_count(2)
            case "triple":
                self._score_target_count(3)
            case "quadruple":
                self._score_target_count(4)
            case "small straight":
                self._score_straight("small")
            case "big straight":
                self._score_straight("big")
            case "chance":
                self._score_chance()
            case "fullhouse":
                self._score_fullhouse()

    def _score_chance(self) -> int:
        return sum(self.dice_roll)

    def _score_yatzy(self) -> int:
        if len(set(self.dice_roll)) == 1:
            return 50
        else:
            return 0

    def _score_target(self, target: int) -> int:
        return sum([outcome for outcome in self.dice_roll if outcome == target])

    def _score_target_count(self, target_count: int) -> int:
        for target in range(6, 0, -1):
            if self.dice_roll.count(target) == target_count:
                return target * target_count
        return 0

    def _score_straight(self, kind: str) -> int:
        small_straight_set = {1, 2, 3, 4, 5}
        big_straight_set = {2, 3, 4, 5, 6}
        if (
            kind == "small"
            and set(self.dice_roll) & small_straight_set == small_straight_set
        ):
            return 15
        elif (
            kind == "big" and set(self.dice_roll) & big_straight_set == big_straight_set
        ):
            return 20
        else:
            return 0

    def _score_fullhouse(self) -> int:
        set_of_counts = {self.dice_roll.count(num) for num in self.dice_roll}
        if set_of_counts & {2, 3} == {2, 3}:
            return sum(self.dice_roll)
        else:
            return 0
