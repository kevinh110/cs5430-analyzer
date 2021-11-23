import sys 

input_file = sys.argv[1]

MAX = 900

f = open(input_file, "w")
for i in range(MAX):
  line = "Add, s{}, s{}, T\n".format(i, i + 1)
  f.write(line)

for i in range(MAX):
  f.write("Add, s{}, o1, W\n".format(i))





