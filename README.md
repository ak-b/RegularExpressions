REGular EXpression or regex:
String containing a combination of normal characters and special metacharacters that describes patterns to find text or positions within a text

Applications:
>String manipulation
e.g. replace and andspecific substrings
>String formatting
e.g. interpolating a string in a template
>Basic and advanced regular expressions
e.g.  nding complex patterns in a string

> Why do we need regular expressions ?
Clean dataset to prepare it for text mining or sentiment analysis
Process email content to feed a machine learning algorithm that decides whether an email is spam
Parse and extract speci c data from a website to build a database

String formating includes:
>Positional formatting
>Formatted string literals
>Template method(Use many $identifier)

Which should I use?
str.format() :
>Good to start with. Concepts apply to f-strings.
>Compatible with all versions of Python.
f-strings:
>Always advisable above all methods.
>Not suitable if not working with modern versions of Python (3.6+).
Template strings:
>When working with external or user-provided strings

Type conversions allowed:
>!s (string version)
>!r (string containing a printable representation, i.e. with quotes)
>!a (some as !r but escape the non-ASCII characters)

Standard format speci􀃗er:
>e (scienti􀃗c notation, e.g. 5 10^3)
>d (digit, e.g. 4)
>f (􀃘oat, e.g. 4.5353)

Escape Sequences:
>backslashes \
>Use $$ to escape the dollar sign

Metacharacter
>\d : digit
>\w : word character
>\W : non-word character
>\s : whitespace
>\S : pattern containing no whitespace
>. : match any character(except newline)
>^ : start of the string
>$ : end of the string

Quantifiers:
>+ : one or more
>* : no or more
>{} : number of times the character on the left appears
>{n,m} : n times at least , m times at most
>? : zero or more

|     GREEDY     |   NON-GREEDY   |
-----------------------------------
| Match as many  | Match as few   |
| characters     | characters as  |
| as possible;   | needed; return |
| return         | shortest match |
| longest match  |
