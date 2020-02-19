# Iterating Through a Python Dictionary

Dictionaries are one of the most important and useful data structures in Python. They can help you solve a wide variety of programming problems.

For more information on dictionaries, you can check out the following resources:

- Dictionaries in Python
- [Itertools in Python 3, By Example](https://realpython.com/python-itertools)
- The documentation for [map()](https://docs.python.org/3/library/functions.html#map) and [filter()](https://docs.python.org/3/library/functions.html#filter)

## A Few Words on Dictionaries

Dictionaries are a cornerstone of Python. The language itself is built around dictionaries. Modules, classes, objects, globals(), locals(): all of these are dictionaries. Dictionaries have been central to Python from its very beginning.

Python’s official documentation defines a dictionary as follows:

> An associative array, where arbitrary keys are mapped to values. The keys can be any object with `__hash__()` and `__eq__()` methods. ([Source](https://docs.python.org/3/glossary.html#term-dictionary))

There are a couple points to keep in mind:

1. Dictionaries map keys to values and store them in an array or collection.
1. The keys must be of a [hashable](https://docs.python.org/3/glossary.html#term-hashable) type, which means that they must have a hash value that never changes during the key’s lifetime.

Dictionaries are frequently used for solving all kinds of programming problems, so they are a fundamental piece of your tool kit as a Python developer.

Unlike [sequences](https://docs.python.org/3/glossary.html#term-sequence), which are [iterables](https://docs.python.org/3/glossary.html#term-iterable) that support element access using integer indices, dictionaries are indexed by keys.

The keys in a dictionary are much like a set, which is a collection of hashable and unique objects. Because the objects need to be hashable, [mutable](https://docs.python.org/3/glossary.html#term-mutable) objects can’t be used as dictionary keys.

On the other hand, values can be of any Python type, whether they are hashable or not. There are literally no restrictions for values.

In Python 3.6 and beyond, the keys and values of a dictionary are iterated over in the same order in which they were created. However, this behavior may vary across different Python versions, and it depends on the dictionary’s history of insertions and deletions.

In Python 2.7, dictionaries are unordered structures. The order of the dictionaries’ items is __scrambled__. This means that the order of the items is deterministic and repeatable. Let’s see an example:

```python
>>> # Python 2.7
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> a_dict
{'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}
>>> a_dict
{'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}
```

If you leave the interpreter and open a new interactive session later, you’ll get the same item order:

```python
>>> # Python 2.7. New interactive session
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> a_dict
{'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}
>>> a_dict
{'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}
```

A closer look at these two outputs shows you that the resulting order is exactly the same in both cases. That’s why you can say that the ordering is deterministic.

In Python 3.5, dictionaries are still unordered, but this time, __randomized__ data structures. This means that every time you re-run the dictionary, you’ll get a different items order. Let’s take a look:

```python
>>> # Python 3.5
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> a_dict
{'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}
>>> a_dict
{'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}
```

If you enter a new interactive session, then you’ll get the following:

```python
>>> # Python 3.5. New interactive session
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> a_dict
{'fruit': 'apple', 'pet': 'dog', 'color': 'blue'}
>>> a_dict
{'fruit': 'apple', 'pet': 'dog', 'color': 'blue'}
```

This time, you can see that the order of the items is different in both outputs. That’s why you can say they are randomized data structures.

In Python 3.6 and beyond, dictionaries are ordered data structures, which means that they keep their elements in the same order in which they were introduced, as you can see here:

```python
>>> # Python 3.6 and beyond
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> a_dict
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> a_dict
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
```

This is a relatively new feature of Python’s dictionaries, and it’s a very useful one. But if you’re writing code that is supposed to be run in different Python versions, then you must not rely on this feature, because it can generate buggy behaviors.

Another important feature of dictionaries is that they are mutable data structures, which means that you can add, delete, and update their items. It’s worth noting that this also means that they can’t be used as keys to other dictionaries, as they are not hashable objects.

- __Note:__ _Everything you’ve learned in this section is related to the core Python implementation, CPython._

    _Other Python implementations, like PyPy, IronPython or Jython, could exhibit different dictionary behaviors and features that are beyond the scope of this article._

## How to Iterate Through a Dictionary in Python: The Basics

Dictionaries are an useful and widely used data structure in Python. As a Python coder, you’ll often be in situations where you’ll need to iterate through a dictionary in Python, while you perform some actions on its key-value pairs.

When it comes to iterating through a dictionary in Python, the language provides you with some great tools that we’ll cover now.

### Iterating Through Keys Directly

Python’s dictionaries are [mapping objects](https://docs.python.org/3/glossary.html#term-mapping). This means that they inherit some __special methods__, which Python uses internally to perform some operations. These methods are named using the naming convention of adding a double underscore at the beginning of and at the end of the method’s name.

To visualize the methods and attributes of any Python object, you can use `dir()`, which is a built-in function that serves that purpose. If you run `dir()` with an empty dictionary as an argument, then you’ll be able to see all the methods and attributes that dictionaries implement:

```python
>>> dir({})
['__class__', '__contains__', '__delattr__', ... , '__iter__', ...]
```

If you take a closer look at the previous output, you’ll see `'__iter__'`. This is a method that is called when an iterator is required for a container, and it should return a new [iterator object](https://docs.python.org/3/glossary.html#term-iterator) that can iterate through all the objects in the container.

For mappings (like dictionaries), `.__iter__()` should iterate over the keys. This means that if you put a dictionary directly into a `for` loop, Python will automatically call `.__iter__()` on that dictionary, and you’ll get an iterator over its keys:

```python
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> for key in a_dict:
...     print(key)
...
color
fruit
pet
```

If you use this approach along with a small trick, then you can process the keys and values of any dictionary. The trick consists of using the indexing operator `[]` with the dictionary and its keys to get access to the values:

```python
>>> for key in a_dict:
...     print(key, '->', a_dict[key])
...
color -> blue
fruit -> apple
pet -> dog
```

### Iterating Through `.items()`

When you’re working with dictionaries, it’s likely that you’ll want to work with both the keys and the values. One of the most useful ways to iterate through a dictionary in Python is by using `.items()`, which is a method that returns a new [view](https://docs.python.org/3/library/stdtypes.html#dict-views) of the dictionary’s items:

```python
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> d_items = a_dict.items()
>>> d_items  # Here d_items is a view of items
dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
```

Dictionary views like `d_items` provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the views reflect these changes.

Views can be iterated over to yield their respective data, so you can iterate through a dictionary in Python by using the view object returned by `.items()`:

```python
>> for item in a_dict.items():
...     print(item)
...
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')
```

The view object returned by `.items()` yields the key-value pairs one at a time and allows you to iterate through a dictionary in Python, but in such a way that you get access to the keys and values at the same time.

If you take a closer look at the individual items yielded by `.items()`, you’ll notice that they’re really tuple objects.

```python
...     print(item)
...     print(type(item))
...
('color', 'blue')
<class 'tuple'>
('fruit', 'apple')
<class 'tuple'>
('pet', 'dog')
<class 'tuple'>
```

Once you know this, you can use [tuple unpacking](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) to iterate through the keys and values of the dictionary you are working with.

```python
>>> for key, value in a_dict.items():
...     print(key, '->', value)
...
color -> blue
fruit -> apple
pet -> dog
```

- __Note:__ _`.values()` and `.keys()` return view objects just like `.items()`_

### Iterating Through `.keys()`

If you just need to work with the keys of a dictionary, then you can use `.keys()`, which is a method that returns a new view object containing the dictionary’s keys:

```python
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> keys = a_dict.keys()
>>> keys
dict_keys(['color', 'fruit', 'pet'])
```

The object returned by `.keys()` provides a dynamic view on the keys of `a_dict` that can be used to iterate through the keys of the dictionary.

To iterate through a dictionary in Python by using `.keys()`, you just need to call `.keys()` in the header of a `for` loop:

```python
>>> for key in a_dict.keys():
...     print(key)
...
color
fruit
pet
```

When you call `.keys()` on `a_dict`, you get a view of its keys. Python knows that view objects are iterables, so it starts looping, and you can process the keys of `a_dict`.

Using the same trick you’ve seen before (indexing operator `[]`), you can get access to the values of the dictionary:

```python
>>> for key in a_dict.keys():
...     print(key, '->', a_dict[key])
...
color -> blue
fruit -> apple
pet -> dog
```

### Iterating Through `.values()`

It’s also common to only use the values to iterate through a dictionary in Python using the `.values()` method which returns a view with the values of the dictionary:

```python
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> values = a_dict.values()
>>> values
dict_values(['blue', 'apple', 'dog'])
```

In the previous code, `values` holds a reference to a view object containing the values of `a_dict`.

As any view object, the object returned by `.values()` can also be iterated over. In this case, `.values()` yields the values of `a_dict`:

```python
>>> for value in a_dict.values():
...     print(value)
...
blue
apple
dog
```

Using `.values()`, you’ll be getting access to only the values of `a_dict`, without dealing with the keys.

It’s worth noting that they also support [membership tests (`in`)](https://docs.python.org/3/library/stdtypes.html#typesseq-common), which is an important feature if you’re trying to know if a specific element is in a dictionary or not:

```python
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> 'pet' in a_dict.keys()
True
>>> 'apple' in a_dict.values()
True
>>> 'onion' in a_dict.values()
False
```

The membership test using `in` returns `True` if the key (or value or item) is present in the dictionary you’re testing, and returns `False` otherwise. The membership test allows you to not iterate through a dictionary in Python if you just want to know if certain key (or value or item) is present in a dictionary or not.

## Modifying Values and Keys

It's common to need to modify the values and keys when you’re iterating through a dictionary in Python. There are some points you’ll need to take into account to accomplish this task.

The values, for example, can be modified whenever you need, but you’ll need to use the original dictionary and the key that maps the value you want to modify:

```python
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for k, v in prices.items():
...     prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
...
>>> prices
{'apple': 0.36, 'orange': 0.32, 'banana': 0.23}
```

In the previous code example, to modify the values of prices and apply a 10% discount, you used the expression `prices[k] = round(v * 0.9, 2)`.

So why do you have to use the original dictionary if you have access to its key (`k`) and its values (`v`)? Should you be able to modify them directly?

The real problem is that `k` and `v` changes aren’t reflected in the original dictionary. That is, if you modify any of them (`k` or `v`) directly inside the loop, then what really happens is that you’ll lose the reference to the relevant dictionary component without changing anything in the dictionary.

On the other hand, the keys can be added or removed from a dictionary by converting the view returned by `.keys()` into a `list` object:

```python
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in list(prices.keys()):  # Use a list instead of a view
...     if key == 'orange':
...         del prices[key]  # Delete a key from prices
...
>>> prices
{'apple': 0.4, 'banana': 0.25}
```

This approach may have some performance implications, mainly related to memory consumption. For example, instead of a view object that yields elements on demand, you’ll have an entire new list in your system’s memory. However, this could be a safe way to modify the keys while you iterate through a dictionary in Python.

Finally, if you try to remove a key from prices by using `.keys()` directly, then Python will raise a `RuntimeError` telling you that the dictionary’s size has changed during iteration:

```python
>>> # Python 3. dict.keys() returns a view object, not a list
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in prices.keys():
...     if key == 'orange':
...         del prices[key]
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    for key in prices.keys():
RuntimeError: dictionary changed size during iteration
```

This is because `.keys()` returns a dictionary-view object, which yields keys on demand one at a time, and if you delete an item (`del prices[key]`), then Python raises a `RuntimeError`, because you’ve modified the dictionary during iteration.

## Real-World Examples

It’s time to see how you can perform some actions with the items of a dictionary during iteration. Let’s look at some real-world examples.

- __Note:__ _Later on in this article, you’ll see another way of solving these very same problems by using other Python tools._

### Turning Keys Into Values and Vice Versa

Suppose you have a dictionary and for some reason need to turn keys into values and vice versa. In this situation, you can use a for loop to iterate through the dictionary and build the new dictionary by using the keys as values and vice versa:

```python
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {}
>>> for key, value in a_dict.items():
...     new_dict[value] = key
...
>>> new_dict
{1: 'one', 2: 'two', 3: 'thee', 4: 'four'}
```

The expression `new_dict[value] = key` did all the work for you by turning the keys into values and using the values as keys. For this code to work, the data stored in the original values must be of a hashable data type.

### Filtering Items

Sometimes you’ll be in situations where you have a dictionary and you want to create a new one to store only the data that satisfies a given condition. You can do this with an if statement inside a for loop as follows:

```python
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {}  # Create a new empty dictionary
>>> for key, value in a_dict.items():
...     # If value satisfies the condition, then store it in new_dict
...     if value <= 2:
...         new_dict[key] = value
...
>>> new_dict
{'one': 1, 'two': 2}
```

Later we'll see a more Pythonic and readable way to get the same result.

### Doing Some Calculations

It’s also common to need to do some calculations while you iterate through a dictionary in Python. Suppose you’ve stored the data for your company’s sales in a dictionary, and now you want to know the total income of the year.

To solve this problem you could define a variable with an initial value of zero. Then, you can accumulate every value of your dictionary in that variable:

```python
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> total_income = 0.00
>>> for value in incomes.values():
...     total_income += value  # Accumulate the values in total_income
...
>>> total_income
14100.0
```

Here, you’ve iterated through `incomes` and sequentially accumulated its values in `total_income` as you wanted to do. The expression `total_income += value` does the word, and at the end of the loop, you’ll get the total income of the year.

## Using Comprehensions

A __dictionary comprehension__ is a compact way to process all or part of the elements in a collection and return a dictionary as a results.

In contrast to list comprehensions, they need two expressions separated with a colon followed by for and if (optional) clauses.

When a dictionary comprehension is run, the resulting key-value pairs are inserted into a new dictionary in the same order in which they were produced.

Suppose, for example, that you have two lists of data, and you need to create a new dictionary from them. In this case, you can use Python’s `zip(*iterables)` to loop over the elements of both lists in pairs:

```python
>>> objects = ['blue', 'apple', 'dog']
>>> categories = ['color', 'fruit', 'pet']
>>> a_dict = {key: value for key, value in zip(categories, objects)}
>>> a_dict
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
```

Here, `zip()` receives two iterables (`categories` and `objects`) as arguments and makes an iterator that aggregates elements from each iterable. The tuple objects generated by `zip()` are then unpacked into `key` and `value`, which are finally used to create the new dictionary.

Dictionary comprehensions open up a wide spectrum of new possibilities and provide you with a great tool to iterate through a dictionary in Python.

### Turning Keys Into Values and Vice Versa: Revisited

If you take another look at the problem of turning keys into values and vice versa, you’ll see that you could write a more Pythonic and efficient solution by using a dictionary comprehension:

```python
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {value: key for key, value in a_dict.items()}
>>> new_dict
{1: 'one', 2: 'two', 3: 'thee', 4: 'four'}
```

With this dictionary comprehension, you’ve created a totally new dictionary where the keys have taken the place of the values and vice versa. This new approach gave you the ability to write more readable, succinct, efficient, and Pythonic code.

The condition for this code to work is the same one you saw before: the values must be hashable objects. Otherwise, you won’t be able to use them as keys for `new_dict`.

### Filtering Items: Revisited

To filter the items in a dictionary with a comprehension, you just need to add an `if` clause that defines the condition you want to meet.

In the previous example where you filtered a dictionary, that condition was if `v <= 2`. With this `if` clause added to the end of the dictionary comprehension, you’ll filter out the items whose values are greater than `2`. Let’s take a look:

```python
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {k: v for k, v in a_dict.items() if v <= 2}
>>> new_dict
{'one': 1, 'two': 2}
```

Now `new_dict` contains only the items that satisfy your condition. Compared to the previous solutions, this one is more Pythonic and efficient.

### Doing Some Calculations: Revisited

Remember the example with the company’s sales? If you use a list comprehension to iterate through the dictionary’s values, then you’ll get code that is more compact, fast, and Pythonic:

```python
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> total_income = sum([value for value in incomes.values()])
>>> total_income
14100.0
```

The list comprehension created a list object containing the values of `incomes`, and then you summed up all of them by using `sum()` and stored the result in `total_income`.

If you’re working with a really large dictionary, and memory usage is a problem for you, then you can use a [generator expression](https://docs.python.org/3/glossary.html#term-generator-expression) instead of a list comprehension. A __generator expression__ is an expression that returns an iterator. It looks like a list comprehension, but instead of brackets you need to use parentheses to define it:

```python
>>> total_income = sum(value for value in incomes.values())
>>> total_income
14100.0
```

If you change the square brackets for a pair of parentheses (the parentheses of `sum()` here), you’ll be turning the list comprehension into a generator expression, and your code will be memory efficient, because generator expressions yield elements on demand. Instead of creating and storing the whole list in memory, you’ll only have to store one element at a time.

- __Note:__ _If you are totally new to generator expressions, you can take a look at [Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/) to get a better understanding of the topic.

Finally, there is a simpler way to solve this problem by just using `incomes.values()` directly as an argument to `sum()`:

```python
>>> total_income = sum(incomes.values())
>>> total_income
14100.0
```

`sum()` receives an iterable as an argument and returns the total sum of its elements. Here, `incomes.values()` plays the role of the iterable passed to `sum()`. The result is the total income you were looking for.

### Removing Specific Items

Now, suppose you have a dictionary and need to create a new one with selected keys removed. Remember how key-view objects are like sets? Well, these similarities go beyond just being collections of hashable and unique objects. Key-view objects also support common set operations. Let’s see how you can take advantage of this to remove specific items in a dictionary:

```python
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
>>> non_citric
{'apple': 5600.0, 'banana': 5000.0}
```

This code works because key-view objects support set operations like unions, intersections, and differences. When you wrote `incomes.keys() - {'orange'}` inside the dictionary comprehension, you were really doing a `set` difference operation. If you need to perform any set operations with the keys of a dictionary, then you can just use the key-view object directly without first converting it into a `set`. This is a little-known feature of key-view objects that can be useful in some situations.

### Sorting a Dictionary

It’s often necessary to sort the elements of a collection. Since Python 3.6, dictionaries are ordered data structures, so if you use Python 3.6 (and beyond), you’ll be able to sort the items of any dictionary by using `sorted()` and with the help of a dictionary comprehension:

```python
>>> # Python 3.6, and beyond
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> sorted_income = {k: incomes[k] for k in sorted(incomes)}
>>> sorted_income
{'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}
```

This code allows you to create a new dictionary with its keys in sorted order. This is possible because `sorted(incomes)` returns a list of sorted keys that you can use to generate the new dictionary `sorted_dict`.

## Iterating in Sorted Order

Sometimes you may need to iterate through a dictionary in Python but want to do it in sorted order. This can be achieved by using `sorted()`. When you call `sorted(iterable)`, you get a list with the elements of iterable in sorted order.

### Sorted by Keys

If you need to iterate through a dictionary in Python and want it to be sorted by keys, then you can use your dictionary as an argument to `sorted()`. This will return a `list` containing the keys in sorted order, and you’ll be able to iterate through them:

```python
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> for key in sorted(incomes):
...     print(key, '->', incomes[key])
...
apple -> 5600.0
banana -> 5000.0
orange -> 3500.0
```

In this example, you sorted the dictionary (alphabetically) by keys using `sorted(incomes)` in the header of the for loop. Notice that you can also use `sorted(incomes.keys())` to get the same result. In both cases, you’ll get a list containing the keys of your dictionary in sorted order.

- __Note:__ _The sorting order will depend on the data type you are using for keys or values and the internal rules that Python uses to sort those data types._

### Sorted by Values

You could also need to iterate through a dictionary in Python with its items sorted by values. You can use `sorted()` too, but with a second argument called `key`.

The `key` keyword argument specifies a function of one argument that is used to extract a comparison key from each element you’re processing.

To sort the items of a dictionary by values, you can write a function that returns the value of each item and use this function as the `key` argument to `sorted()`:

```python
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> def by_value(item):
...     return item[1]
...
>>> for k, v in sorted(incomes.items(), key=by_value):
...     print(k, '->', v)
...
('orange', '->', 3500.0)
('banana', '->', 5000.0)
('apple', '->', 5600.0)
```

In this example, you defined `by_value()` and used it to sort the items of `incomes` by value. Then you iterated through the dictionary in sorted order by using `sorted()`. The key function (`by_value()`) tells `sorted()` to sort `incomes.items()` by the second element of each item, that is, by the value (`item[1]`).

You may also just want to iterate through the values of a dictionary in sorted order, without worrying about the keys. In that case, you can use `.values()` as follows:

```python
>>> for value in sorted(incomes.values()):
...     print(value)
...
3500.0
5000.0
5600.0
```

`sorted(incomes.values())` returned the values of the dictionary in sorted order as you desired. The keys won’t be accessible if you use `incomes.values()`, but sometimes you don’t really need the keys, just the values, and this is a fast way to get access to them.

### Reversed

If you need to sort your dictionaries in reverse order, you can add `reverse=True` as an argument to `sorted()`. The keyword argument `reverse` should take a boolean value. If it’s set to `True`, then the elements are sorted in reverse order:

```python
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> for key in sorted(incomes, reverse=True):
...     print(key, '->', incomes[key])
...
orange -> 3500.0
banana -> 5000.0
apple -> 5600.0
```

Here, you iterated over the keys of `incomes` in reverse order by using `sorted(incomes, reverse=True)` in the header of the `for` loop.

Finally, it’s important to note that `sorted()` doesn’t really modify the order of the underlying dictionary. What really happen is that `sorted()` creates an independent list with its element in sorted order, so `incomes` remains the same:

```python
>>> incomes
{'apple': 5600.0, 'orange': 3500.0, 'banana': 5000.0}
```

## Iterating Destructively With `.popitem()`

Sometimes you need to iterate through a dictionary in Python and delete its items sequentially. To accomplish this task, you can use `.popitem()`, which will remove and return an arbitrary key-value pair from a dictionary. On the other hand, when you call `.popitem()` on an empty dictionary, it raises a `KeyError`.

If you really need to destructively iterate through a dictionary in Python, then `.popitem()` can be useful. Here’s an example:

```python
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break
```

Here, you used a `while` loop instead of a `for` loop. The reason for this is that it’s never safe to iterate through a dictionary in Python if you intend to modify it this way, that is, if you’re deleting or adding items to it.

Inside the `while` loop, you defined a `try...except` block to catch the `KeyError` raised by `.popitems()` when `a_dict` turns empty. In the `try...except` block, you process the dictionary, removing an item in each iteration. The variable item keeps a reference to the successive items and allows you to do some actions with them.

## Using Some of Python’s Built-In Functions

Python provides some built-in functions that could be useful when you’re working with collections, like dictionaries. These functions are a sort of iteration tool that provides you with another way of iterating through a dictionary in Python.

### `map()`

Python’s `map()` is defined as `map(function, iterable, ...)` and returns an iterator that applies `function` to every item of `iterable`, yielding the results on demand. So, `map()` could be viewed as an iteration tool that you can use to iterate through a dictionary in Python.

Suppose you have a dictionary containing the prices of a bunch of products, and you need to apply a discount to them. In this case, you can define a function that manages the discount and then uses it as the first argument to `map()`. The second argument can be `prices.items()`:

```python
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> def discount(current_price):
...     return (current_price[0], round(current_price[1] * 0.95, 2))
...
>>> new_prices = dict(map(discount, prices.items()))
>>> new_prices
{'apple': 0.38, 'orange': 0.33, 'banana': 0.24}
```

Here, `map()` iterated through the items of the dictionary (`prices.items()`) to apply a 5% discount to each fruit by using `discount()`. In this case, you need to use `dict()` to generate the `new_prices` dictionary from the iterator returned by `map()`.

Note that `discount()` returns a `tuple` of the form (`key, value`), where `current_price[0]` represents the key and `round(current_price[1] * 0.95, 2)` represents the new value.

### `filter()`

`filter()` is another built-in function that you can use to iterate through a dictionary in Python and filter out some of its items. This function is defined as `filter(function, iterable)` and returns an iterator from those elements of i`terable` for which `function` returns `True`.

Suppose you want to know the products with a price lower than `0.40`. You need to define a function to determine if the price satisfies that condition and pass it as first argument to `filter()`. The second argument can be `prices.keys()`:

```python
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> def has_low_price(price):
...     return prices[price] < 0.4
...
>>> low_price = list(filter(has_low_price, prices.keys()))
>>> low_price
['orange', 'banana']
```

Here, you iterated through the keys of prices with `filter()`. Then `filter()` applies `has_low_price()` to every key of `prices`. Finally, you need to use `list()` to generate the list of products with a low price, because `filter()` returns an iterator, and you really need a `list` object.

## Using `collections.ChainMap`

[collections](https://docs.python.org/3/library/collections.html) is a useful module from the Python Standard Library that provides specialized container data types. One of these data types is `ChainMap`, which is a dictionary-like class for creating a single view of multiple mappings (like dictionaries). With `ChainMap`, you can group multiple dictionaries together to create a single, updateable view.

Now, suppose you have two (or more) dictionaries, and you need to iterate through them together as one. To achieve this, you can create a `ChainMap` object and initialize it with your dictionaries:

```python
>>> from collections import ChainMap
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35}
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
>>> chained_dict = ChainMap(fruit_prices, vegetable_prices)
>>> chained_dict  # A ChainMap object
ChainMap({'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55})
>>> for key in chained_dict:
...     print(key, '->', chained_dict[key])
...
pepper -> 0.2
orange -> 0.35
onion -> 0.55
apple -> 0.4
```

After importing `ChainMap` from collections, you need to create a `ChainMap` object with the dictionaries you want to chain, and then you can freely iterate through the resulting object as you would do with a regular dictionary.

`ChainMap` objects also implement `.keys()`, `.values()`, and `.items()` as a standard dictionary does, so you can use these methods to iterate through the dictionary-like object generated by `ChainMap`, just like you would do with a regular dictionary:

```python
>>> for key, value in chained_dict.items():
...     print(key, '->', value)
...
apple -> 0.4
pepper -> 0.2
orange -> 0.35
onion -> 0.55
```

In this case, you’ve called `.items()` on a `ChainMap` object. The `ChainMap` object behaved as if it were a regular dictionary, and `.items()` returned a dictionary view object that can be iterated over as usual.

## Using itertools

Python’s itertools is a module that provides some useful tools to perform iteration tasks. Let’s see how you can use some of them to iterate through a dictionary in Python.

### Cyclic Iteration With `cycle()`

Suppose you want to iterate through a dictionary in Python, but you need to iterate through it repeatedly in a single loop. To get this task done, you can use `itertools.cycle(iterable)`, which makes an iterator returning elements from iterable and saving a copy of each. When iterable is exhausted, `cycle()` returns elements from the saved copy. This is performed in cyclic fashion, so it’s up to you to stop the cycle.

In the following example, you’ll be iterating through the items of a dictionary three consecutive times:

```python
>>> from itertools import cycle
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> times = 3  # Define how many times you need to iterate through prices
>>> total_items = times * len(prices)
>>> for item in cycle(prices.items()):
...     if not total_items:
...         break
...     total_items -= 1
...     print(item)
...
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
```

The preceding code allowed you to iterate through `prices` a given number of times (3 in this case). This cycle could be as long as you need, but you are responsible for stopping it. The `if` condition breaks the cycle when total_items counts down to zero.

### Chained Iteration With `chain()`

`itertools` also provides `chain(*iterables)`, which gets some `iterables` as arguments and makes an iterator that yields elements from the first iterable until it’s exhausted, then iterates over the next iterable and so on, until all of them are exhausted.

This allows you to iterate through multiple dictionaries in a chain, like to what you did with `collections.ChainMap`:

```python
>>> from itertools import chain
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55, 'tomato': 0.42}
>>> for item in chain(fruit_prices.items(), vegetable_prices.items()):
...     print(item)
...
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('pepper', 0.2)
('onion', 0.55)
('tomato', 0.42)
```

In the above code, `chain()` returned an iterable that combined the items from `fruit_prices` and `vegetable_prices`.

It’s also possible to use `.keys()` or `.values()`, depending on your needs, with the condition of being homogeneous: if you use `.keys()` for an argument to `chain()`, then you need to use `.keys()` for the rest of them.

## Using the Dictionary Unpacking Operator (`**`)

Python 3.5 brings a new and interesting feature. [PEP 448 - Additional Unpacking Generalizations](https://www.python.org/dev/peps/pep-0448) can make your life easier when it comes to iterating through multiple dictionaries in Python. Let’s see how this works with a short example.

Suppose you have two (or more) dictionaries, and you need to iterate through them together, without using `collections.ChainMap` or `itertools.chain()`, as you’ve seen in the previous sections. In this case, you can use the dictionary unpacking operator (`**`) to merge the two dictionaries into a new one and then iterate through it:

```python
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35}
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
>>> # How to use the unpacking operator **
>>> {**vegetable_prices, **fruit_prices}
{'pepper': 0.2, 'onion': 0.55, 'apple': 0.4, 'orange': 0.35}
>>> # You can use this feature to iterate through multiple dictionaries
>>> for k, v in {**vegetable_prices, **fruit_prices}.items():
...     print(k, '->', v)
...
pepper -> 0.2
onion -> 0.55
apple -> 0.4
orange -> 0.35
```

The dictionary unpacking operator (`**`) is really an awesome feature in Python. It allows you to merge multiple dictionaries into a new one, as you did in the example with `vegetable_prices` and `fruit_prices`. Once you’ve merged the dictionaries with the unpacking operator, you can iterate through the new dictionary as usual.

It’s important to note that if the dictionaries you’re trying to merge have repeated or common keys, then the values of the right-most dictionary will prevail:

```python
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35, 'pepper': .25}
>>> {**vegetable_prices, **fruit_prices}
{'pepper': 0.25, 'onion': 0.55, 'apple': 0.4, 'orange': 0.35}
```

The pepper key is present in both dictionaries. After you merge them, the `fruit_prices` value for `pepper` (`0.25`) prevailed, because `fruit_prices` is the right-most dictionary.
