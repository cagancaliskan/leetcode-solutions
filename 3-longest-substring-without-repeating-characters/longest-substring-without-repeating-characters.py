class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_index_map = {}
        
        left = 0
        max_len = 0
        
        # Enumerate is faster than manual indexing in Python
        for right, char in enumerate(s):
            
            # Check if duplicate is found AND if it is inside the current window
            # (char_index_map[char] >= left ensures we don't look at old duplicates outside our window)
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1
            
            # Update the last seen position of the character
            char_index_map[char] = right
            
            # Calculate current window length
            curr_len = right - left + 1
            
            # Optimization: Using 'if' is faster than calling max(max_len, curr_len)
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len