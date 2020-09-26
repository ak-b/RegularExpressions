'''
A good example:
* The first part can contain:
    * Upper A-Z and lowercase letters a-z
    * Numbers
    * Characters: !, #, %, &, *, $, .
* Must have @
* Domain:
    * Can contain any word characters
    * But only .com ending is allowed
'''

# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*\$\.]+@\w+\.com"

'''
another example
* It can contain lowercase a-z and uppercase letters A-Z
* It can contain numbers
* It can contain the symbols: *, #, $, %, !, &, .
* It must be at least 8 characters long but not more than 20
'''
regex = r"[a-zA-Z0-9*#\$%\!&\.]{8,20}"

# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"
