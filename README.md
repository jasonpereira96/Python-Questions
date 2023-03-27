# Python Exercises for Royce

## Q1
Write a program to print this:
```
*
**
***
****
*****
```

## Q2
Write a program to print this:
```
1
12
123
1234
12345
```

## Q3
Create a program that asks the user to enter their name and their year of birth. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.


## Q4
### Odd Or Even
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. 

Extras:
If the number is a multiple of 4, print out a different message.


## Q5

Take a list, say for example this one:
```
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
and write a program that prints out all the elements of the list that are less than N, where N is a number you must take an input from the user. 
Required: Make a new list that contains all the numbers.


## Q6
Take two lists, say for example these two:
```
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.


## Q7
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no
divisors.)
Take this opportunity to practice using functions, described below.


## Q8
Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity to
think about how you can use functions. Make sure to ask the
user to enter the number of numbers in the sequence to
generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this: 1, 1,
2, 3, 5, 8, 13, …)

So if the user enters 5, your program should print: 1, 1, 2, 3, 5

## Q9 
Take a number N from the user and print the Nth term in fibonacci series using RECURSION


## Q10
Write a program (using functions!) that asks the user for
a long string containing multiple words. Print back to the
user the same string, except with the words in backwards
order. For example, say I type the string:
```
  My name is Michele
```
Then I would see the string:
```
  Michele is name My
```
shown back to me.


## Q11
Implement the following functions:

```python
def contains(alist, x):
	pass

def create_new_list(size):
	pass

def filter(alist, x):
	pass

def find_index(alist, x):
	pass

def double(alist):
	pass

def multiply(alist, x):
	pass

def double_and_multiply(alist, x):
	pass

```

Examples: 
```
double([1,2,3]) => [1,2,3,1,2,3]
multiply([1,2,3],2) => [2,4,6]
double_and_multiply([1,2,3], 2) => [2,4,6,2,4,6]
create_new_list(4) => [0,0,0,0]
filter([1,2,3,4,5,6], 4) => [1,2,3,4]
contains([1,2,3], 3) => True
contains([1,2,3], 0) => False
```

## Q12
Design a class `BankAccount`.
It should have the following fields:
- owner_name -> String
- balance -> int

It should have the following methods
- get_balance()
- get_owner()
- withdraw(amount) => amount should be subracted from balance
- deposit(amount) => amount should be added to balance

## Q12B
**Prerequsites: Understanding objects and classes and inheritance**
Design 2 classes `SavingsAccount` and `CheckingAccount`
They should both extend `BankAccount`

`SavingsAccount` should have an additional method `deposit_interest(rate)` 
where the `rate` will be something like 12.5
So if the current balance is 100 and the user calls `deposit_interest(12.5)`, the current balance is now 112.5.

`CheckingAccount` should internally maintain a list of credit card numbers.
These card numbers are stored as strings.
Initially, this list is empty.
The user can then call `add_credit_card(card_number)` on this class and the passed card number is added to the list.

There should also be another method `get_most_recent_card()` which will return the most recently added card.


## Q13
Download the file `numbers.csv` from the resources folder. Write a program that opens this file, reads the data and creates a new file called `result.csv` with 2 additional columns, `sum` and `product`. There columns should contain the sum and product of the cols A and B in each row.

## Q14
Consider the string 
```
The quick brown fox jumps over the lazy dog
```
Write a program that removes all the vowels from it and prints it out.

https://leetcode.com/problems/remove-vowels-from-a-string/

## Q15
Open the file `prices.csv`. 
Read the data and print the following stats:
- The max price and the date it reached that price
- The min price and the date it reached that price
- The median price and the date it reached that price
- The mean price
- The second highest price and the date it reached that price

## Q16
Write a program that prints a multiplication table for all numbers up to 12.

## Q17
Write a function that tests whether a string is a palindrome.

## Q18
Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

## Q19
Implement 3 functions:
- `factorialr(x)` Calculates the factorial of x recursively
- `factorial(x)`
- `nCr(n, r)`
- `nPr(n, r)`


## Q20
**Prerequsites: Understanding objects and classes**

Update the `BankAccount` class in Q12. Add a method `transfer(acc2, amount)` to `BankAccount`. Money should get transferred from this account to acc2 and the respective balances should get updated. Ensure that the transfer does not take place if this account does not have enough balance.
 `acc2` is an object of type `BankAccount`.

## Q21
Calculate the value of π using the Leibniz formula for π. Only expand upto the first 1000 terms. Print the final value of π.

https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

## Q22
Read all the data from `colors.csv`. Create a Python dictionary to store the mapping from a person's name to their favourite color.
Ask the user to enter the name of a person. If their name was present in the file, print out their favourite color. Otherwise, print out `I do not know this person`


## Q23
Consider the following 2 functions:
```python
def change_value(a):
	a = a + 1

def change_value2(alist):
	alist[0] = alist[0] + 1	


v1 = 4
v2 = [4]

change_value(v1)
change_value2(v2)

print(v1)
print(v2)
```

- Why does the value of `v1` not change after calling the function?
- Why does the value of `v2` change after calling the function?


## Q24
Select Python3 as the language and solve this. Press the Submit button to run it against all the test cases.
https://leetcode.com/problems/two-sum/



# Q25
Solve these:
- https://leetcode.com/problems/convert-the-temperature/
- https://leetcode.com/problems/defanging-an-ip-address/
- https://leetcode.com/problems/number-of-good-pairs/
- https://leetcode.com/problems/jewels-and-stones/ (Concepts covered: Python dicts)
- https://leetcode.com/problems/running-sum-of-1d-array/

# Q26
- https://leetcode.com/problems/decode-the-message/ (Concepts covered: Python dicts, ASCII (maybe))

Pray to God before starting this question