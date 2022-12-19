class Score:
    def __init__(self, current_round_score, previous_round_cumulative_score, cumulative_score):
        """
        Round scores for a player

        Parameters
        ----------
        current_round_score
        previous_round_cumulative_score
        cumulative_score
        """
        self._current_round_score = current_round_score
        self._previous_round_cumulative_score = previous_round_cumulative_score
        self._cumulative_score = cumulative_score

    def complete_turn(self, current_score, previous_round_cumulative_score):
        """
        Update statistics after current_round_score is entered
        """
        self._current_round_score = current_score
        self._previous_round_cumulative_score = previous_round_cumulative_score
        self._cumulative_score = self._previous_round_cumulative_score + self._current_round_score


