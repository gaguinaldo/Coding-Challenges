"""
Tuple unpacking in python.

"""


def get_earlier(string1, string2):
    
    import re

    m1, d1, y1 = tuple(re.split(r'[/]+', string1))
    m2, d2, y2 = tuple(re.split(r'[/]+', string2))

    string_1_ = (y1, m1, d1)
    string_2_ = (y2, m2, d2)

    if string_1_ < string_2_:
        return string1
    
    else:
        return string2
