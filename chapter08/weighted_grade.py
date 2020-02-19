#! /usr/bin/env python3.8
"""Calculate weighted grades."""

from typing import List, Tuple


def weighted_grade(
    scores: List[float], weights: Tuple[float, float, float] = (0.3, 0.3, 0.4)
) -> float:
    """Calculate a weighted grade.

    Given a list of three scores, the weighted grade will be calculated by
    multiplying each grade in turn by its weight.

    Arguments:
        scores {list} -- The scores to be weighted.

    Keyword Arguments:
        weights {tuple} -- The weights applied to each of the scores.
        (default: {(0.3, 0.3, 0.4)})

    Returns:
        float -- The computed weighted grade.

    """
    if len(scores) != 3:
        raise ValueError("You must provide exactly three scores.")

    if len(weights) != 3:
        raise ValueError("You must provide exactly three values to weigh the scores by.")

    return (scores[0] * weights[0]) + (scores[1] * weights[1]) + (scores[2] * weights[2])


def parse_line(line: str) -> Tuple[str, List[float]]:
    """Parse student info.

    Given a string containing a student's name and their grades return a tuple
    containing their information.

    Arguments:
        line {str} -- The student's name.
        List {float} -- The studen't grades.

    Returns:
        Tuple -- A tuple containing the student's name and a list of their
        grades.
    """
    fields: List[str] = line.strip().split(",")
    name: str = fields[1] + " " + fields[0]
    scores: List = []

    # gather the scores, now strings, as a list of floats
    for element in fields[2:]:
        scores.append(float(element))

    return name, scores


def main():
    """Get a line from the file, print the final grade nicely."""
    file_name: str = input("Open what file? ")

    with open(file_name, "r") as grade_file:
        print(f"{'Name':>13s}  {'Grade':>15s}")
        print("-" * 30)

        name: str = ""
        scores: List[float] = []

        for line in grade_file:
            name, scores = parse_line(line)
            grade = weighted_grade(scores)
            print(f"{name:>15s} {grade:14.2f}")


if __name__ == "__main__":
    main()
