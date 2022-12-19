from collections.abc import Iterable
from domino_stats.player import Player
from domino_stats.round import Round
import datetime
import math


class Game:
    def __init__(self, game_type=None, num_players=2):
        self._game_id = datetime.datetime.utcnow().toordinal()
        self._num_players = num_players
        self._accepted_game_types = {'Double 15': {'num_rounds': 16}}
        self._game_type = game_type
        self._rounds = []
        self._players = []
        self._average_score = 0
        self._current_round = 0
        self._final_ranking = []
        self._complete = False

        self.initialize_players()
        self.initialize_rounds()

    @property
    def accepted_game_types(self):
        return self._accepted_game_types

    @accepted_game_types.setter
    def accepted_game_types(self, value):
        if isinstance(value, Iterable):
            self._accepted_game_types = value
        else:
            raise TypeError('Accepted values needs to be iterable')

    @property
    def game_type(self):
        return self._game_type

    @game_type.setter
    def game_type(self, value):
        if value in self.accepted_game_types.keys():
            self.game_type = value

    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, value):
        if isinstance(value, list):
            self._rounds = value
        else:
            raise TypeError('Game.rounds needs to be of type list')

    @property
    def num_players(self):
        return self._num_players

    @num_players.setter
    def num_players(self, value):
        if isinstance(value, int):
            if value > 2:
                self._num_players = value
            else:
                ValueError('There must be at least 2 players')

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        if isinstance(value, list):
            self._players = value
        else:
            raise TypeError('Game.players needs to be of type list')

    @property
    def current_round(self):
        return self._current_round

    @current_round.setter
    def current_round(self, value):
        if isinstance(value, int):
            if value >= 0:
                if value <= len(self.rounds):
                    self.current_round = value
            else:
                raise ValueError('Game.current_round must be greater than zero and less than or equal to the total \
                number of rounds for the selected game type')

    def initialize_players(self):
        for i in range(self.num_players):
            current_player = Player(id=i, name=str(i + 1))
            self.players.append(current_player)

    def initialize_rounds(self):
        """
        Initialize the rounds of a new game.
        """
        if self.game_type:
            for i in range(self.accepted_game_types[self.game_type]['num_rounds']):
                self.rounds.append(Round(round_number=i, active_players=self.players))
        else:
            pass

    def play_round(self):
        """
        In the current round, each player takes a turn.
        When a turn is taken, a score is entered, and the player's round score is collected and updated.
        When all players have taken a turn, the turn is completed and the average score is
        updated so it can be easily used for adding new players. After the round is completed, game cumulative stats
        are updated.
        """
        round_scores = []
        cumulative_scores = []
        ranking_lookup_round = {}
        ranking_lookup_cumulative = {}
        ranked_round = []
        ranked_cumulative = []
        num_active_players = 0
        for player in self.players:
            if player._active:
                score_prompt = "Enter current score for player {} in round {}".format(player.name, self.current_round)
                round_score = int(input(score_prompt))
                self.rounds[self.current_round]._scores[player.name]['current_score'] = round_score
                round_cumulative = player._cumulative_score + round_score
                self.rounds[self.current_round]._scores[player.name]['cumulative_score'] = round_cumulative
                player._cumulative_score = round_cumulative
                cumulative_scores.append(round_cumulative)
                round_scores.append(round_score)
                ranking_lookup_round[round_score] = player.name
                ranking_lookup_cumulative[round_cumulative] = player.name
                num_active_players += 1

        # Finish out the round
        round_total = int(math.fsum(round_scores))
        self.rounds[self.current_round]._total_score = round_total
        self._average_score = int(int(math.fsum(cumulative_scores))/num_active_players)
        round_scores.sort(reverse=True)
        cumulative_scores.sort(reverse=True)
        # Rankings
        for x in round_scores:
            ranked_round.append({ranking_lookup_round[x]: x})
        for x in cumulative_scores:
            ranked_cumulative.append({ranking_lookup_cumulative[x]: x})

        self.rounds[self.current_round]._round_ranking = ranked_round
        self.rounds[self.current_round]._cumulative_ranking = ranked_cumulative

        # Finish out the round
        self.rounds[self.current_round].complete = True

        if self.current_round + 1 == len(self.rounds):
            next_round = self.current_round + 1
            self._current_round = next_round
        else:
            self._complete = True
            self._final_ranking = ranked_cumulative
            print(self._final_ranking)















