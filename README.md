**REGular EXpression or regex:**
String containing a combination of normal characters and special metacharacters that describes patterns to find text or positions within a text

Applications:
:String manipulation
e.g. replace and andspecific substrings
:String formatting
e.g. interpolating a string in a template
:Basic and advanced regular expressions
e.g.  nding complex patterns in a string

> Why do we need regular expressions ?
Clean dataset to prepare it for text mining or sentiment analysis
Process email content to feed a machine learning algorithm that decides whether an email is spam
Parse and extract speci c data from a website to build a database

String formating includes:
**Positional formatting**
**Formatted string literals**
**Template method(Use many $identifier)**

Which should I use?
str.format() :
* Good to start with. Concepts apply to f-strings.
* Compatible with all versions of Python.
f-strings:
* Always advisable above all methods.
* Not suitable if not working with modern versions of Python (3.6+).
Template strings:
* When working with external or user-provided strings

Type conversions allowed:
+ !s (string version)
+ !r (string containing a printable representation, i.e. with quotes)
+ !a (some as !r but escape the non-ASCII characters)

Standard format specifier:
* e (scientific notation, e.g. 5 10^3)
* d (digit, e.g. 4)
* f (float, e.g. 4.5353)

Escape Sequences:
* backslashes \
* Use $$ to escape the dollar sign

**Python Supported Methods**
Library: re
|re.search(r"regex",string)| re.match(r"regex",string)|re.findall(r"regex",string)|
|--------------------------|--------------------------|---------------------------|
| search everywhere | anchored at beginning | return all matches |

|Metacharacter|Meaning|
|----|---------------|
|\d | digit|
|\w | word character|
|\W | non-word character|
|\s | whitespace|
|\S | pattern containing no whitespace|
|. |match any character(except newline)|
|^ | start of the string|
|$ | end of the string|
|| | OR operator|

Qantifiers tells the regex engine how many times to match a character immediately to its left.

Quantifiers|Meaning|
|----|---------------|
|+ | one or more|
|* | no or more|
|{} | number of times the character on the left appears|
|{n,m} | n times at least , m times at most|
|? | zero or more|

Two types of matching methods:
* Greedy
* Non-greedy or lazy

|     GREEDY      |   NON-GREEDY   |
|-----------------|----------------|
|1. Match as      | 1. Match as few|
| many characters | characters as  |
| as possible;    | needed; return |
| return          | shortest match |
| longest match   |                |
|2. Standard      | 2. Append ? to |
|quantifiers are  | non-greedy     |
|greedy by default| match          |


**Capturing Groups**
Match a specific subpattern in a pattern.Groups can be used to choose between optional patterns.
* Alternation - Use non-capturing groups for alternation
* Non-capturing Group - Match but not capture a group.Useful when agroup is not backreferenced;Add ?: : (?:regex)

**Numbered Groups**

**Named Groups**
Give a name to the groups (?P<name>regex)
  
**Backreferences**
Using capturing groups to reference back to a group

**Looking Around**
Allow us to con rm that sub-pattern is ahead or behind main pattern
* Look Ahead positive: (?=regex) negative: (?!regex)
* Look Behind positive: (?<=regex) negative: (?<!regex)

For more information and guide to building regex check [link]
(https://regex101.com/)

