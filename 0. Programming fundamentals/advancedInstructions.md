## Working with Pre-Defined Functions and Files in Python

### Substrings in Python

A substring is a portion of a string. Python provides easy ways to access and manipulate substrings.

- **To get the first character of a string `name`:**
  ```python
  print(name[0])  # Output: M
  ```

- **To get the first four characters:**
  ```python
  print(name[0:4])  # Output: Mr W
  ```

- **To get the last four characters:**
  ```python
  print(name[-4:])  # Output: lker
  ```

- **To get the last two characters:**
  ```python
  print(name[-2:])  # Output: er
  ```

- **To get characters from index 2 to 5:**
  ```python
  print(name[2:5])  # Output: Wa
  ```

---

### Random Numbers in Python

Python provides several functions in the `random` module to generate random numbers. This module is part of Python's standard utility modules, so it doesn't require any additional installation.

#### Importing the `random` Module

Before you can generate random numbers, you need to import the `random` module:

```python
import random
```

#### Generating a Random Integer

To generate a random integer in Python, you can use the `random.randint()` function. This function takes two arguments: the start and the end of the range within which you want to generate a random integer. Both the start and end values are inclusive.

- **Syntax:**
  ```python
  random.randint(a, b)
  ```
  - `a`: The lower limit of the range (inclusive).
  - `b`: The upper limit of the range (inclusive).

#### Example

Let's say you want to simulate a dice roll, generating a random number between 1 and 6:

```python
import random

dice_roll = random.randint(1, 6)
print(dice_roll)
```

#### Additional Functions

- **`random.randrange(start, stop[, step])`:** Generates a randomly selected element from the range created by the start, stop, and step arguments. The stop parameter is exclusive.
- **`random.choice(sequence)`:** Returns a randomly selected element from a non-empty sequence, such as a list or a string.

#### Practical Applications

Understanding how to generate random numbers and use them effectively can be incredibly useful in programming. Here are a few examples:

- **Game Development:** Creating elements of chance, such as random enemy encounters or loot drops.
- **Simulation:** Simulating real-world events or experiments where outcomes have elements of randomness.
- **Data Analysis:** Generating random datasets for testing algorithms or models.

---

### Task: Number Guessing Game

**Objective:** Write a Python program that implements a number guessing game. The program should generate a random number between 0 and 100 and ask the user to guess the number. The program should provide feedback on whether the guess is too high or too low and continue to prompt the user until the correct number is guessed. Once the correct number is guessed, the program should congratulate the user.

---

## Data Structures: Arrays

### 1-Dimensional Arrays

A 1-D array is a linear structure where each element is of the same data type and is identified by an index number.

#### Basics of 1-D Arrays

- An array can store a group of data elements, all of the same type.
- Each element in the array is accessed using the array's name and an index number.

**Example:**
- **Array `classHeights` stores the heights of students:**
  ```python
  classHeights = [180, 163, 170, 190]
  ```
- **Array `names` might store names of teachers:**
  ```python
  names = ["Mr Walker", "Mr Smith", "Mrs Green"]
  ```

#### Accessing Array Elements

- To access an element from an array, you use the array's name followed by the index number in brackets.
- Remember that in most programming languages, array indexes start at 0.

**Example:**
```python
print(names[0])  # Outputs: Mr Walker
print(names[1])  # Outputs: Mr Smith
print(names[2])  # Outputs: Mrs Green
print(names[3])  # Error, as there is no element at index 3
```

### 2-Dimensional Arrays

A 2-D array is an array of arrays. It is used to represent a table where data is arranged in rows and columns.

#### Basics of 2-D Arrays

- A 2-D array can store a grid of data elements, all of the same type.
- Each element in the 2-D array is accessed using the array's name followed by two index numbers in brackets.

**Example:**
- **A 2-D array `table` stores a 3x3 grid of numbers:**

  ```python
  table = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]
  ```

#### Accessing Elements in a 2-D Array

- To access an element from a 2-D array, you use the array's name followed by two index numbers in brackets.

**Example:**
```python
print(table[0][0])  # Outputs: 1
print(table[1][2])  # Outputs: 6
print(table[2][1])  # Outputs: 8
```

#### Iterating Through a 2-D Array

You can iterate through all elements in a 2-D array using nested loops.

**Example in Python:**
```python
# Define a 2-D array (table)
table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(table[0][0])  # Outputs: 1
print(table[1][2])  # Outputs: 6
print(table[2][1])  # Outputs: 8

# Iterating through the 2-D array
for row in table:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row
```

---

### Task: Arrays in Python

