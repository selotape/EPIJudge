import functools
from collections import namedtuple

from test_framework import generic_test

Score = namedtuple('Score', 'first,second')


def maximum_revenue(coins):
    @functools.lru_cache(maxsize=None)
    def max_rev(_from, _to):

        if _from > _to:
            return Score(first=0, second=0)

        left_coin = coins[_from]
        future_game = max_rev(_from + 1, _to)
        my_score_if_choose_left = left_coin + future_game.second
        opponent_score_if_choose_left = future_game.first

        right_coin = coins[_to]
        future_game = max_rev(_from, _to - 1)
        my_score_if_choose_right = right_coin + future_game.second
        opponent_score_if_choose_right = future_game.first

        if my_score_if_choose_left > my_score_if_choose_right:
            return Score(my_score_if_choose_left, opponent_score_if_choose_left)
        else:
            return Score(my_score_if_choose_right, opponent_score_if_choose_right)

    return max_rev(0, len(coins) - 1)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
