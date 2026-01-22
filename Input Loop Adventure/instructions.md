# Project: Text-Based Adventure!
### Background
Before computers could handle graphics, a very popular game genre was the text-based adventure.  You might be able to google "Zork", a particularly famous one, and play it somewhere online.  Here's a snippet of the beginning of the game.  Each time you see a `>`, that's something that the user - the person playing the game - types in.

```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

>open mailbox
Opening the small mailbox reveals a leaflet.

>take leaflet
Taken.

>read leaflet
"WELCOME TO ZORK!

ZORK is a game of adventure, danger, and low cunning.  In it you will explore some of the most amazing territory ever seen by mortals.  No computer should be without one!"

>go east
The door is boarded and you can't remove the boards.

>go north
North of Hourse
You are facing the north side of a white house.  There is no door here, and all the windows are boarded up.  To the north a narrow path winds through the trees.

>go north
Forest Path
This is a path winding through a dimly lit forest.  The path heads north-south here.  One particularly large tree with some low branches stands at the edge of the path.

>quit

```

You can see how this works: you type commands; the computer understands them.  You keep typing commands until you beat the game, or until you type quit.

This means we'll need to upgrade our input loop!  It needs to be able to read multiple words, instead of just one number.

Go ahead and run the code in main.py and type a couple of commands (for example, try typing `go north`); they won't work yet, but you will see how Python can handle splitting a single string into several words.

What this code does is create a LIST of text strings.  That list will be as long as it needs to be to fit the number of words that the user typed.  The only weird thing is that Python, like most programming languages, starts numbering items starting at 0, not 1.  So:
- If the user typed a single word, say `hello`, then the length of in_list will be 1 and there will be a single word at index 0 which you can retrieve by writing `in_list[0]`.
- If the user typed `go north`, then `in_list[0]` will be `"go"` and `in_list[1]` will be `"north"`.
- Etc.

### Instructions

Your job is to create a text-based adventure using this input loop!  A few things:

- **Please review the handout in Schoology for official criteria**
- Your game should have the following:
  1.	**A help menu** -- When the user types “help” they should see a list of a few commands they can use to explore the room
  2.	**Two different rooms** --  The rooms can be simple, you do not need as many options as in Zork
        You should start in one room and “escape” into the second
  	    The second room should then be able to “escape” to win
  3.	**Handle incorrect input** -- If a user inputs a command that is not recognized you should display some sort message, e.g. “I don’t understand that command”
  4.	**Print user’s commands to a file** -- Write the user’s input in a new file and save that file when the user exits the game, either by winning or by quitting. 
- You probably want to restrict your user to only a few different possible commands; maybe "examine", "take", and "use".  So if the player's character wakes up in an empty room except for a button and a key, they could type "use button" or "take key" or "examine key", etc.
- **You should not write any more `while` or `input` commands**.  Let the input loop keep running; you just write code to handle it!
- There's an example of the first room of a game, and all the code to write it, that you can look at to get the idea.
