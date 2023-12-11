"""
SPLITTING A STRING INTO DESCENDING CONSECUTIVE VALUES

You are given a string `s` that consists of only digits.

Check if we can split `s` into **two or more non-empty substrings** such that the **numerical values** of the substrings are in **descending order** and the **difference** between numerical values of every two **adjacent** **substrings** is equal to `1`.

- For example, the string `s = "0090089"` can be split into `["0090", "089"]` with numerical values `[90,89]`. The values are in descending order and adjacent values differ by `1`, so this way is valid.
- Another example, the string `s = "001"` can be split into `["0", "01"]`, `["00", "1"]`, or `["0", "0", "1"]`. However all the ways are invalid because they have numerical values `[0,1]`, `[0,1]`, and `[0,0,1]` respectively, all of which are not in descending order.

Return `true` *if it is possible to split* `s` *as described above, or* `false` *otherwise.*

A **substring** is a contiguous sequence of characters in a string.

Input: s = "1234"
Output: false
Explanation: There is no valid way to split

"""


def splitting_string_into_descending_consecutive_values(s):
    def DFS(index, prev):
        if index == len(s):
            return True

        for j in range(index, len(s)):
            val = int(s[index:j+1])
            if val + 1 == prev and DFS(j+1, val):
                return True
        return False

    for i in range(len(s)-1):
        val = int(s[:i + 1])

        if DFS(i+1, val):
            return True

    return False


print("Splitting a string into descending consecutive values: ",
      splitting_string_into_descending_consecutive_values("1234"))
