"""
 *****************************************************************************
   FILE:            yahtzee.py

   DESCRIPTION:     Crreate Yahtzee, a dice game that is played with five
                    dices. For each roll, the player add all the values
                    from the dice and add to chance. Each player can roll
                    three times to get the result that they desired. Special 
                    outcomes of each rolling are three-of-a-kind, 
                    four-of-a-kind, large straight (1-2-3-4-5 or 2-3-4-5-6),
                    small straight (1-2-3-4, 2-3-4-5, 3-4-5-6), and Yahtzee, 
                    or all five dices the same. Each player who roll out each
                    of the outcomes will be rewarded with very special points.

 *****************************************************************************
"""
import random

      #---------The code provided by Professor Alistair Campbell */-----------#
   
# Information for drawing dice:
PIPSTRINGS = [None, ["   ", " * ", "   "], ["*  ", "   ", "  *"],
              ["*  ", " * ", "  *"], ["* *", "   ", "* *"],
              ["* *", " * ", "* *"], ["* *", "* *", "* *"]]

HAND_TYPES = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes',
              'three_of_a_kind', 'four_of_a_kind', 'full_house',
              'small_straight', 'large_straight', 'yahtzee',
              'chance']

# Constants for controlling when to exit the program
END = 0       
CONTINUE = 1

# Constants describing rolls
ORDINALS = [None, "First", "Second", "Third"]

class Die:
    """ A class representing a multi-sided die """
      
    # Constructor:
    def __init__(self, num_sides=6):
        self._num_sides = num_sides
        self._value = 1
    
    def roll(self):
        """ Change to a new random value. """
      
        self._value = random.randint(1, self._num_sides)

    def get_value(self):
        """ Return the value of this die. """
         
        return self._value

    def set_value(self, value):
        """ Set the value of this die. """
      
        assert value in range(1, self._num_sides + 1)
        self._value = value

