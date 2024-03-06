def rle(string: str) -> str:
    string = string + '~'
    last_el = string[0]
    counter = {}
    result = ''
    for i in range(1, len(string)):
        if last_el == string[i]:
            counter[last_el] = counter.get(last_el, 1) + 1
        else:
            result += last_el
            result += str(counter.get(last_el, ''))
            counter = {}
        last_el = string[i]
    return result


assert rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBB') == 'A4B3C2XYZD4E3F3A6B10'
assert rle("aaa") == "a3"
assert rle("bbbb") == "b4"
assert rle("ccccc") == "c5"
assert rle("eeeffgh") == "e3f2gh"
assert rle("yyyzxyz") == "y3zxyz"
assert rle("aaabbbccc") == "a3b3c3"
assert rle("abcabcabc") == "abcabcabc"

if __name__ == "__main__":
    string = input()
    result = rle(string)
    print(result)
