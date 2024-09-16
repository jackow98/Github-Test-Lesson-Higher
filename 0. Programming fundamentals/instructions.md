# Key Concepts and Data Types

Python is a versatile and widely-used programming language, known for its readability and straightforward syntax. In programming with Python, it's crucial to understand the various data types, as they define the kind of value you're working with and determine what operations you can perform on them.

## Common Data Types
- **String**: A data type for a sequence of characters, enclosed in single or double-quotes. For instance, "Hello, World!".
- **Integer**: This type represents whole numbers, without a decimal point, like 3 or 100.
- **Float**: A floating-point number, which includes a decimal, like 3.14 or 2.0.
- **Boolean**: This type has two possible values: True or False. It's often used in conditions and loops.

## What Are Data Types?

Data types are classifications that specify the type of data a variable can hold, such as text, numbers, and true/false values. They are essential because they:
- Allow the translator (like a compiler or interpreter) to allocate the appropriate amount of memory for storing a variable's data.
- Restrict the range of operations that can be performed on the data.
- Ensure that data is stored efficiently and appropriately in the main memory.

## Common Data Types (Detailed)

1. **String**: Used to store text or a sequence of characters. For example, a name, phone number, or any item of text enclosed in quotation marks:
   ```python
   name = "Mr Walker"
   phone = "07723231222"
   username = "mrw98!"
   question = "What’s a string?"
   ```
   
2. **Character**: Stores a single character. It's often used for simple data like 'M' or 'F' for male or female. Characters are stored as ASCII codes or Unicode for a larger character set:
   ```python
   myChar = "a"
   ```
   
3. **Integer**: For storing whole numbers, both positive and negative, including zero. They are stored using two's complement:
   ```python
   height = 190
   temperature = -2
   bankBalance = 0
   ```
   
4. **Real**: Represents positive and negative decimal or fractional numbers. Stored using floating point notation, which includes an exponent and a mantissa:
   ```python
   averageHeight = 30.2
   height = 1.82
   score = -10.3
   ```
   
5. **Boolean**: This type stores only two values: True or False. Used in conditions and binary settings, it's stored as a single bit that is either on or off:
   ```python
   inputIsValid = False
   freeTrial = True
   ```

## Using the `input()` Function

When you want to get information from the user, you use the `input()` function. This function pauses the program and waits for the user to type something. Once they press Enter, the `input` function returns what was typed as a string. For example:

```python
name = input("What is your name? ")
print("Hello, " + name)
```

Notice the `+` sign used for concatenation, which is a way to combine strings. However, you cannot directly concatenate strings with other data types like integers. First, you need to cast the integer to a string using the `str()` function.

## Using Comments in Python

A comment in Python is a line of text in your code that is not executed by the interpreter. Comments are mainly used for explaining code, making it more readable and understandable to humans. They are extremely useful for providing context or explaining the purpose of complex sections of code, and they can also be used to temporarily disable code that should not be executed during debugging.

### Single-Line Comments

You start a single-line comment with the hash symbol (`#`). Everything following the `#` on that line is part of the comment and will not be executed.

```python
# This is a single-line comment in Python
print("Hello, World!")  # This is a comment after code
```

Comments are especially useful when the code is complex and might not be immediately obvious to someone who is reading it for the first time. It's a good practice to comment your code to explain **why** you did something, rather than **what** you did, as the latter should be clear from the code itself.

## Fixed Loops in Python (For Loop)

One of the fundamental structures in Python is the fixed loop, often referred to as a **for loop**. This loop repeats a block of code a fixed number of times, which is handy for tasks like printing a message multiple times. The for loop uses an iteration variable that changes each time through the loop.

### Example: Printing Your Name Multiple Times

```python
# This for loop will print your name 10 times.
for i in range(10):
    print("Your Name")
```

In the above example, `range(10)` tells Python to repeat the loop 10 times, with `i` (the counter) taking on values from 0 to 9 during each iteration.

## Working with Numbers and Strings

Let's look at an example that combines several of these concepts—data types, input, and loops—to create a program that interacts with the user and performs calculations.

### Example: Times Table Program

Here, we use `int(input())` to convert the user input into an integer. The for loop then iterates 12 times, printing the multiplication table for the given number.

