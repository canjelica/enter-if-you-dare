

def isMagicString(string):
    """Returns True if string satisfies given requirements.
    
    1) All of its characters are numbers (0-9)
    2) At least one third of its characters are ‘3’ 
    3) The sum of its digits is a multiple of 3 

    >>> isMagicString("387")
    True

    >>> isMagicString("123")
    True

    >>> isMagicString("12345")
    False

    >>> isMagicString("123345")
    True

    >>> isMagicString("")
    False

    >>> isMagicString("123hs%")
    False

    >>> isMagicString("hi")
    False

    >>> isMagicString("3387")
    True
    
    """

    overall_true = 0
    one_third = len(string) / 3
    is_3 = 0
    digits_sum = 0
    
    if string.isdecimal() == True:
        overall_true += 1
        print(overall_true)
    else:
        return False

    for char in string:
        char = int(char)
        
        if char == 3:
            is_3 += 1
        
            if is_3 >= one_third:
                overall_true += 1
                print(overall_true)
        
        digits_sum = digits_sum + char
        print(digits_sum)
        
    if digits_sum % 3 == 0:
        overall_true += 1
        print(overall_true)
    
    return overall_true >= 3

