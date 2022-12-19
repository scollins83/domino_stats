from domino_stats.score import Score

class Round:
    def __init__(self, round_number, active_players):
        """

        Parameters
        ----------
        round_number
        active_players
            List of players in order
        """
        self._round_number = round_number
        self._total_score = 0
        self._active_players = active_players
        self._round_ranking = []
        self._cumulative_ranking = []
        self._scores = {}
        self._complete = False

        self.initialize_scores()

    def initialize_scores(self):
        """
        Initializes scores
        """
        for player in self._active_players:
            #self._scores[player.name] = Score(0, 0, 0)
            self._scores[player.name] = {'current_score': 0, 'cumulative_score': 0}

    def take_turn(self, player_name):
        """
        Parameters
        ----------
        player_name
            Lookup tag for a key in self._scores
        """
        self._scores[player_name]['current_score'] = input()

    def play(self):
        """
        Iterate through active players who take their turns to update their scores
        """
        for player in self._active_players:
            pass
            #self.get_round_score(player.name)
            #player._cumulative_score = self.









