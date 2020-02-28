import os
import sys
from enum import Enum

class Type(Enum):
    values = "values"
    differences = "differences"


def find_max_sum_subsiquence(sequence, subsequence_mlen_max, type) -> int:
    """Find the consecutive, non-empty subsequence with the highest element"""

    sequence_transformed = []
    siquence_sum_temp_array = []
    # Prepare original sequence in rihght form for algorithm
    if type == Type.values:
        sequence_transformed = sequence
        for i in range(0, len(sequence)):
            #element of sequence, number of elements finded
            siquence_sum_temp_array.append((sequence[i], 0))
    elif type == Type.differences:
        sequence_transformed = [0] * (len(sequence) - 1)
        for i in range(1, len(sequence)):
            #element of sequence, number of elements finded -> start with 1, because with diff
            #we lost 1 element.
            sequence_transformed[i - 1] = abs(sequence[i - 1] - sequence[i])
            siquence_sum_temp_array.append((sequence_transformed[i - 1], 1))

    max_sum = None
    for i in range(0, len(sequence_transformed)):
        for j in range(0, i):
            element, element_num = siquence_sum_temp_array[j]
            tmp = element + sequence_transformed[i]
            element_num = element_num + 1
            if element_num >= subsequence_mlen_max:
                continue
            if max_sum is None or tmp > max_sum:
                max_sum = tmp
            siquence_sum_temp_array[j] = (tmp, element_num)

    return max_sum


def parse_attributes() -> ():
    """Attribute handling"""
    sequence = None
    n = None

    # Check if any of parameters is missing
    assert len(
        sys.argv) == 4, "Invalid number of parameters. Example: python find_subsequence.py data/input_1.txt 9 values"
    filename = sys.argv[1]

    try:
        file = os.path.join(os.path.dirname(__file__), filename)
        f = open(file, "r")
        contents = f.read()
        sequence = [int(x) for x in contents.strip().split(" ")]
    except FileNotFoundError as ex:
        raise Exception("The specified file couldn't be found: %s" % (ex))
    except IOError as ex:
        raise Exception("Something wrong with file: %s" % (ex))

    try:
        n = int(sys.argv[2])
    except ValueError as verr:
        raise Exception("Cannot convert to int %s" % (verr))

    type = sys.argv[3]
    if type == Type.differences.value:
        type = Type.differences
    elif type == Type.values.value:
        type = Type.values
    else:
        raise Exception("Expected input for type is differences and values")
    return sequence, n, type


if __name__ == "__main__":
    sequence, subsequence_len_max, type = parse_attributes()
    print(find_max_sum_subsiquence(sequence, subsequence_len_max, type))
