# import difflib
from collections import namedtuple as _namedtuple

Match = _namedtuple('Match', 'a b size')
ans_list = []
new_list = []
class SequenceMatcher_edit:
    def __init__(self, isjunk=None, a='', b='', autojunk=True):

        self.isjunk = isjunk
        self.a = self.b = None
        self.autojunk = autojunk
        self.set_seqs(a, b)

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
        # 여기서 a,b는 받아오는 문자열, j는 b의 공통문자열의 시작 부분
        str1, str2, b2j = self.a, self.b, self.b2j
        besti, bestj, bestsize = alo, blo, 0

        # find longest junk-free match
        # during an iteration of the loop, j2len[j] = length of longest
        # junk-free match ending with a[i-1] and b[j]
        j2len = {}
        nothing = []
        for i in range(alo, ahi):
            # look at all instances of a[i] in b; note that because
            # b2j has no junk keys, the loop is skipped if a[i] is junk
            j2lenget = j2len.get
            newj2len = {}
            for j in b2j.get(str1[i], nothing):
                # a[i] matches b[j]
                if j < blo:
                    continue
                if j >= bhi:
                    break
                k = newj2len[j] = j2lenget(j - 1, 0) + 1
                # print("newj2len[j], j2lenget:",k, j2lenget(j-1,0))
                if k > bestsize:
                    besti, bestj, bestsize = i - k + 1, j - k + 1, k
            j2len = newj2len
            # print("newj2len:",newj2len)
            # print("besti,bestj,bestsize:",besti, bestj, bestsize)
            # print("---")
        match_1 = Match(besti, bestj, bestsize)
        ans_list.append(match_1)
        # print("str1:",str1[match_1.a:match_1.a + match_1.size])
        # print("str2:",str2[match_1.b:match_1.b + match_1.size])

        if match_1.a == 0 and match_1.b == 0:
            return ans_list

        string1_new = "".join(str1.split(str1[match_1.a:match_1.a + match_1.size]))
        string2_new = "".join(str2.split(str2[match_1.b:match_1.b + match_1.size]))

        print("string1 new, 2new:",string1_new,string2_new)
        print("---")
        new_list.append(str1[match_1.a:match_1.a + match_1.size])

        SequenceMatcher_edit(None, string1_new, string2_new).find_longest_match(0, len(string1_new), 0, len(string2_new))


        # Extend the best by non-junk elements on each end.  In particular,
        # "popular" non-junk elements aren't in b2j, which greatly speeds
        # the inner loop above, but also means "the best" match so far
        # doesn't contain any junk *or* popular non-junk elements.
        while besti > alo and bestj > blo and \
                str1[besti - 1] == str2[bestj - 1]:
            besti, bestj, bestsize = besti - 1, bestj - 1, bestsize + 1
            print("while version1 besti,bestj,bestsize:", besti, bestj, bestsize)

        while besti + bestsize < ahi and bestj + bestsize < bhi and \
                str1[besti + bestsize] == str2[bestj + bestsize]:
            bestsize += 1

        # Now that we have a wholly interesting match (albeit possibly
        # empty!), we may as well suck up the matching junk on each
        # side of it too.  Can't think of a good reason not to, and it
        # saves post-processing the (possibly considerable) expense of
        # figuring out what to do with it.  In the case of an empty
        # interesting match, this is clearly the right thing to do,
        # because no other kind of match is possible in the regions.
        while besti > alo and bestj > blo and \
                str1[besti - 1] == str2[bestj - 1]:
            besti, bestj, bestsize = besti - 1, bestj - 1, bestsize + 1
        while besti + bestsize < ahi and bestj + bestsize < bhi and \
                str1[besti + bestsize] == str2[bestj + bestsize]:
            bestsize = bestsize + 1

        return ans_list

string1 = "xzyxyabcdzzpz"
string2 = "zzoxqabcdoazxzyx"
sequence_matcher = SequenceMatcher_edit(None, string1, string2)
match1 = sequence_matcher.find_longest_match(0, len(string1), 0, len(string2))
print("match:",match1)
print("new_list:",new_list)
print(sorted(new_list)[0])