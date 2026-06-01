from fileinput import filename
import os

@staticmethod
def read_multiple_lines(filename):
    with open(os.path.dirname(__file__) + '/DataSets/' + filename) as file:
        for line in file :
            yield line.strip()

@staticmethod
def read_multiple_lines_no_backslash_n(filename):
    with open(os.path.dirname(__file__) + '/DataSets/' + filename) as file:
        for line in file :
            yield line.strip('\n')

@staticmethod
def read_one_line(filename):
    with open(os.path.dirname(__file__) + '/DataSets/' + filename) as file:
        return file.readline()
        

@staticmethod
def read_all_lines(filename):
    lines: list[str] = []
    for w in read_multiple_lines(filename) :
        lines.append(w)
    return lines

@staticmethod
def read_all_lines_with_spaces(filename):
    lines: list[str] = []
    for w in read_multiple_lines_no_backslash_n(filename) :
        lines.append(w)
    return lines

@staticmethod
def read_all_lines_as_listlistint(filename):
    lines: list[list[int]] = []
    for w in read_multiple_lines(filename) :
        line = []
        for i in w:
            line.append(int(i))
        lines.append(line)
    return lines