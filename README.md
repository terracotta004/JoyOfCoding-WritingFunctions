# JoyOfCoding-WritingFunctions
Learning Exercise: Writing Functions

1. Write a function, add, that takes two numbers as parameters and 
returns their sum. 

2. Write a function, multiply, that takes two numbers as parameters 
and returns their product. 

3. Now, test! Write python code that gets two numbers as input from 
the user and prints out their sum and product by calling the two 
functions above. Bonus points for putting this part in a main function.

Practice Problems: 
 
1. Write a function, pyramid, that takes a single character and a number as parameters and 
displays an ASCII art pyramid to the screen with number rows: 
 
|Example call|Displays|
|---|---|
|pyramid(“\*”, 2)|<pre><code>*<br>**</code></pre>
|pyramid(“+”, 5)|<pre><code>+<br>++<br>+++<br>++++<br>+++++</code></pre> 
|pyramid(“x”, 10)|<pre><code>x<br>xx<br>xxx<br>xxxx<br>xxxxx<br>xxxxxx<br>xxxxxxx<br>xxxxxxxx<br>xxxxxxxxx<br>xxxxxxxxxx</code></pre> 
 
2. Write a function, absolute_difference, that takes two numbers as parameters and 
returns their absolute difference: 
 
|Example call|Returns|
|---|---|
absolute_difference(5, 10)|5 
absolute_difference(10, 5)|5 
absolute_difference(200, -200)|400

4. Write a function is_even that takes a number as a parameter and 
returns whether or not it is even. Test that your function works by 
calling it twice, once with an even number and once with an odd 
number, and print the results. 

5. Write a function calculate_total that takes 3 parameters: 

a. `meal`: the cost of the meal 

b. `tax_rate`: the percent tax (e.g., NJ tax would be 0.07) 

c. `tip_rate`: the percent tip (e.g., a 20% tip rate is 0.20) 

Proper tipping technique dictates that the tip should be calculated 
based on the total cost of the meal, before tax is applied. Then, 
return the total. Test your function  works by using the following call:  

`calculate_total(53.48, .07, .18)` 

Note that the total for the above meal with tax & tip is $66.85.