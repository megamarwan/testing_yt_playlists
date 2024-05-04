def is_palindrome(x):
    # Convert the integer to a string
    x_str = str(x)

    # Check if the string reads the same forwards and backwards
    return x_str == x_str[::-1]