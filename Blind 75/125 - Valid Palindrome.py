class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lower first
        s = s.lower()
        
        # Iterate through string to remove alpha numeric characters
        newString = ""
        for stringChar in s:
            if stringChar.isalnum():
                newString += stringChar

        # Compare reverse string and the string we got after removing alpha numeric characters
        reverseString = newString[::-1]
        if reverseString == newString:
            return True
        return False
