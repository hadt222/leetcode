"""
1079. Letter Tile Possibilities
https://leetcode.com/problems/letter-tile-possibilities/description/?envType=daily-question&envId=2025-02-17
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

from typing import *

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        def backtrack(counter: Counter, path: str) -> int:
            count = 0
            for letter in counter:
                if counter[letter] > 0:
                    # Choose the letter
                    path += letter
                    counter[letter] -= 1
                    count += 1 + backtrack(counter, path)
                    # Backtrack
                    path = path[:-1]
                    counter[letter] += 1
            return count
        
        counter = Counter(tiles)
        return backtrack(counter, "")
    

# Test cases
def test():
    s = Solution()
    assert s.numTilePossibilities("AAB") == 8
    assert s.numTilePossibilities("AAABBC") == 188
    assert s.numTilePossibilities("V") == 1
    print("All test cases passed.")

if __name__ == "__main__":
    test()