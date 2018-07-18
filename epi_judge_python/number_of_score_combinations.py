from functools import lru_cache

from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    @lru_cache(maxsize=None)
    def _combs(final_score, plays):
        if final_score < 0:
            return 0
        if final_score == 0:
            return 1
        if not plays:
            return 0
        else:
            first_play = plays[0]
            possible_scores = range(0, final_score+1, first_play)
            return sum(_combs(final_score - score, plays[1:]) for score in possible_scores)

    return _combs(final_score, tuple(individual_play_scores))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
