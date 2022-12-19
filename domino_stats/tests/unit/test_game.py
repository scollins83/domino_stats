import unittest
from domino_stats.game import Game
from domino_stats.player import Player
from io import StringIO


class DominoStatsTest(unittest.TestCase):
    def test_create_blank_game(self):
        game = Game()
        self.assertIsNotNone(game)

    def test_create_double_15_game(self):
        num_players = 2
        game = Game(game_type="Double 15", num_players=num_players)
        self.assertEqual(len(game.rounds), 16)
        test_round = game.rounds[0]
        self.assertEqual(len(test_round._active_players), num_players)

def test_play_round(monkeypatch):
    num_players = 2
    game = Game(game_type="Double 15", num_players=num_players)
    # Enter 4 and 6
    score_inputs = StringIO('4\n6\n')
    monkeypatch.setattr('sys.stdin', score_inputs)
    game.play_round()
    assert game._average_score == 5


    #def test_instantiate_player(self):
    #    player = Player(name='')

    #def add_new_player(self):
    #    player_name = 'MandMs'
    #    game = Game(game_type="Double 15")
    #    game.add_new_player(player_name)
    #    self.assertIn(player_name, game.player_names)
    #    self.assertIn(player_name, game.rounds[0].scores.keys())

if __name__ == '__main__':
    unittest.main()
