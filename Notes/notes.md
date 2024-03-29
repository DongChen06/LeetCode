


## Recursion (Dynamic Programming)
Following is an example of how to use *recursion* to solve the factorial problem.

![image](https://user-images.githubusercontent.com/25771207/123892427-9106e700-d928-11eb-83b1-2d63ea48ab08.png)


# Python Items

## Big O 
- [cheat Sheet](https://www.bigocheatsheet.com/)

## Math
- module, `12 % 7 = 5`.
- division, `12 // 7 = 1`;   `12 / 7 = 1.714...`.

## String
- startswith("xx"), e.g., 
```
str = "this is string example....wow!!!
print(str.startswith( 'this' ))
==> True
```

- **string.find("s")** and **string.index("s")**: return the index of a specific item.



## set
- Set items are unordered, unchangeable, and do not allow duplicate values.
  
- It is a good tool to check duplicate.



## list
- remove elements:
  
- sort a list: `a = [1,2,1]`, then `a.sort()` --> `a = [1,1,2]`.
  
- slice: reverse a list, `lst[::-1]`;

- pop(index), the default value is -1.

- insert() method inserts an element to the list at the specified index.`list.insert(i, elem)`
e.g.,  `# vowel = ['a', 'e', 'i', 'u'], vowel.insert(3, 'o') >> ['a', 'e', 'i', 'o', 'u']`

- **Attention**, when creating list of class objects, `out = [class] * 4` will make copy of class and will
be overrupted all the values at the same time. Using `out = [class for i in range(4)]` instead. See Q2

- **list.index("bar")**: find index of a specific item.

## dictionary
- **get(keyname, value)**:  returns the value of the item with the specified key. **value** means return value if key is not exist.
e.g., `car = {"model": "Mustang"}, x = car.get("model", 0)`. 


## String
- The **replace()** method replaces a specified phrase with another specified phrase. 
  `e.g., s="she is a mother",  s.replace(" ", "") >> "sheisamother"`

- The lower() method returns a string where all characters are lower case.
    'e.g., s="She is A Mother",  s.lower() >> "she is a mother"'

- **isalnum()** method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

- **lower()** method returns a string where all characters are lower case.
`filter_s = filter_s.lower()`


# Linked Lists (Fast Slow Pointers)

## Singly Linked Lists
![img.png](imgs/img.png)

## Doubly Linked Lists
![img_1.png](imgs/img_1.png)


# Stack and Queue
- **Stack**: last in and first out (LIFO).
- **Queue**: First in and First out. (FIFO)
- **Deque**: New items can be added at either the front or the end.


# Search and Sorting
## Sequential Search

## Binary Search

## Hashing
- **collections**: Counter: dict subclass for counting hashable objects.


## Bubble Sort
![img2.png](imgs/img2.png)

## Selection Sort
![img3.png](imgs/img3.png)


## Insertion Sort


## Shell Sort


## Merge Sort


## Quick Sort



# Useful functions
- check the type of variables: `isinstance(x, int)`.
  
- **bin()**: returns the binary string equivalent to the given integer. `e.g., bin(number) >> 0b101`, where
`ob`  represents that the result is a binary string.
  
- **count()** method returns the number of elements with the specified value. `e.g., list.count(value)`, where 
The value can be any type (string, number, list, tuple, etc.). `e.g., a = '1231', a.count('1') >> 2` 

- **sorted()** function returns a sorted list of the specified iterable object. `e.g., sorted("acad") >> "aacd"`
- `sorted(list, key=x)`, e.g., `intervals.sort(key=lambda x: x[0])`, where `x = [[0, 1], [2, 4]]`
- `sorted(a, reverse=True)`

- **random.randrange(start, stop)** generates a random number.

- **max(iterable, *[, key, default])**: Return the largest item in an iterable or the largest of two or more arguments.
e.g., `max(count.keys(), key = count.get)` (T.169)

- **map(func, iter)**: returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
e.g., `map(str, [1, 2, 3]) --> ['1', '2', '3']`
- **lambda iter: func**: `list(map(lambda x: (float(5)/9)*(x-32), F))`

- **ord()** method in Python converts a character into its Unicode code value. 
- **chr()** method returns a character (a string) from an integer (represents unicode code point of the character). 