import sys

input_file, output_file = sys.argv[1], sys.argv[2]

# Indexes
R = 0
W = 1
T = 2

state = {}  # subject => [bit, bit, {}]
obj_to_bit = {}


def augment(seen, subject):
    if subject not in seen:
        seen.add(subject)
        canTake = state[subject][2]
        for s in canTake:
            augment(seen, s)
            state[subject][0] |= state[s][0]
            state[subject][1] |= state[s][1]


def search(seen, subj, obj):
    if subj not in seen:
        seen.add(subj)
        if obj in state[subj][T]:
            return True
        for s in state[subj][T]:
            if search(seen, s, obj):
                return True
    return False


def parse_line(line):

    line_arr = line.split(',')
    if len(line_arr) != 4:
        return line

    command = line_arr[0].strip()
    subj = line_arr[1].strip()
    obj = line_arr[2].strip()
    priv = line_arr[3].strip()

    if error_check(command, subj, obj, priv):

        if priv == "T" and not obj in state:
            state[obj] = [0, 0, set()]
        if priv != "T" and not obj in obj_to_bit:
            obj_to_bit[obj] = len(obj_to_bit)
        if not subj in state:
            state[subj] = [0, 0, set()]

        if command == "Add":
            add_com(subj, obj, priv)
            return line
        elif command == "Query":
            if query_com(subj, obj, priv):
                return line.strip() + " YES\n"
            else:
                return line.strip() + " NO\n"
    else:
        return line


def error_check(com, subj, obj, priv):
    if priv == "T":
        if obj in obj_to_bit or subj in obj_to_bit:
            return False
    else:
        if subj in obj_to_bit or obj in state:
            return False
    return True


def add_com(subj, obj, priv):
    # Add new subjects/objects to data structures
    # if priv == "T" and not obj in state:
    #     state[obj] = [0, 0, set()]
    # if priv != "T" and not obj in obj_to_bit:
    #     obj_to_bit[obj] = len(obj_to_bit)
    # if not subj in state:
    #     state[subj] = [0, 0, set()]

    if priv == "R":
        bit_shift = obj_to_bit[obj]
        state[subj][R] |= 1 << bit_shift
    elif priv == "W":
        bit_shift = obj_to_bit[obj]
        state[subj][W] |= 1 << bit_shift
    elif priv == "T":
        state[subj][T].add(obj)


def query_com(subj, obj, priv):

    p = R if priv == "R" else W if priv == "W" else T

    if p == R or p == W:
        bit_string = 1 << obj_to_bit[obj]
        if state[subj][p] & bit_string:
            return True
        augment(set(), subj)
        return state[subj][p] & bit_string
    else:
        return search(set(), subj, obj)


def parse_input():
    with open(input_file) as file:
        f = open(output_file, 'w')
        for line in file:
            out = parse_line(line)
            f.write(out)
        f.close()


if __name__ == "__main__":
    parse_input()
