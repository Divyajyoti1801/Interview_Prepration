"""
Encode And Decode Strings

Design an algorithm to encode a list to a string. The encoded string is the sent over the network and is decoded back to the original lists of strings.


Input : ["lint","code","love","you"]
Output : ["lint","code","love","you"]
"""


def encode(strs=[]):
    res = ""

    for s in strs:
        res += str(len(s)) + "#" + s

    return res


def decode(str=""):
    res, i = [], 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1: j + 1 + length])
        i = j + 1 + length

    return res


print("The decoded string : ", decode(encode(["lint", "code", "love", "you"])))
