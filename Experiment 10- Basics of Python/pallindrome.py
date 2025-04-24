def is_palindrome(s):
    reversed_s = s[::-1]  
    print(f"Reversed String: {reversed_s}")
    
    if s == reversed_s:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

string = input("Enter a string: ").lower()  
is_palindrome(string)
