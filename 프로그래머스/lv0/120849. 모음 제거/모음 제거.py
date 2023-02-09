def solution(my_string):
    for char in my_string:
        if char in "AEIOUaeiou":
            my_string= my_string.replace(char,'')
    return my_string
        