1. **Create an array of five integers:** `[1, 2, 3, 4, 5]`. Print the array.

2. **Given the array** `[10, 20, 30, 40, 50]`, **print the first and last elements** of the array.

3. **Given the array** `[10, 20, 30, 40, 50]`, **change the element at index 2 to 100**. Print the modified array.

4. **Given the array** `[5, 10, 15, 20, 25]`, **print all elements** of the array using a loop.

5. **Given the array** `[2, 4, 6, 8, 10]`, **calculate the sum** of all elements. Print the result.

6. **Given the array** `[12, 45, 2, 9, 50, 33]`, **find and print the maximum value** in the array.

7. **Given the array** `[18, 4, 22, 9, 31, 15]`, **find and print the minimum value** in the array.

8. **Given the array** `[3, 6, 9, 12, 15]`, **print the array in reverse order**.

9. **Given the array** `[7, 14, 21, 28, 35]`, **check if the array contains the number 21**. Print `True` if it does, otherwise print `False`.

10. **Given two arrays** `[1, 2, 3]` **and** `[4, 5, 6]`, **concatenate them** and print the resulting array.

11. **Given the array** `[5, 3, 8, 1, 2]`, **sort the array in ascending order** and print it.

12. **Given the array** `[3, 3, 3, 3, 3]`, **check if all elements are the same**. Print `True` if they are, otherwise print `False`.

13. **Given the array** `[10, 20, 30, 40, 50]`, **create a new array where each element is multiplied by 2**. Print the new array.

14. **Given the array** `[8, 6, 7, 5, 3, 0, 9]`, **remove the element at index 3**. Print the modified array.

15. **Given the array** `[12, 24, 35, 24, 88, 120, 155]`, **remove all occurrences of the value 24**. Print the modified array.

16. **Given the array** `[5, 12, 7, 5, 5, 7]`, **count how many times the number 5 appears** in the array. Print the result.

17. **Given the array** `[9, 3, 6, 1, 7]`, **find and print the index of the number 6**.

18. **Given the array** `[2, 4, 

6, 8, 10]`, **find and print the sum of the even numbers** in the array.

19. **Given the array** `[15, 22, 13, 14, 22, 45]`, **find and print the indices of all occurrences of the value 22**.

20. **Given two parallel arrays** `names = ["Alice", "Bob", "Charlie"]` **and** `scores = [85, 92, 78]`, **print each name along with its corresponding score** in the format "Name: Score".

---

## Subprograms

Subprograms, also known as subroutines, procedures, methods, and functions, are independent blocks of code within a program. They are designed for reuse, enhancing modularity and reducing redundancy in code.

### Types of Subprograms

- **Procedures:** A procedure is a subprogram that performs a specific task but does not return a value.

  ```python
  # This is a procedure as it doesn't return any values
  def add_glitter(bag): 
      bag.append("glitter")

  my_bag = ["keys", "wallet", "phone"]    
  add_glitter(my_bag)
  print(my_bag)  # Output: ["keys", "wallet", "phone", "glitter"]
  ```

- **Functions:** Unlike procedures, functions are designed to return a single value. They are often used to perform calculations or operations that result in a specific output.

  ```python
  # This is a function as it returns a value
  def drink_coffee(cup):
      cup = "empty"
      return cup

  my_cup = "full"
  after_drinking = drink_coffee(my_cup)
  print(my_cup)          # Output: "full"
  print(after_drinking)  # Output: "empty"
  ```

### Parameters and Arguments

- **Parameters:** Variables listed inside the parentheses in the subprogram definition. They act as placeholders for the values that will be passed to the subprogram when it is called.

  ```python
  def greet(name):
      print(f"Hello, {name}!")
  ```

  In this example, `name` is a parameter.

- **Arguments:** The actual values that are passed to the subprogram when it is called. They replace the parameters in the subprogram definition with real data.

  ```python
  greet("Alice")
  ```

  In this example, `"Alice"` is an argument passed to the `greet` function, replacing the parameter `name` with `"Alice"`.

### Example Combining Parameters and Arguments

**Example:**
```python
# Function with two parameters
def calculate_area(length, width):
    area = length * width
    return area

# Calling the function with arguments
room_length = 5
room_width = 4
room_area = calculate_area(room_length, room_width)
print(f"The area of the room is {room_area} square meters.")
```

- `length` and `width` are parameters defined in the `calculate_area` function.
- `room_length` and `room_width` are arguments passed to the `calculate_area` function when it is called.
- The function uses these arguments to perform the calculation and return the area of the room.

---

### Task: Travel Information Program

