# Created by saracollins at 12/18/22
Feature: Play a Double 15 game of Dominoes
  As someone who wants to play a game of dominos, I want to start a new game with players and play it through

  @game
  Scenario: Create a new game
    Given domino_stats is installed
    When I call create_game with the type Double 15 with 2 players
    Then a game will be instantiated with 16 zero-indexed rounds with structures for each player

  @game
  Scenario: Play a round
    Given a game has been instantiated with 2 players
    When I call play_round
    Then one round will be played and all scores will be updated

  #@game
  #Scenario: Add new players to a game
  #  Given a type Double 15 game is created
  #  When I call add_new_player with user MandMs
  #  Then MandMs will be added to the list of players, and a score will be added for MandMs to each existing round
