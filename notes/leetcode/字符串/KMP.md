# KMP

算法4

> For every character c, dfa[c][j] is the pattern position to compare against the next text position after comparing c with pat.charAt(j).

对于每个字符c, dfa[c][j]表示的是，在c和pat[j]比较之后，应该与下一个文本字符比较的pat位置。
dfs[c][j] = next pat index

> For a match, we want to just move on to the 
next character, so dfa[pat.charAt(j)][j] is 
always j+1.

如果匹配上了，我们希望移动到下一个字符，所以dfs[pat[j]][j]等于j+1

> For a mismatch, we know not just txt.charAt(i), but also the j-1 previous characters in the text: they are the first j-1 characters in the pattern.

如果没匹配上，我们不仅知道txt[i], 也知道前j-1个txt中的字符：他们是pat中前j-1个字符。

> For each character c, imagine that we slide a copy of the pattern over these j characters (the first j-1 characters in the pattern followed by c—we are deciding what to do when these characters are txt.charAt(i-j+1..i)), from left to right, stopping when all overlapping characters match (or there are none). 



> This gives the next possible place the pattern 
could match. The index of the pattern character to compare with txt.charAt(i+1) (dfa[txt.charAt(i)][j]) is precisely the number of overlapping characters.