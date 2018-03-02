# CamoflagePuzzle

This respository will create the Camoflage puzzle.  See the examplepuzzle.pdf


Structuring this work:

- Create a Word Bank -
- Create an AnswerKey From the Word Bank -
- Create a Puzzle From the Answer Key -
- Create a tangible output from a Puzzle -
- Structure and properties to tie all of these together -

______________________________________________________________________
- Create a Word Bank -

No hypenated word
No proper nouns
No plurals
Minimum length of 5 letters
Maximum length of 13 letters
We should read a directory of AnswerKeys to create a NegativeWord Bank to not have the same word appear in multiple AnswerKeys

Should this Word Bank really be 26 separate word banks?
'a' => Bank of Words for letter 'a'


- Create an AnswerKey From the Word Bank -

Choose words from the Word Bank
The letter chosen must be index 6 of the word, and the word must fit within the puzzle.
Write to a ?txt? file this answer key for future negative word banks

How well can we choose words such that letters could go in multiple places?


- Create a Puzzle From the Answer Key -

Randomize the rows the of the answer
Add letters to pad out the length of the answer key to 13 characters
Do we add more common letters to make the word less obvious?


- Create a tangible output from a Puzzle -

I'm thinking of a .pdf or a .html file.  Something that we can print out.


- Structure and properties to tie all of these together -

How do we kick this off?  command line?
What properties do we accept?

WordBank source dir?
Negative wordbank source dir?
Output dir?
Puzzle row character length?  currently 13
Minimum word length?          currently 5



- Other Questions -

What determines puzzle difficulty? How can we make more difficult puzzles?

