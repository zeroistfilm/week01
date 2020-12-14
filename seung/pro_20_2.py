from collections import namedtuple as _namedtuple
import sys
string1 = sys.stdin.readline()
string2 = sys.stdin.readline()

Match = _namedtuple('Match', 'a b size')
ans_list = []
new_list = []
class SequenceMatcher_edit:
    def __init__(self, isjunk=None, a='', b='', autojunk=True, len_ans=0):

        self.isjunk = isjunk
        self.a = self.b = None
        self.autojunk = autojunk
        self.set_seqs(a, b)
        self.len_ans = len_ans

    def set_seqs(self, a, b):

        self.set_seq1(a)
        self.set_seq2(b)

    def set_seq1(self, a):
        if a is self.a:
            return
        self.a = a

    def set_seq2(self, b):
        if b is self.b:
            return
        self.b = b
        self.__chain_b()

    def __chain_b(self):
        b = self.b
        self.b2j = b2j = {}

        for i, elt in enumerate(b):
            indices = b2j.setdefault(elt, [])
            indices.append(i)

    def find_longest_match(self, alo=0, ahi=None, blo=0, bhi=None):
        str1, str2, b2j,len_ans = self.a, self.b, self.b2j, self.len_ans
        besti, bestj, bestsize = alo, blo, 0

        j2len = {}
        nothing = []
        for i in range(alo, ahi):
            j2lenget = j2len.get
            newj2len = {}
            for j in b2j.get(str1[i], nothing):
                if j < blo:
                    continue
                if j >= bhi:
                    break
                k = newj2len[j] = j2lenget(j - 1, 0) + 1
                if k > bestsize:
                    besti, bestj, bestsize = i - k + 1, j - k + 1, k
            j2len = newj2len
        match_1 = Match(besti, bestj, bestsize)


        string1_new = "".join(str1.split(str1[match_1.a:match_1.a + match_1.size]))
        string2_new = "".join(str2.split(str2[match_1.b:match_1.b + match_1.size]))

        new_list.append(str1[match_1.a:match_1.a + match_1.size])

        if match_1.size > len_ans:
            len_ans = match_1.size

        elif match_1.size == len_ans:
            return new_list
        else :
            return new_list

        if match_1.a and match_1.b == 0:
            return new_list

        SequenceMatcher_edit(None, string1_new, string2_new,len_ans).find_longest_match(0, len(string1_new), 0,
                                                                                len(string2_new))

        while besti > alo and bestj > blo and \
                str1[besti - 1] == str2[bestj - 1]:
            besti, bestj, bestsize = besti - 1, bestj - 1, bestsize + 1

        while besti + bestsize < ahi and bestj + bestsize < bhi and \
                str1[besti + bestsize] == str2[bestj + bestsize]:
            bestsize += 1

        while besti > alo and bestj > blo and \
                str1[besti - 1] == str2[bestj - 1]:
            besti, bestj, bestsize = besti - 1, bestj - 1, bestsize + 1
        while besti + bestsize < ahi and bestj + bestsize < bhi and \
                str1[besti + bestsize] == str2[bestj + bestsize]:
            bestsize = bestsize + 1

        return ans_list


sequence_matcher = SequenceMatcher_edit(None, string1, string2, 0)
match1 = sequence_matcher.find_longest_match(0, len(string1), 0, len(string2))
print(len(sorted(new_list)[0]))
print(sorted(new_list)[0])