```python
# Ask for a number from the user
number = int(input("Enter a number for the times table: "))

# Calculate and print the times table for the entered number up to 12
for i in range(1, 13):
    # Concatenation of strings and type casting of integer to string
    print(str(number) + " x " + str(i) + " = " + str(number * i))
```

## Calculating a Running Total

A common pattern in programming is calculating a running total during a loop. This means you start with a total of 0 and then add to it with each iteration of the loop.

### Example: Calculating Total Age

In this example, `+=` is used to update the `total_age` each time a new age is entered.

```python
total_age = 0
for i in range(10):
    age = int(input(f"Enter the age of person {i+1}: "))
    total_age += age  # Adds the age to the running total
print("The total age is: " + str(total_age))
```

---

# Task List

1. Write a Python program to print your name 10 times.
2. Write a Python program to:
   1. Ask for your name.
   2. Print your name 1000 times.
3. Warm up task #3: Write a Python program to:
   1. Ask for your name.
   2. Print "Hello" then your name 1000 times.
4. Write a Python program to print the answers to the 8 times table from 1 to 12.
5. Write a Python program to print the answers to the 8 times table from 1 to 1000.
6. Write a Python program to:
   1. Calculate the 7 times table up to 12.
   2. Print "7 x number = answer" each time.
7. Write a Python program to ask the user to input the age of 10 people and print each age.
8. Write a Python program to:
   1. Ask the user to input the age of 10 people.
   2. Print the age of each person in 10 years' time.
9. Write a Python program to:
   1. Ask the user to input the age of 10 people.
   2. Add up all the ages.
   3. Print the total ages.
10. Write a Python program to output the 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12 times tables from 1 to 12.
11. **Extension Task 1**: Come up with another use case for a fixed loop and write a program.

---

# Introduction to Conditional Loops

In Python programming, a **conditional loop** is a fundamental concept that allows a program to execute a block of code repeatedly as long as a specified condition is true. These loops are essential for tasks that require repetition, and they are particularly useful when you're unsure how many times a task needs to be repeated. The most common type of conditional loop in Python is the **while loop**.

## Understanding the `while` Loop

The `while` loop in Python repeatedly executes a target statement as long as a given condition is true. Here’s the basic structure of a `while` loop:

```python
while condition:
    # code to execute
```

- **Condition**: This is a boolean expression that determines whether the loop continues to execute. If the condition evaluates to `True`, the loop's body will run. Once the condition is `False`, the loop stops.
- **Body of the Loop**: This is the block of code that gets executed repeatedly as long as the condition is true. It's indented under the `while` statement, which is standard in Python to indicate a block of code.

## Practical Examples of `while` Loops

### 1. Asking for User Input Until a Condition is Met

A common use of `while` loops is to keep asking for user input until the input meets certain criteria. For example, you might ask users to input a password

 and keep asking until they provide a password that’s long enough.

### 2. Accumulating Values

`while` loops can be used to accumulate values. For instance, you might start with a total of 0 and keep adding user-entered numbers to this total until it exceeds a certain amount.

### 3. Control Flow in Applications

In many applications, `while` loops are used to control the flow of the program. For example, a menu-driven program might continue to display the menu and prompt for user input until the user selects the option to exit.

---

## Important Concepts Related to `while` Loops

- **Infinite Loops**: If the condition of a `while` loop never becomes false, the loop will continue indefinitely. This is known as an infinite loop. It's often a mistake, but can be intentional in cases like a server that runs continuously, processing requests.
- **Loop Control Statements**: Python provides control statements like `break` and `continue` to modify the behavior of conditional loops. `break` is used to exit the loop prematurely, and `continue` skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
- **Nested Loops**: Loops can be nested inside other loops. This means you can have a `while` loop inside another `while` loop.

---

# Task List for Conditional Loops

### Question 1

**Objective**: Write a Python program to keep asking for a code until it equals "rzy" and print "Code accepted" once the user enters "rzy".

### Question 2

**Objective**: Write a Python program to keep asking for a code until it equals 4003 and print "Code accepted" when the code is correct.

### Question 3

