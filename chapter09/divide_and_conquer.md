# Algorithm Development&mdash;Divide and Conquer

Here we'll build a slightly simplified version of the example from the book.

When building a dictionary you must first decide on the key you will use to access the values in the dictionary. Using the periodic table of the elements we will use to atomic symbol of the element as a key, we will build a dictionary that contains interesting information about that element.

## Working with CSV Files

Storing data as [comma separated values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) gives us a simple, light-weight way to save and transmit data. Using CSV, all the individual pieces of data about a particular entity are saved as text with a comma separating each part. For example, below is some CSV data made up of the last name, first name, and email address of some (fake) users. Notice that each line of text holds the data about exactly one entity (a user in this case) and that each piece of data is separated by a comma.

```text
id,last_name,first_name,email
1,nelissen,lucius,lnelissen0@t.co
2,hiley,arvie,ahiley1@51.la
3,ilyuchyov,anthe,ailyuchyov2@so-net.ne.jp
4,strainge,nickolas,nstrainge3@dyndns.org
5,sunman,darlleen,dsunman4@elpais.com
```

Python's standard library has a module named `csv` that helps read and write CSV files.

```python
import csv

with open("users.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    row_count = 0
    for row in csv_reader:
        if row_count == 0:
            print(f'Field names are: {", ".join(row)}')
        else:
            print(f"id: {row[0]} last name: {row[1]} first name: {row[2]} email address: {row[3]}")
        row_count += 1
print(f"Processed {row_count} lines")
```

demo: `users_demo.py`

The `csv` module has tools that enable you to easily read a line from a CSV file into a dictionary.

```python
import csv

with open("users.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f'{row["id"]} {row["last_name"]} {row["first_name"]} {row["email"]}')
```

demo: `users_dict_demo.py`

## Algorithm Overview

For this example, we will read in information about each element in the periodic table (stored in the file `periodic_table.csv`) and use the atomic mass of each element to determine the atomic weight of a chemical compound. That is, if someone enters the chemical compound such as sulfuric acic (H<sub>2</sub>SO<sub>4</sub>) as H2-S-O4, we will look up the atomic weight of each element in the compound, multiply that by the count of the element in the compound (e.g., H2 means two hydrogen atoms), then add all the masses together.

Let's begin with an algorithm:

1. Read in the contents of the periodic table CSV file
1. Create a dictionary of the periodic table using each element's symbol as the key
1. Prompt the user for a chemical compound string
1. Parse the chemical compound string into a list of elements
1. Parse the list of elements into tuples of elements and their quantities, e.g., "H2" becomes `("H", 2)`
1. Print the name of each element in the compound
1. Add each component's atomic mass to the total mass using the information in the dictionary

Notice how the process has been broken down into small, discreet steps. Each of these is responsible for accomplishing exactly _one part_ of the process. This makes them ideal candidates for each being its own `function`. This also means each would be easy to test.

demo: `periodic_table.py`
