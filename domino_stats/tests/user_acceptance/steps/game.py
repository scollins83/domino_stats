from behave import *

from domino_stats.game import Game
from domino_stats.player import Player

use_step_matcher("re")

@given("domino_stats is installed")
def package_exists(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    try:
        import domino_stats
    except ImportError:
        print("Package domino_stats not installed")


@when("I call create_game with the type Double 15 with 2 players")
def create_game_with_type(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    game_type = "Double 15"
    number_of_players = 2
    context.game = Game(game_type=game_type, num_players=2)

@then("a game will be instantiated with 16 zero-indexed rounds with structures for each player")
def verify_correct_rounds(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    assert len(context.game.rounds) == 16, "Game of type Double 15 does not contain 16 rounds"
    # Write something to check the rounds have all the names
@when("I call add_new_player with user MandMs")
def add_player(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    player_name = 'MandMs'
    context.game.add_new_player('MandMs')
@then("MandMs will be added to the list of players, and a score will be added for MandMs to each existing round")
def check_player_added(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    assert 'MandMs' in context.game.player_names
    assert 'MandMs' in list(context.game.rounds[0].scores.keys())


@given("a game has been instantiated with 2 players")
def two_player_basic_game(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    game_type = "Double 15"
    number_of_players = 2
    context.game = Game(game_type=game_type, num_players=number_of_players)


@when("I call play_round")
def play_a_round(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    context.game.play_round()
    context.starting_round = context.game.current_round

@then("one round will be played and all scores will be updated")
def round_scores_updated(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    assert context.game._average_score > 0
