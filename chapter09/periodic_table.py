#! /usr/bin/env python3.7
"""Compute the atomic weight of a chemical compound given its formula."""
import csv
import re
from typing import Dict, List, Tuple


def read_periodic_table() -> Dict:
    """Read in the contents of the periodic table CSV file."""
    try:
        with open("periodic_table.csv", "r") as in_file:
            # make a list of strings where each string is a line of text from
            # periodic_table.csv if and only if that line starts with a number
            # (i.e., it is not a header line)
            # text = [line for line in in_file if line[0].isdigit()]
            text = [line.strip() for line in in_file]
    except FileNotFoundError:
        # file not found, gracefully exit by closing all handles, etc. and
        # printing an error message
        raise SystemExit("File periodic_table.csv not found. Program terminating.")
    else:
        return make_periodic_table_dict(text)


def make_periodic_table_dict(elements: List[str]) -> Dict:
    """Create a dictionary of the periodic table.

    This dictionary will map a string, the element's symbol, to another
    dictionary which holds the data about the element.

    This will require massaging the data to re-order it and manipulate the
    headers which will be used as keys in the sub-dictionary."""

    # clean up the headers and remove 'atomic symbol'
    headers = elements.pop(0).replace(" ", "_").split(",")
    headers.pop(1)

    periodic_table: Dict[str, Dict] = {}

    # for each of the elements remaining elements, split the string into a list,
    # pull out the element symbol, create a dictionary of the remaining data,
    # and add the key/value to periodic_table, skipping any missing elements
    for element in elements:
        element_data = element.split(",")
        if element_data[0]:  # skip missing elements like Tennessine (#117)
            symbol = element_data.pop(1)
            headers_and_element_data = zip(headers, element_data)
            periodic_table[symbol] = dict(headers_and_element_data)

    return periodic_table


def get_compound_string(prompt):
    """Prompt the user for a chemical compound string."""
    compound_string = input(prompt)

    return parse_compound_string(compound_string)


def parse_compound_string(compound_string: str) -> List[str]:
    """Parse the chemical compound string into a list of elements."""
    compound_string.replace("-", "")

    # A regular expression that matches any string that begins with exactly
    # *one* upper-case letter, followed by zero or more lower-case lettes,
    # followed by zero or more digits
    compound_regex = r"[A-Z]{1}[a-z]*\d*"

    # get a list of strings that are the compent parts of the compound
    matches = re.findall(compound_regex, compound_string)

    if not matches:
        raise ValueError

    return matches


def parse_element_quantities(compound_components: List[str]) -> List[Tuple[str, int]]:
    """Parse the list of elements into tuples of elements and their quantities,
    e.g., "H2" becomes ("H", 2)."""
    # A regular expression that matches one or more digit characters
    part_regex = r"(\d+)"

    # build a list of components in the compound replacing any missing quantity
    # with a 1
    # can you build a list comprehension that does the same thing?
    components = []
    for component in compound_components:
        parts = re.split(part_regex, component)
        if len(parts) == 1:
            components.append((parts[0], 1))
        else:
            components.append((parts[0], int(parts[1])))

    return components


def print_elements_in_compound(*args):
    """Print the name of each element in the compound."""
    print("The compound is composed of:  ", end="")
    for component in args:
        print(f"{component.title()}", end=" ")

    print()


def compute_atom_weight(components: List[Tuple[str, int]], periodic_table) -> float:
    """Add each component's atomic mass to the total mass using the information
    in the dictionary."""
    weight = 0

    for component in components:
        qty = component[1]
        component_weight = float(periodic_table[component[0]]["atomic_mass"])
        weight += component_weight * qty

    return weight


def main():
    """Run the program."""
    periodic_table = read_periodic_table()

    while True:
        try:
            compound_string = get_compound_string("Please enter a compound string: ")
        except ValueError:
            print("Invalid chemical compound. Please try again.")
        else:
            break

    components = parse_element_quantities(compound_string)

    # get the names of the elements in the compound for printing
    # can you re-write the list complrehension as a series of Python statements?
    component_names = [periodic_table[c[0]]["element_name"] for c in components]

    print_elements_in_compound(*component_names)

    compound_atomic_weight = compute_atom_weight(components, periodic_table)

    print(f"The atomic weight of the compound is {compound_atomic_weight}")

    print("Bye!")


if __name__ == "__main__":
    main()
