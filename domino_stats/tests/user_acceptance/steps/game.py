from behave import *

import domino_stats

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


@when("I call create_game with the type Double 15")
def create_game_with_type(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    game_type = "Double 15"
    context.game = domino_stats.game.Game(type=game_type)


@then("a game will be instantiated with 16 zero-indexed rounds")
def verify_correct_rounds(context):
    """
    Parameters
    ----------
    context : behave.runner.Context
    """
    assert len(context.game.rounds) == 16, "Game of type Double 15 does not contain 16 rounds"
