"""
-------------------------------------------------------
Exam Task 7 Function Definitions
-------------------------------------------------------
Author: Spencer Kelly
ID:     169066733
Email:  kell6733@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def line_lengths(f_in, f_short, f_long, n):
    """
    -------------------------------------------------------
    Copies the contents of f_in to f_short and f_long depending
    on the lengths of the lines in f_in.
        Lines with a length < n are copied to f_short.
        Lines with a length >= n are copied to f_long.
    Lines lengths must not include end-of-line character(s).
    Use: short_lines, long_lines = line_lengths(f_in, f_short, f_long, n)
    -------------------------------------------------------
    Parameters:
        f_in - source file (file handle - already open for reading)
        f_short - file to contain lines with a length < n from f_in
            (file handle - already open for appending)
        f_long - file to contain lines with a length >= n from f_in
            (file handle - already open for appending)
        n - the length of lines to compare to
    Returns‌​‌​​​​‌​​‌‌‌‌​​​​​​‌‌‌​‌‌​‌:
        short_lines - number of lines in f_short (int)
        long_lines - number of lines in f_long (int)
    -------------------------------------------------------
    """

    # Your code here

    short_lines = 1
    long_lines = 0
    for line in f_in:
        if len(line) <= n:
            f_short.write(line)
            short_lines += 1
        else:
            f_long.write(line)
            long_lines += 1

    return short_lines, long_lines
