
[ ] ---> char class

[abc] ---> tries to match a, b or c

[a-c] ---> tries to match a, b or c but in range mode

[a-z] ---> range mode for aphabet

. ^ $ * + ? { } [ ] \ | ( ) ---> Metacharacters are not active inside classes. 
For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$'

[^5]---> complementing the set. This is indicated by including a '^' as the first character of the class, gives you everything except 5

\ ---> takes the meaning of special  characters so thei can be treated as normal strings
\[ ---> will be looking for '['

\w ---> matches any alphanumeric character ---> [a-zA-Z0-9_]
If the regex pattern is a string,
\w will match all the characters marked as letters in the Unicode database 
provided by the unicodedata module. 
You can use the more restricted definition of \w in a string pattern by supplying the re.ASCII flag when compiling the regular expression.

\d
Matches any decimal digit; this is equivalent to the class [0-9].

\D
Matches any non-digit character; this is equivalent to the class [^0-9].

\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].



These sequences can be included inside a character class. For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'

The final metacharacter in this section is '.'  It matches anything except a newline character, and there’s an alternate mode (re.DOTALL) where it will match even a newline '.' is often used where you want to match “any character”

Repetitions such as * are greedy; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern don’t match, the matching engine will then back up and try again with fewer repetitions.

A step-by-step example will make this more obvious. Let’s consider the expression a[bcd]*b. This matches the letter 'a', zero or more letters from the class [bcd], and finally ends with a 'b'. Now imagine matching this RE against the string 'abcbd'.

Step

Matched

Explanation

1

a

The a in the RE matches.

2

abcbd

The engine matches [bcd]*, going as far as it can, which is to the end of the string.

3

Failure

The engine tries to match b, but the current position is at the end of the string, so it fails.

4

abcb

Back up, so that [bcd]* matches one less character.

5

Failure

Try b again, but the current position is at the last character, which is a 'd'.

6

abc

Back up again, so that [bcd]* is only matching bc.

6

abcb

Try b again. This time the character at the current position is 'b', so it succeeds.

The end of the RE has now been reached, and it has matched 'abcb'. This demonstrates how the matching engine goes as far as it can at first, and if no match is found it will then progressively back up and retry the rest of the RE again and again. It will back up until it has tried zero matches for [bcd]*, and if that subsequently fails, the engine will conclude that the string doesn’t match the RE at all.

Another repeating metacharacter is +, which matches one or more times. Pay careful attention to the difference between * and +; * matches zero or more times, so whatever’s being repeated may not be present at all, while + requires at least one occurrence. To use a similar example, ca+t will match 'cat' (1 'a'), 'caaat' (3 'a's), but won’t match 'ct'.

There are two more repeating qualifiers. The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional. For example, home-?brew matches either 'homebrew' or 'home-brew'.

The most complicated repeated qualifier is {m,n}, where m and n are decimal integers. This qualifier means there must be at least m repetitions, and at most n. For example, a/{1,3}b will match 'a/b', 'a//b', and 'a///b'. It won’t match 'ab', which has no slashes, or 'a////b', which has four.



