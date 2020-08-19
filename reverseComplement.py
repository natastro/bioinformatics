def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

# starting with reverse

# range over each character 'char' of a string Pattern (from beginning to end) using:

for char in Pattern:

# Write a function Reverse() that takes a string Pattern and returns a string formed by reversing all the letters of Pattern.  Recall that for strings x, y, and z, the notation z=x+y concatenates x and y together into the variable z.
def Reverse(Pattern):
    return Pattern[::-1]

# Write a function Complement() that takes a DNA string Pattern and returns a string formed by taking the complement of each letter of Pattern (don't reverse the string yet).

def Complement(Pattern):
    pairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    comp = ''
    for char in Pattern:
        comp += pairs.get(char)
    return comp

# Write a function ReverseComplement() to solve the Reverse Complement Problem, which is reproduced below. (Remember that we have already given you this code at the beginning of the module.) Then add ReverseComplement (and its needed subroutines) to Replication.py.

def ReverseComplement(Pattern):