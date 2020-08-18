# for number in range(51):
#     print(2*number)

# To put everything together, we will put all this code into a function, called PatternCount (see below). We will see soon that this function will help us return to finding frequent words in the replication origin.


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
        return count