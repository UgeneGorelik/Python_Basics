import re

#example of raw string where \t \n is also used as a charachter



'''


.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
'''
st=(r'\tTTT')

text_to_search='''
   ha haha
   12d
   aa
   dd.

'''
sentence='start a'

pattern=re.compile(r'.')


#match dot
pattern=re.compile(r'\.')

#match word after dot
pattern=re.compile(r'avi\.com')

#match 2 numbers
pattern=re.compile(r'\d\d.')


#fecth the matchs from pattern to text to search
matches=pattern.finditer(text_to_search)

#open file to search
with open('data.txt','r') as f:
    #read file contents
    contents=f.read()
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
    #number and or -  or .
    pattern = re.compile(r'\d\d\d[-.]\d\d\d.\d\d\d')
    #number starts with 8 or 9
    pattern = re.compile(r'[89]\d\d[-.]\d\d\d.\d\d\d')
    #in number range
    pattern = re.compile(r'[1-5]')
    pattern = re.compile(r'[a-zA-z]')
    #everething not in charset
    pattern = re.compile(r'[^a-zA-z]')
    #not starts with b but at
    pattern = re.compile(r'[^b]at')


    #quantifuer 3 numbers
    pattern = re.compile(r'\d{3}.\d{3}.\d{3}')
    #0 or one
    pattern = re.compile(r'Mr\.?')

    #groups
    pattern = re.compile(r'M(r|s|rs)')

    matches = pattern.finditer(contents)

    for match in matches:
        print((match))


