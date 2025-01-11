is_digit = lambda s: s.isdigit()

# Test cases
print(is_digit("123"))   # Output: True
print(is_digit("abc"))   # Output: False
print(is_digit("12.3"))  # Output: False (because of the dot)
print(is_digit(""))      # Output: False (empty string is not a digit)