**Objective**: Write a Python program to keep asking for the user's age until it is over 14 and print "Age accepted" once the user enters an age over 14.

### Question 4

**Objective**: Write a Python program to keep asking the user to input a password until it is longer than 5 characters and print "Password accepted" once the password is longer than 5 characters.

### Question 5

**Objective**: Write a Python program to ask the user if they would like to watch another episode of Modern Family. If they enter the word "yes," then print "playing another episode" and repeat. Otherwise, print "See you later!" and stop.

### Question 6

**Objective**: Write a Python program to keep asking for money until the total amount of money is greater than 100. Print "I accept your offer" once the total money is greater than 100.

---

# Understanding If Statements

- **Purpose**: `if` statements are used to execute a block of code only if a specific condition is true.
- **Syntax**: `if condition:`
- **Example**:
  
```python
if age >= 18:
    print("Adult")
```

---

## The Role of Else Statements

- **Purpose**: `else` is used to execute code when the `if` statement's condition is false.
- **Syntax**:
  ```python
  if condition:
      # code if true
  else:
      # code if false
  ```

---

## Using `elif` for Multiple Conditions

- **Purpose**: `elif` (short for else if) allows you to check multiple conditions after the initial `if`.
- **Syntax**:
  ```python
  if condition1:
      # code if condition1 is true
  elif condition2:
      # code if condition2 is true
  ```

---

## Nested If Statements

- **Purpose**: Nested `if` statements are `if` statements inside another `if` statement. They are useful for checking multiple layers of conditions.
- **Example**:
  ```python
  if condition1:
      if condition2:
          # code if both conditions are true
  ```

---

## Benefits of Case (Switch) Statements

- **Note**: Python doesn't have a built-in case or switch statement. However, it can be mimicked using multiple `elif` statements.
- **Benefit**: Simplifies complex conditional structures, making the code more readable.

---

## Logical Operators: `<`, `>`, `==`

- **Purpose**: These operators are used within conditional statements to compare values.
  - `<` and `>` for less than and greater than.
  - `==` for equality comparison.
  - `!=` for not equal.
- **Example**:
  ```python
  if age < 18:
      print("Minor")
  ```

---

## Using `and`, `or`, and `not`

- **Purpose**: These operators allow for more complex conditionals.

### The `and` Operator

- **Function**: Checks if both conditions are true.
- **Example**:
  ```python
  if age >= 13 and age <= 19:
      print("Teenager")
  ```

### The `or` Operator

- **Function**: Checks if at least one of multiple conditions is true.
- **Example**:
  ```python
  if age < 13 or age > 19:
      print("Not a teenager")
  ```

### The `not` Operator

- **Function**: Inverts the truth value of the condition.
- **Example**:
  ```python
  if not (age >= 18):
      print("Minor")
  ```

---

# Task List for If Statements

### Question 1

Write a Python program to:
1. Input a user's age.
2. Print "You are eligible for movies with a rating of 18 or below" if the user's age is 18 or over.
3. Otherwise, print "You are not eligible for movies with an 18 rating".

### Question 2

Extend the above program to also:
1. Print "You are eligible for movies with a rating of 15 or below" if the user's age is 15 or more.
   - **Note**: Use an `if-elif-else` structure for this purpose.

### Question 3

Write a Python program to:
1. Ask the user how they are feeling.
2. Respond appropriately based on the entered emotion (e.g., "bored" or "tired").
   - **Note**: Include responses for 10 different emotions using `if`, `elif`, and `else` statements.

### Question 4

Write a Python program to:
1. Ask the user what genres they enjoy.
2. Recommend 3 TV shows, films, or books based on their genre preference.
   - **Note**: Support 5 genres and handle unknown genres gracefully.

### Question 5

Write a Python program to:
1. Ask the user to input two numbers.
2. Multiply these two numbers together.
3. Output the result.
   - **Note**: This task does not require an `if` statement.

Extend your above Python program to:
- Ask the user to input two numbers
- Ask the user if they would like to add, multiply, subtract or divide two numbers
- Depending on their answer, add, multiply, subtract or divide the two numbers
- Output the answer 

---

# Basic Definitions