**Objective:** Write a Python program that uses three subroutines to collect travel information. Each subroutine will ask a question and return the response to the main program. The main program will keep running until the user types "END". The program should ask for the destination, the number of people going, and the method of travel.

---

## Working with Files in Python

Working with files is essential for tasks such as data storage, log creation, and data processing.

### Why Work with Files?

- To handle various tasks like logging system events, storing user data, processing datasets, and more.
- Files can be used for data backup, importing/exporting data, generating reports, and database management.

### File Operations

#### Opening/Closing Files

- Files must be opened for reading/writing and closed after operations are complete.
- In Python, files are automatically closed when using a `with` statement. However, you can explicitly close a file using the `.close()` method if not using `with`.

**Example:**
```python
# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed after the indented block

# Pseudocode for explicit file closing
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()  # Explicitly closing the file
```

#### Reading Files Line by Line

Reading files line by line is useful for processing large files or when handling the file contents incrementally.

**Using `readline` Method:**

- **Read a Single Line:**
  ```python
  with open('./example.txt', 'r') as file:
      first_line = file.readline()
      print(first_line)
  ```

- **Read Multiple Lines Using a Loop:**
  ```python
  with open('./example.txt', 'r') as file:
        line = file.readline()
        while line:
            print(line, end='')  # 'end' prevents adding extra newline
            line = file.readline()
  ```

**Using `readlines` Method:**

- **Read All Lines into a List:**
  ```python
  with open('../example.txt', 'r') as file:
      all_lines = file.readlines()
      for line in all_lines:
          print(line, end='')  # 'end' prevents adding extra newline
  ```

#### Writing to Files

**Example:**
```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, Friend Finder!")
# File is automatically closed after the indented block

# Pseudocode for explicit file closing
file = open('example.txt', 'w')
file.write("Hello, Friend Finder!")
file.close()  # Explicitly closing the file
```

#### Appending to Files

**Example:**
```python
# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\\nAppending this line.")
# File is automatically closed after the indented block

# Pseudocode for explicit file closing
file = open('example.txt', 'a')
file.write("\\nAppending this line.")
file.close()  # Explicitly closing the file
```

---

### Task: File Operations Program

1. **Prompt the User for Their Name:**
   - Ask the user to enter their name.
   - Store the name in a variable.

2. **Prompt the User for Their Age:**
   - Ask the user to enter their age.
   - Ensure the age is a valid integer between 10 and 30.
   - If the entered age is not valid, keep prompting the user until they provide a valid age.

3. **Append the Information to a Text File:**
   - Open the file `people.txt` in append mode.
   - Write the user's name and age to the file in a formatted manner.
   - Close the file.

4. **Comment Your Code:**
   - Include comments that describe the purpose of each section of the code.
   - Explain any loops and conditionals used for validation.

---

## Parallel Arrays

Parallel arrays allow you to store related information across multiple arrays, using the same index to refer to related items.

### Example of Parallel Arrays

**Suppose we have two arrays, `names` and `ages`, storing names of teachers and their ages, respectively:**

```python
names = ["Mr Walker", "Mr Smith", "Mrs Green"]
ages = [45, 32, 32]
```

These arrays are parallel because the indices correspond across both arrays. For example, `names[1]` and `ages[1]` both refer to information about "Mr Smith".

- **To answer a question like "How old is Mr Smith?":**
  - Mr Smith's index is `1` in the `names` array.
  - Therefore, Mr Smith's age is `ages[1]`, which is 32.

### Declaring Parallel Arrays

- **In Pseudocode:**
  ```plaintext
  DECLARE names AS ARRAY INITIALLY[""] * 200
  DECLARE category AS ARRAY INITIALLY[""] * 200 
  DECLARE score AS ARRAY INITIALLY[0] * 200
  ```

- **In Python (for exams):**
  ```python
  name = [""] * 200
  category = [0] * 200
  scores = [0] * 200
  ```

- **In Python (when implementing):**
  ```python
  name = []
  category = []
  scores = []
  ```

---

### Task: Collecting and Storing Data

1. **Set Up the Parallel Arrays:**
   - Ensure the `names`, `ages`, and `colours` arrays are defined with the provided values.

    ```python
    names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Harry", "Ivy", "Jack", "Katie", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tara", "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zach", "Sophie", "Thomas", "Natalie", "Ellie", "Lucas", "Isabella", "Henry", "Amelia", "Leo

", "Ella", "Oscar", "Charlotte"]
    ages = [25, 30, 22, 35, 28, 40, 33, 29, 26, 31, 27, 34, 23, 36, 32, 39, 21, 38, 37, 24, 42, 45, 41, 43, 44, 46, 33, 29, 35, 26, 31, 30, 28, 36, 27, 32, 34, 23, 22, 37]
    colours = ["blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow"]
    ```

