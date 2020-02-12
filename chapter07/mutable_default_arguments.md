# Mutable Default Arguments

One of the most common and surprising gotcha's new Python programmers encounter is Python’s treatment of mutable default arguments in function definitions.

## What You Wrote

```python
    def to.append(element)
    return to
```

## What You Might Have Expected to Happen

```python
my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)
```

A new list is created each time the function is called if a second argument isn’t provided, so that the output is:

```python
[12]
[42]
```

## What Does Happen

```python
[12]
[12, 42]
```

A new list is created _once_ when the function is defined, and the same list is used in each successive call.

Python’s default arguments are evaluated _once_ when the function is defined, not each time the function is called (like it is in say, Ruby). This means that if you use a mutable default argument and mutate it, you _will_ and have mutated that object for all future calls to the function as well.

## What You Should Do Instead

Create a new object each time the function is called, by using a default arg to signal that no argument was provided (`None` is often a good choice).

```python
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```

Do not forget, you are passing a _list_ object as the second argument.
