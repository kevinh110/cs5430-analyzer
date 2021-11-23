# cs5430-analyzer

To use:

Unzip directory

Just run ./analyze.sh input output where input is the input file path and 
output is the output file path
e.g. ./analyze.sh tests.txt tests_out.txt

Note that input command components must be comma delimited with one command 
on each line. Invalidly formatted commands are interpreted as comments. See
tests.txt or the other test files for examples.

Note that setup.sh is just an empty file. This is because our analyzer requires 
no further environment setup on UGCLinux. We tested on UGCLinux Servers which 
already have python3 installed.