2. **Create an Empty List for Storing Results:**
   - Initialise an empty list to store the names, ages, and favourite colours of people who fall within the specified age range (30 to 40).

3. **Loop Through the `ages` Array:**
   - Use a loop to iterate through each element in the `ages` array.
   - For each age, check if it falls within the range of 30 to 40 (inclusive).

4. **Check and Collect Matching Entries:**
   - If the age is within the specified range, collect the corresponding `name`, `age`, and `colour` from the parallel arrays.
   - Append these details to the list created in step 2.

5. **Open a Text File in Write Mode:**
   - Open a file called `people_in_age_range.txt` in write mode to store the results.

6. **Write the Collected Information to the Text File:**
   - Loop through the list of collected entries.
   - For each entry, write the `name`, `age`, and `favourite colour` to the file in a formatted manner.

7. **Close the Text File:**
   - Ensure the file is properly closed after writing all the information.

---

## Programmer-Defined Data Types

### The Concept of a Record

- **A record** is a data type that can hold a set of different data types in one named structure.
- Unlike parallel 1-D arrays, which store individual data types, a record keeps related data together, making it more efficient for sorting and managing.

#### Declaring Records

- **In Pseudocode:**
  ```plaintext
  RECORD player IS {
      STRING uniqueID, 
      INTEGER score, 
      REAL minutes, 
      INTEGER speed, 
      INTEGER Strength, 
      INTEGER agility
  }
  ```

- **In Python:**
  ```python
  # To create a record called Player with default values 
  class Player:
    def __init__(self, uniqueID, score, minutes, speed, strength, agility):
      self.uniqueID: str = uniqueID
      self.score: int = score
      self.minutes: float = minutes
      self.speed: int = speed
      self.strength: int = strength
      self.agility: int = agility
  ```

#### Initialisation in Python

- In Python, when declaring a record, it's necessary to set initial values for each field.
- This requirement varies in other programming languages.

---

### Task: Player Record Program

**Objective:** Create a Python program that uses the `Player` class to manage a list of players. The program should allow the user to add new players, display player information, and modify player stats.

---

## Indexing in Arrays

Indexing allows you to access individual elements in an array using their position. The first element has an index of 0, the second element has an index of 1, and so on.

**Example:**
```python
numbers = [10, 20, 30, 40, 50]

# Access the first element
first_element = numbers[0]
print(first_element)  # Output: 10

# Access the last element
last_element = numbers[-1]
print(last_element)  # Output: 50

# Access the third element
third_element = numbers[2]
print(third_element)  # Output: 30
```

### Iterating Through Arrays

You can iterate through arrays using loops to access and manipulate each element.

#### Using a `for` Loop

A `for` loop is commonly used to iterate through each element in an array.

**Example:**
```python
names = ["Alice", "Bob", "Charlie"]
# Iterate through the array and print each element
for name in names:
    print(name)
# Output:
# Alice
# Bob
# Charlie
```

#### Using a `for` Loop with Index

You can also use a `for` loop to access both the elements and their indices.

**Example:**
```python
names = ["Alice", "Bob", "Charlie"]
# Iterate through the array using the range function to access indices
for i in range(len(names)):
    print(f"Index {i} has value {names[i]}")
# Output:
# Index 0 has value Alice
# Index 1 has value Bob
# Index 2 has value Charlie
```

#### Using a `while` Loop

A `while` loop can be used to iterate through an array until a certain condition is met.

**Example:**
```python
numbers = [1, 2, 3, 4, 5]
i = 0
# Iterate through the array using a while loop
while i < len(numbers):
    print(numbers[i])
    i += 1
# Output:
# 1
# 2
# 3
# 4
# 5
```

---

### Task: Array Manipulation Program

1. **Create an array of integers:** `[10, 20, 30, 40, 50]`.
2. **Modify the array** by replacing the third element with 35.
3. **Print all elements** of the modified array using a loop.

---

## Modifying Elements in Arrays

You can change the elements in an array by accessing them through their index.

**Example:**
```python
numbers = [10, 20, 30, 40, 50]
# Modify the second element
numbers[1] = 25
print(numbers)  # Output: [10, 25, 30, 40, 50]

# Modify the last element
numbers[-1] = 60
print(numbers)  # Output: [10, 25, 30, 40, 60]
```

---

### Summary

- Indexing allows you to access elements in an array using their position.
- `for` loops and `while` loops are commonly used to iterate through arrays.
- You can use loops to access and modify each element in an array.