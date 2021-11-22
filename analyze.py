import sys

input_file, output_file = sys.argv[1], sys.argv[2]


def parse_line():
    pass


def parse_input():
    with open(input_file) as file:
        f = open(output_file, 'w')
        for line in file:
            print(line)
            f.write(line)


if __name__ == "__main__":
    parse_input()
