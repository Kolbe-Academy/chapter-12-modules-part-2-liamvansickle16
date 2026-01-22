# Instructions  

**For this week (March 18th-22nd) we will only be working on questions 1, 3. and 5-7. We will complete the others the following week.**

The material for this lesson is based on [Chapter 18: Recursion](https://learnpythontherightway.com/chapter/chapter-18.html).

For this lesson, you will be required to complete the  exercises below. 

Make sure to write your solutions in the `main.py` file.

1. Modify the Koch fractal program so that it draws a Koch snowflake, like this:

![Koch Snowflake](assets/koch_snowflake.png)




3. A Sierpinski triangle of order 0 is an equilateral triangle. An order 1 triangle can be drawn by drawing 3 smaller triangles (shown slightly disconnected here, just to help our understanding). Higher order 2 and 3 triangles are also shown. Draw Sierpinski triangles of any order input by the user.

![Sierpinski triangle](assets/sierpinski_triangle.png)



5. Write a function, `recursive_min`, that returns the smallest value in a nested number list. Assume there are no empty lists or sublists:
```python
test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
```

6. Write a function `count` that returns the number of occurrences of target in a nested list:
```python
test(count(2, []), 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
test(count("a", 
     [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
```

7. Write a function `flatten` that returns a simple list containing all the values in a nested list:
```python
test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
test(flatten([]) == [])
```

8. Rewrite the fibonacci algorithm without using recursion. Can you find bigger terms of the sequence? Can you find `fib(200)`?


9. Use help to find out what `sys.getrecursionlimit()` and `sys.setrecursionlimit(n)` do. Create several experiments similar to what was done in infinite_recursion.py to test your understanding of how these module functions work.


10. Write a program that walks a directory structure (as in the last section of this chapter), but instead of printing filenames, it returns a list of all the full paths of files in the directory or the subdirectories. (Don’t include directories in this list — just files.) For example, the output list might have elements like this:
```python
["C:\Python31\Lib\site-packages\pygame\docs\ref\mask.html",
 "C:\Python31\Lib\site-packages\pygame\docs\ref\midi.html",
 "C:\Python31\Lib\site-packages\pygame\examples\aliens.py",
 "C:\Python31\Lib\site-packages\pygame\examples\data\boom.wav", 
 ... ]   
```
