import sys

input_file, output_file = sys.argv[1], sys.argv[2]

state = {}  # subject => [bit, bit, {}]
#                           R   W   T
obj_to_bit = {}


def parse_line(line):
    line_arr = line.split(',')
    command = line_arr[0].strip()
    subj = line_arr[1].strip()
    obj = line_arr[2].strip()
    priv = line_arr[3].strip()

    if subj not in obj_to_bit:
        if command == "Add":
            add_com(subj, obj, priv)
        elif command == "Query":
            query_com
    else:
        print("comment")


def add_com(subj, obj, priv):
    if not obj in obj_to_bit:
        obj_to_bit[obj] = len(obj_to_bit)

    if not subj in state:
        state[subj] = [0, 0, {}]

    bit_shift = obj_to_bit[obj]
    if priv == "R":
        state[subj][0] |= 1 << bit_shift
    elif priv == "W":
        state[subj][1] |= 1 << bit_shift
    elif priv == "T":
        state[obj][2].add(sub)


def query_com(subj, obj, priv):
    bit_string = 1 << obj_to_bit[obj]
    if priv == "R":
        stack = []
        stack.append(subj)
        while(len(stack) > 0):
            subject = stack.pop()
            perms = state[subject][0]
            if bit_string & perms == 1:
                return True


# def query_dfs(subj):
#     for subj2 in state[subj][2]:
#         subj2 = state[subj][2].pop()
#         query_dfs(subj2)
#         state[subj][0] |= state[subj2][0]
#         state[subj][1] |= state[subj2][1]


def parse_input():
    with open(input_file) as file:
        f = open(output_file, 'w')
        for line in file:
            parse_line(line)


if __name__ == "__main__":
    parse_input()
