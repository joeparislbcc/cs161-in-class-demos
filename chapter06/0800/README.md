# Files and Exceptions

## What is a file?

A set of bits given a name and stored in a computer.

## Accessing Files: Reading and Writing Text Files

## Reading and Writing Files

## File Creation and Overwriting

File modes

| Mode | How opened                    | File Exists                                                          | File Does Not Exist          |
| ---- | ----------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| 'r'  | read-only                     | Opens the file                                                       | Error                        |
| 'w'  | write-only                    | Clears the file content                                              | Creates and opens a new file |
| 'a'  | write-only                    | Append new content to the end of the file                            | Creates and opens a new file |
| 'r+' | read-and-write                | Reads and overwrites it from the beginning                           | Error                        |
| 'w+' | read-and-write                | Clears the file contents                                             | Creates and opens a new file |
| 'a+' | read-and-write                | File contents are left intact and new content is appended to the end | Creates and opens a new file |
| 'rb' | open as binary file           |
| 'wb  | ope binary file for writing   |
| 'ab  | ope binary file for appending |

## Word Puzzle Game

Find a word that has the letters "aeiou" in that order

## Error Handling with Exceptions

```python
try:
    suite
except:
    handle error here
```
