# Instructions  
The material for this lesson are based on [Chapter 7: Iteration](https://learnpythontherightway.com/chapter/chapter-7.html).

For this lesson, you will be required to complete the  exercises below. 

Make sure to write your solutions in the `main.py` file.

This chapter showed us how to sum a list of items, and how to count items. The counting example also had an `if` statement that let us only count some selected items. In the previous chapter we also showed a function `find_first_2_letter_word` that allowed us an “early exit” from inside a loop by using `return` when some condition occurred. We now also have `break` to exit a loop but not the enclosing function, and `continue` to abandon the current iteration of the loop without ending the loop.

Composition of list traversal, summing, counting, testing conditions and early exit is a rich collection of building blocks that can be combined in powerful ways to create many functions that are all slightly different.


4. Count how many words in a list have length 5.


5. Sum all the elements in a list up to but not including the first even number. (Write your unit tests. What if there is no even number?)


6. Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)


  10.. Write a function, is_prime, which takes a single integer argument and returns True when the argument is a prime number and False otherwise. Add tests for cases like this:

    ```python
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    ```

The last case could represent your birth date. Were you born on a prime day? In a class of 100 students, how many do you think would have prime birth dates?

12. Many interesting shapes can be drawn by the turtle by giving a list of pairs, where the first item of the pair is the angle to turn, and the second item is the distance to move forward. Set up a list of pairs so that the turtle draws a house with a cross through the centre, as show here. This should be done without going over any of the lines / edges more than once, and without lifting your pen.

![House](assets/house.png)

13. Not all shapes like the one above can be drawn without lifting your pen, or going over an edge more than once. Which of these can be drawn?

![Houses](assets/houses.png)

Now read Wikipedia’s article (http://en.wikipedia.org/wiki/Eulerian_path) about Eulerian paths. Learn how to tell immediately by inspection whether it is possible to find a solution or not. If the path is possible, you’ll also know where to put your pen to start drawing, and where you should end up!

17. You and your friend are in a team to write a two-player game, human against computer, such as Tic-Tac-Toe / Noughts and Crosses. Your friend will write the logic to play one round of the game, while you will write the logic to allow many rounds of play, keep score, decide who plays, first, etc. The two of you negotiate on how the two parts of the program will fit together, and you come up with this simple scaffolding (which your friend will improve later):

    ```python
    # Your friend will complete this function
    def play_once(human_plays_first):
        """
        Must play one round of the game. If the parameter
        is True, the human gets to play first, else the
        computer gets to play first.  When the round ends,
        the return value of the function is one of
        -1 (human wins),  0 (game drawn),   1 (computer wins).
        """
        # This is all dummy scaffolding code right at the moment...
        import random                  # See Modules chapter ...
        rng = random.Random()
        # Pick a random result between -1 and 1.
        result = rng.randrange(-1,2)
        print("Human plays first={0},  winner={1} "
                        .format(human_plays_first, result))
        return result
    ```

  a. Write the main program which repeatedly calls this function to play the game, and after each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”. It then asks the player “Do you want to play again?” and either plays again, or says “Goodbye”, and terminates.

  b. Keep score of how many wins each player has had, and how many draws there have been. After each round of play, also announce the scores.

  c. Add logic so that the players take turns to play first.

  d. Compute the percentage of wins for the human, out of all games played. Also announce this at the end of each round.

  e. Draw a flowchart of your logic.
