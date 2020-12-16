words = ['yeshowmuchiloveyoumydearmotherreallyicannotbelieveit', 'yeaphowmuchiloveyoumydearmother']
word = "$".join(words)
word_len = len(word)


sa = [i for i in range(word_len)]
rank = [ord(i) for i in word]
tmp = [0] * word_len


# def f(x): return rank[x] if x < word_len else -1
def f(x):
    if x < word_len:
        return rank[x]
    else:
        return -1


t = 1
while t <= word_len:
    sa.sort(key=lambda x: (f(x), f(x + t)))
    p = 0
    tmp[sa[0]] = 0

    for i in range(1, word_len):
        if f(sa[i - 1]) != f(sa[i]) or f(sa[i - 1] + t) != f(sa[i] + t):
            p += 1
        tmp[sa[i]] = p
    print(sa, rank, tmp)
    rank = tmp[:]
    t <<= 1


result = [0]*word_len
for i in range(word_len):
    rank[sa[i]] = i

length = 0
for i in range(len(word.split()[0])):
    if not rank[i]:
        continue
    j = sa[rank[i] - 1]
    while i+length < word_len and j+length < word_len and word[i+length] == word[j+length]:
        length += 1

    result[rank[i]] = length
    length = length-1 if length else length

m = (0, 0)

for i, j in enumerate(result):
    if 0 <= sa[i-1] + j - 1 < len(words[0]) and len(words[0]) < sa[i] + j - 1 < len(word):
        m = max(m, (j, i))

    if 0 <= sa[i] + j - 1 < len(words[0]) and len(words[0]) < sa[i-1] + j - 1 < len(word):
        m = max(m, (j, i))

length, start = m
print(length)
print(word[sa[start]:sa[start]+length])
