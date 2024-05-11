Python Basics
===

All we need is Python, and as we need to start somewhere, how about doing it here.

From the [Python 3 tutorial](https://docs.python.org/3/tutorial/index.html):

> Python is an easy to learn, powerful programming language [...] Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development.

## Math Operators

From **highest** to **lowest** precedence:

| Operators | Operation         | Example         |
| --------- | ----------------- | --------------- |
| \*\*      | Exponent          | `2 ** 3 = 8`    |
| %         | Modulus/Remainder | `22 % 8 = 6`    |
| //        | Integer division  | `22 // 8 = 2`   |
| /         | Division          | `22 / 8 = 2.75` |
| \*        | Multiplication    | `3 * 3 = 9`     |
| -         | Subtraction       | `5 - 2 = 3`     |
| +         | Addition          | `2 + 2 = 4`     |

Examples of expressions:

```python
>>> 2 + 3 * 6
# 20

>>> (2 + 3) * 6
# 30

>>> 2 ** 8
# 256

>>> 23 // 7
# 3

>>> 23 % 7
# 2

>>> (5 - 1) * ((7 + 1) / (3 - 1))
# 16.0
```

## Data Types

| Data Type              | Examples                                  |
| ---------------------- | ----------------------------------------- |
| Integers               | `-2, -1, 0, 1, 2, 3, 4, 5`                |
| Floating-point numbers | `-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25` |
| Strings                | `'a', 'aa', 'aaa', 'Hello!', '11 cats'`   |

## Concatenation and Replication

String concatenation:

```python
>>> 'Alice' + 'Bob'
# 'AliceBob'

>>> 'Alice' 'Bob'
# 'AliceBob'
```

String replication:

```python
>>> 'Alice' * 5
# 'AliceAliceAliceAliceAlice'
```

## Variables

You can name a variable anything as long as it obeys the following rules:

1. It can be only one word.

```python
>>> # bad
>>> my variable = 'Hello'

>>> # good
>>> var = 'Hello'
```

2. It can use only letters, numbers, and the underscore (`_`) character.

```python
>>> # bad
>>> %$@variable = 'Hello'

>>> # good
>>> my_var = 'Hello'

>>> # good
>>> my_var_2 = 'Hello'
```

3. It can’t begin with a number.

```python
>>> # this wont work
>>> 23_var = 'hello'
```

4. It can't be a reserved word (a small set of keywords that designate special language functionality)[^1].

```python
>>> False = 2
  File "<stdin>", line 1
    False = 2
    ^^^^^
SyntaxError: cannot assign to False

>>> True = 2
  File "<stdin>", line 1
    True = 2
    ^^^^
SyntaxError: cannot assign to True
```

## Augmented Assignment Operators

| Operator    | Equivalent       |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

Examples:

```python
>>> greeting = 'Hello'
>>> greeting += ' world!'
>>> greeting
# 'Hello world!'

>>> number = 1
>>> number += 1
>>> number
# 2

>>> my_list = ['item']
>>> my_list *= 3
>>> my_list
# ['item', 'item', 'item']
```

## Comments

Inline comment:

```python
# This is a comment
```

Multiline comment:

```python
# This is a
# multiline comment
```

Code with a comment:

```python
a = 1 # initialization
```

## References

- [Python official documentation - An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html#an-informal-introduction-to-python). You could stop reading at the [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists) topic.
- [Book Automate the Boring Stuff with Python - Chapter 1](https://automatetheboringstuff.com/2e/chapter1/). You could stop reading at [the print() Function](https://automatetheboringstuff.com/2e/chapter1/#:~:text=in%20a%20book.-,The%20print()%20Function,-The%20print()) topic.

[^1]: Type `help('keywords')` on the Python interpreter to get a full list of Python's reserved words.
