# Instructions

The material for this lesson is based on [Chapter 15:  Classes and Objects --- the Basics](https://learnpythontherightway.com/chapter/chapter-15.html).

For this lesson, you will be required to complete the  exercises below. 

Make sure to write your solutions in the `main.py` file.


2.  Add a method `reflect_x` to `Point` which returns a new `Point`, one which is the reflection of the point 
    about the x-axis. For example, `Point(3, 5).reflect_x()` is (3, -5)

3.  Add a method `slope_from_origin` which returns the slope of the line joining the origin to the point. For 
    example:

```python
>>> Point(4, 10).slope_from_origin()
2.5 
```    

What cases will cause this method to fail?

4.  The equation of a straight line is "y = ax + b", (or perhaps "y = mx + c"). The coefficients a and b completely describe the line. Write a method in the `Point` class so that if a point instance is given another point, it will compute the equation of the straight ine joining the two points. It must return the two coefficients as a tuple of two values. For example, :

```python
>>> print(Point(4, 11).get_line_to(Point(6, 15))) 
>>> (2, 3)
```

This tells us that the equation of the line joining the two points is "y = 2x + 3". When will this method fail?

  
  
