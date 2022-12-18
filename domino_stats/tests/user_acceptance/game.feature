# Created by saracollins at 12/18/22
Feature: Start a new game
  As someone who wants to play a game of dominos, I want to start a new game

  @game
  Scenario: Create a new game
    Given domino-stats is installed
    When I call create_game with the type Double 15
    Then a game will be instantiated with 16 zero-indexed rounds
