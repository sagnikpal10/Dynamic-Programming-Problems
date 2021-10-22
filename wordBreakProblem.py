def wordBreak(words, word, out=''):
    if not word:
        print(out)
        return
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix in words:
            wordBreak(words, word[i:], out + ' ' + prefix)


if __name__ == '__main__':
    words = [
        'self', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r',
        'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'
    ]
    word = 'Wordbreakproblem'
    wordBreak(words, word)