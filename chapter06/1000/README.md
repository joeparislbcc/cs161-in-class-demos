# Files and Exceptions

## What is a File?

A set of bits given a name and stored in a computer.

## Reading Text Files

## Writing Text Files

## File Modes

| Mode | How opened                     | File Exists                                                          | File Does Not Exist          |
| ---- | ------------------------------ | -------------------------------------------------------------------- | ---------------------------- |
| 'r'  | read-only                      | Opens the file                                                       | Error                        |
| 'w'  | write-only                     | Clears the file content                                              | Creates and opens a new file |
| 'a'  | write-only                     | Append new content to the end of the file                            | Creates and opens a new file |
| 'r+' | read-and-write                 | Reads and overwrites it from the beginning                           | Error                        |
| 'w+' | read-and-write                 | Clears the file contents                                             | Creates and opens a new file |
| 'a+' | read-and-write                 | File contents are left intact and new content is appended to the end | Creates and opens a new file |
| 'rb' | open as binary file            |
| 'wb  | open binary file for writing   |
| 'ab  | open binary file for appending |

## Word Puzzle

Find a word containing "aeiou" in order.

## Handling Errors

```python
try:
    # suite
except:
    # handle error(s)
else:
    # what to do if no errors
finally:
    # do whether or not there were errors
```
