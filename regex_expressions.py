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

#Regex to remove HTML tags
string="I want to see that <strong>amazing show</strong> again!"
string_notags = re.sub(r"<.+?>","", string)

#Commonly used string commands 
sep.join(iterable)

.capitalize(to capitalize the first character)

.split(‘’,maxsplit=2)  (maximum number of substrings we want)

.rsplit

#Escape sequences such as /n and /r indicate a line boundary

.splitlines()
#split at /n sequence

.join(string) #to concatenate

.strip()  #trailing escape sequences will be removed

.rstrip() #to remove from right
.lstrip() #to remove from left
