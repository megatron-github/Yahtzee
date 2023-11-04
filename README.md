# Yahtzee

## Background

Yahtzee is a dice game involving five dice. After each roll of dice, the player can earn a score for various combinations of dice. The program will allow users to play the game of Yahtzee and display the dices and scores of each hand.

## Approach

When the program is executed, users will be asked to hit enter to roll the dice the first time. The dice will be shown, followed by a listing of scores that the current dice configuraiton would earn. Then, users may select the dices they would like to roll again by entering theirs values at the prompt. If user hits enter without specifying the die to roll in the next round, the game will end. The game will also end after the third roll. At the end of the game, a prompt will ask for input from users to play again. User may play again by entering "Y" or "y".

Two classes are created: Die (to set and return the Die's value after each roll) and YahtzeeHand (to create a Yathzee hand and display the dices and scores).

## Sample run
```
Entered Yahtzee!!!
First roll.  Press enter to roll the dice!
+---+---+---+---+---+
|* *|*  |*  |* *|* *|
|   |   | * |* *| * |
|* *|  *|  *|* *|* *|
+---+---+---+---+---+
 (4) (2) (3) (6) (5)
           aces: 0
           twos: 2
         threes: 3
          fours: 4
          fives: 5
          sixes: 6
three_of_a_kind: 0
 four_of_a_kind: 0
     full_house: 0
 small_straight: 0
 large_straight: 40
        yahtzee: 0
         chance: 20
Second roll.  Select dice values to roll: 2 3 4 5 6
+---+---+---+---+---+
|* *|* *|*  |* *|* *|
|* *| * | * | * |   |
|* *|* *|  *|* *|* *|
+---+---+---+---+---+
 (6) (5) (3) (5) (4)
           aces: 0
           twos: 0
         threes: 3
          fours: 4
          fives: 10
          sixes: 6
three_of_a_kind: 0
 four_of_a_kind: 0
     full_house: 0
 small_straight: 30
 large_straight: 0
        yahtzee: 0
         chance: 23
Third roll.  Select dice values to roll: 6 3 4
+---+---+---+---+---+
|   |* *|*  |* *|*  |
| * | * | * | * |   |
|   |* *|  *|* *|  *|
+---+---+---+---+---+
 (1) (5) (3) (5) (2)
           aces: 1
           twos: 2
         threes: 3
          fours: 0
          fives: 10
          sixes: 0
three_of_a_kind: 0
 four_of_a_kind: 0
     full_house: 0
 small_straight: 0
 large_straight: 0
        yahtzee: 0
         chance: 16
Do you want to play again (Y/n): n
Exited Yahtzee. Good bye!
```

## How to run

To run the program and play Yahtzee
```
python3 yahtzee.py
```

## Author

Truong Pham
