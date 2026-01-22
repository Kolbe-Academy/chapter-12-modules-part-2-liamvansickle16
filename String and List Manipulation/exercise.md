# Exercise: String and List Manipulation
Refer back to the demo to see examples of all the commands you'll need to use in order to figure out these questions.

Replace the blank function for each question with the code to accomplish what the question asks for.

**Level 1 – straightforward.**

If you’re stumped, you probably just need to look at the demo file again and find the right command!

1.	Return the character at index 2 in string s.  (Which I’ll remind you is not the second character.)
2.	Return the fifth character in string s.  (Which I’ll remind you is not the character at index 5.)
3.	Return the number of characters in the string.
4.	Return the first character.
5.	Return the last character.
6.	Return the penultimate character.  (Penultimate means “second to last”).
7.	Return the five character long substring starting at index 3.
8.	Return a substring consisting of the last five characters of the string.
9.	Return a substring starting at the character at index 3 and continuing to the end of the string.
10.	Return the original string in all lowercase.
11.	Return the original string in all uppercase.
12.	Convert the string to a list and return the list.  (For instance, `"CATS"` --> `["C", "A", "T", "S"]`.)
13.	Return the string shifted to the right by one (ie, the original string with the last character removed).
14.	Return the string shifted to the left by one (ie, the original string with the first character removed).

**Level 2 – kinda tricky.**

Some of these questions are pretty challenging!  It's ok if you need to ask for help!  You can absolutely do these with only the commands demonstrated in the demo file though; no need to Google.

15.	Return the number of times a lower case e appears in the string.
16.	Return the number of times a lower or upper case e appears in the string.
17.	Return the total number of times any lower or upper case vowel (do not include y) appears in the string.  Example: `"Every vowel counts"` --> `6`, because there are 6 total vowels in that string, including the capital E.
18.	Return a list containing every vowel from the original string, in the order they originally appeared.  (Hint: make a blank list, then use a for loop over each character in the string and use an if statement inside the for loop to decide when to append to the list.)  
Example: `"Every vowel counts"` --> `["E", "e", "o", "e", "o", "u"]`
19.	Make a new string that consists of every other character in the original string (ie, the characters at index 0, 2, 4, etc) and return that.
20.	Make a new string that consists of every other character in the original string starting with the character at index 1 (ie, the characters at index 1, 3, 5, etc) and return that.
21.	Return a list of every 2-character substring of the original string.  Example:  `"CATS"` --> `["CA", "AT", "TS"] `
22.	Return a string made by replacing every third character of the original string with an exclamation point, starting at index 0.
23.	Return a string made by replacing every third character of the original string with an exclamation point, starting at index 2.

**Example output.**

You can certainly use the built in tests, but if you want to see it all at once, here is what the complete output should look like if you use `s = "ExampleString"`.

Questions 17, 18, 22, and 23 are especially worth double-checking!

```
#1: a
#2: p
#3: 13
#4: E
#5: g
#6: n
#7: mpleS
#8: tring
#9: mpleString
#10: examplestring
#11: EXAMPLESTRING
#12: ['E', 'x', 'a', 'm', 'p', 'l', 'e', 'S', 't', 'r', 'i', 'n', 'g']
#13: ExampleStrin
#14: xampleString
#15: 1
#16: 2
#17: 4
#18: ['E', 'a', 'e', 'i']
#19: Eapetig
#20: xmlSrn
#21: ['Ex', 'xa', 'am', 'mp', 'pl', 'le', 'eS', 'St', 'tr', 'ri', 'in', 'ng']
#22: !xa!pl!St!in!
#23: Ex!mp!eS!ri!g
```
