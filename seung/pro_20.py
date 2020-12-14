import difflib

string1 = input()
string2 = input()
if " " in string2 and " " in string1:
    if len(string1) >= len(string2):
        print(len(string2))
        print(string2)
    else :
        print(len(string1))
        print(string1)
else :
    sequence_matcher = difflib.SequenceMatcher(None, string1, string2)
    match = sequence_matcher.find_longest_match(0, len(string1)+1, 0, len(string2)+1)
    print(match)
    print(match.size)
    print(string1[match.a:match.a+match.size])
    blocks = sequence_matcher.get_matching_blocks()
    print(blocks)
    for block in blocks:
       print(string1[block.a:block.a+block.size])

# lambda x: x==" "