- **and Operator**: This returns `True` if both the conditions around it are true. Otherwise, it returns `False`.
- **or Operator**: This returns `True` if at least one of the conditions around it is true. It returns `False` only if both conditions are false.
- **not Operator**: This inverts the Boolean value of the condition that follows it. If the condition is `True`, `not` makes it `False`, and vice versa.

## Order of Precedence

In Python, the order of precedence for logical operators is `not`, `and`, then `or`. This means:
1. `not` is evaluated first,
2. `and` is evaluated next,
3. `or` is evaluated last.

This precedence can affect how an expression is evaluated if brackets are not used to explicitly state the order of operations.

---

## Examples and Explanation

Let’s use the provided examples to illustrate how Python evaluates these expressions:

### 1. Without Brackets (and takes precedence)
```python
print(city == 'Stirling' or city == 'Dundee' and visits > 4)
```
Here, `and` takes precedence over `or`.
- The expression checks if `city == 'Dundee'` and `visits > 4`. This part evaluates to `False` because the city is 'Stirling'.
- The `or` then evaluates whether `city == 'Stirling'` or the above `and` condition is True. Since city is 'Stirling', the whole expression evaluates to `True`.

### 2. Brackets around `and`
```python
print(city == 'Stirling' or (city == 'Dundee' and visits > 4))
```
- Similar to the first example, but brackets explicitly show the intended precedence.
- This is clearer but functionally the same as the first expression.

### 3. Brackets around `or`
```python
print((city == 'Stirling' or city == 'Dundee') and visits > 4)
```
- Brackets change the evaluation order by making `or` evaluated first.
- This checks if either city is 'Stirling' or 'Dundee'. That part is True since city is 'Stirling'.
- Then it checks if visits is more than 4 (which it is not, since visits is 3), so the overall expression is `False`.

### 4. Another example with `or` precedence
```python
print((city == 'Stirling' and visits > 4

) or (city == 'Dundee' and visits > 4))
```
- This statement is checking two conditions separately for Stirling and Dundee, each combined with `visits > 4`.
- Both conditions are False, as visits is not more than 4, so the overall expression is `False`.

---

# Activity - Logic

**19 marks**

## Exercise 1: Basic Logical Operators

### 1. Exercise 1.1

- **Question**: Assign values to variables representing the temperature and whether it is sunny. Write a Python program to check if the temperature is greater than 15 and it is sunny. Print the result. [1]

### 2. Exercise 1.2

- **Question**: Assign values to variables representing the temperature and whether it is raining. Write a Python program to check if the temperature is greater than 15 or it is raining. Print the result. [2]

### 3. Exercise 1.3

- **Question**: Assign a value to a variable representing the number of apples. Write a Python program to check if the number of apples is not greater than 10. Print the result. [2]

## Exercise 2: Precedence of Logical Operators

### 1. Exercise 2.1

- **Question**: Assign values to variables representing the age of a person and whether they have a driving licence. Write a Python program to check if the person is older than 18 and has a driving licence. Print the result. [2]

### 2. Exercise 2.2

- **Question**: Assign values to variables representing the speed of a car and whether it is raining. Write a Python program to check if the speed is greater than 60 or it is not raining. Print the result. [2]

### 3. Exercise 2.3

- **Question**: Assign values to variables representing the number of hours studied and whether the student feels prepared. Write a Python program to check if the number of hours studied is greater than 5 or the student feels prepared. Use parentheses to ensure that the 'or' condition is evaluated first. Print the result. [2]

## Exercise 3: Complex Logical Expressions

### 1. Exercise 3.1

- **Question**: Assign values to variables representing the number of assignments completed and the number of assignments pending. Write a Python program to check if the number of assignments completed is greater than 5 and the number of assignments pending is less than 2. Print the result. [2]

### 2. Exercise 3.2

- **Question**: Assign values to variables representing the amount of savings and the price of a desired item. Write a Python program to check if the amount of savings is greater than the price of the item or if the item is on sale. Print the result. [3]

### 3. Exercise 3.3

- **Question**: Assign values to variables representing the weather condition (sunny or not) and the day of the week (weekend or not). Write a Python program to check if it is sunny and it is the weekend or if it is not sunny and it is a weekday. Print the result. [3]