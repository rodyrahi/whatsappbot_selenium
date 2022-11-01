from difflib import SequenceMatcher


def is_matched(a, b):
    r = SequenceMatcher(a=a.lower(), b=b.lower()).ratio()
    print(r)
    print(a,b)

    if r >= 0.9:

        return True

    return False

is_matched(    '''
1. PLATINUM PACKAGE 
2. GOLD PACKAGE 
3. I HAVE MONEY PROBLEM
4. I HAVE A QUERY
''', '''
1. INTERESTED
2. NOT INTERESTED
''' )