class YahtzeeHand:
    """ Represents a 5-dice hand of Yahtzee, supporting rolling 
        a selection of the dice, and calculating possible scores. """
      
    def __init__(self):
        self._dice = []
        for _ in range(5):
            self._dice.append(Die())

    def set_hand(self, values):
        """ Make this yahtzee hand have the given values. """
         
        assert len(values) == 5
        for val in values:
            assert val in range(1, 7)
        for i in range(5):
            self._dice[i].set_value(values[i])
    
    def roll(self, indices=range(5)):
        """ Roll dice given by the sequence of indices. """
      
        for i in indices:
            self._dice[i].roll()

    def _get_choice_indices(self, value_list):
        """ Decide whether value_list represents a selection of dice
            values from this hand. Return one if not. Otherwise, 
            return a list of indices. """
         
        # Build a list of index/value pairs for the dice:
        iv_pairs = [(i, self._dice[i].get_value()) for i in range(5)]
         
        choices = [] # the pairs that match values we want to roll.
        for value in value_list:
            
            # Find value in iv_pairs, if possible.
            items = [pair for pair in iv_pairs if pair[1] == value]
            if items == []:
                return None  # Can't find any!
               
            # Take the first match.
            item = items[0]
            
            # Add it to choices, remove it from iv_pairs.
            choices.append(item)
            iv_pairs.remove(item)
            
        # Return the indices.
        return [tuple[0] for tuple in choices]
            
    def user_input_roll(self, roll_num):
        """ Ask the user for the values of dice to roll until valid 
            selection is made.  Roll those dice. """
         
        while True:  # Loop exits from the middle
            response = input("{} roll.  Select dice values to roll: "
                             .format(ORDINALS[roll_num]))
            if response == "":
                return END
               
            # Get rid of delimiters, and make a list of values
            # from input.
            value_list = [int(x) for x in
                          "".join([ch if ch in '0123456789' else ' '
                                   for ch in response]).split()]
            
            # See whether it's valid.
            indices = self._get_choice_indices(value_list)
            if indices is not None:
               
                # ..Got a valid input! Roll them and be done!
                self.roll(indices)
                return CONTINUE
               
            # ..Not valid. Chastize and repeat.
            print("Invalid input.  Try again.")
                    
    def show(self):
        """ Show the values of the Yahtzee hand in a nice way. """
         
        print("+" + "---+" * 5)
        for row in range(3):
            print('|', end="")
            for i in range(5):
                print(PIPSTRINGS[self._dice[i].get_value()][row], end='|')
            print()
        print("+" + "---+" * 5)
        for i in range(5):
            print(" ({})".format(self._dice[i].get_value()), end="")
        print()

    def show_all_scores(self):
        """ Show all scores that could be entered for this 
            yahtzee hand. """
         
        for hand_type in HAND_TYPES:
            score = getattr(self, hand_type+"_score")()
            print("{:>15s}: {}".format(hand_type, score))
            
    def _get_values(self):
        """ Return a list of the dice values """
         
        return [self._dice[i].get_value() for i in range(5)]

    def _total_dice_with(self, value):
        """ Return a sum of dice that have the given value """
      
        return sum([x for x in self._get_values() if x == value])
    
    def aces_score(self):
        """ Return total for Aces. """
      
        return self._total_dice_with(1)

    def twos_score(self):
        """ Return total for Twos. """
         
        return self._total_dice_with(2)

    def threes_score(self):
        """ Return total for Threes. """
      
        return self._total_dice_with(3)

    def fours_score(self):
        """ Return total for Fours. """
         
        return self._total_dice_with(4)

    def fives_score(self):
        """ Return total for Fives. """
      
        return self._total_dice_with(5)

    def sixes_score(self):
        """ Return total for Sixes. """
         
        return self._total_dice_with(6)

    def chance_score(self):
        """ Return total of Dice. """
      
        return sum(self._get_values())
      
   #--------------------------------------------------------------------#

    def find_repeated_value(self, wanted_value):
        """ Return a list of repeated values from the dices. """ 
         
        # Make a list of values from the dices that are equal 
        # to the given value.
        rolled_values = self._get_values()
        repeated_values = []
        for value in rolled_values:
            if value == wanted_value:
                repeated_values.append(value)
        return repeated_values

    def check_straigth(self, straight):
        """ Check if the dices represented all the numbers in a given
            straight. """
      
        # Return True if all the numbers of given straight are 
        # represented by the dices. If not, return False.
        rolled_values = self._get_values()
        for num in straight:
            if num not in rolled_values:
                return False
        return True
    
    def three_of_a_kind_score(self):
        """ Return the sum of three dice with the same value, or zero """
      
        # Find all values that repeated three times or more in the rolling 
        # and find the sum the three repeated values.
        rolled_values = self._get_values()
        for value in rolled_values:
            repeated_values = self.find_repeated_value(value)

            # It is a three-of-a-kind when there are four dices 
            # with the same value.
            if len(repeated_values) >= 3:
                return repeated_values[0] * 3
        return 0

    def four_of_a_kind_score(self):
        """ Return the sum of four dice with the same value, or zero """
      
        # Find all values that repeated four times or more in the rolling 
        # and find the sum the four repeated values.
        rolled_values = self._get_values()
        for value in rolled_values:
            repeated_values = self.find_repeated_value(value)
            if len(repeated_values) >= 4:
                return repeated_values[0] * 4
        return 0

    def full_house_score(self):
        """ Return 25 if this is a full house. Or zero if not. """
        rolled_values = self._get_values()
        house = []
      
        # Check if the rolling produces three dices that have same 
        # value. If so, append the three values into the list house.
        for value in rolled_values:
            triple = self.find_repeated_value(value)
            if len(triple) == 3:
                house.append(triple)
                  
        # Check if the rolling produces two dices that have same 
        # value. If so, append the three values into the list house.
        for value in rolled_values:
            double = self.find_repeated_value(value)
            if len(double) == 2:
                house.append(double) 
                  
        # Check is house have a triple (three same values) and a
        # double (two same values, that are different from the triple)
        if len(house) == 5:
            return 25
        return 0

    def small_straight_score(self):
        """ Return 30 if this is a small straight. Or zero if not. """
      
        # Given senarios that a small straight would happen, check
        # if the rolling has an output that is the same with one of
        # the senarios. If so, then it is a small straight.
        straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        for straight in straights:
            small_straight = self.check_straigth(straight)
            if small_straight is True:
                return 30
        return 0

    def large_straight_score(self):
        """ Return 40 if this is a large straight. Or zero if not. """
      
        # Given senarios that a large straight would happen, check
        # if the rolling has an output that is the same with one of
        # the senarios. If so, then it is a large straight.
        straights = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        for straight in straights:
            large_straight = self.check_straigth(straight)
            if large_straight is True:
                return 40
        return 0

    def yahtzee_score(self):
        """ Return 50 if this is Yahtzee. Or zero if not. """

        # If one value from the dices is different from the rest, 
        # there is no Yahtzee.
        rolled_values = self._get_values()
        for value in rolled_values:
            if value != rolled_values[0]:
                return 0
        return 50

def main():
    """ The main program """
      
    yh = YahtzeeHand()
    _ = input("First roll.  Press enter to roll the dice!")
    yh.roll()
    yh.show()
    yh.show_all_scores()
    roll_num = 2
    while roll_num <= 3 and yh.user_input_roll(roll_num) == CONTINUE:
        yh.show()
        yh.show_all_scores()
        roll_num += 1

if __name__ == "__main__":
    main()
    
