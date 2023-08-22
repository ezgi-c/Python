def funcSubstring(inputStr):
	# Write your code here
    def is_palindrome(s):
        return s == s[::-1]

    longest_palindrome = ""
    for i in range(len(inputStr)):
        for j in range(i + 1, len(inputStr) + 1):
            substring = inputStr[i:j]
            if is_palindrome(substring):
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
                elif len(substring) == len(longest_palindrome):
                    longest_palindrome = min(substring, longest_palindrome)

    return longest_palindrome if len(longest_palindrome) > 1 else "None"

def main():
    # input for inputStr
    inputStr = input()
    
    result = funcSubstring("YABCCBAZ")
    print(result)

if __name__ == "__main__":
    main()