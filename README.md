# CamouflagePuzzle

This respository will create the Camouflage puzzle.  See the examplepuzzle.pdf

Rules of the Puzzle
- [Rules of the Puzzle](https://github.com/TurnUpTheMike/CamouflagePuzzle/blob/master/README.md#rules-of-the-puzzle)

The Coding Competition:
- [The Coding Competition](https://github.com/TurnUpTheMike/CamouflagePuzzle/blob/master/README.md#the-coding-competition)

Structuring this work:
- [Create a Word Bank](https://github.com/TurnUpTheMike/CamouflagePuzzle#create-a-word-bank)
- [Create an AnswerKey From the Word Bank](https://github.com/TurnUpTheMike/CamouflagePuzzle#create-an-answerkey-from-the-word-bank)
- [Create a Puzzle From the Answer Key](https://github.com/TurnUpTheMike/CamouflagePuzzle#create-a-puzzle-from-the-answer-key)
- [Create a tangible output from a Puzzle](https://github.com/TurnUpTheMike/CamouflagePuzzle#create-a-tangible-output-from-a-puzzle)
- [Structure and properties to tie all of these together](https://github.com/TurnUpTheMike/CamouflagePuzzle#structure-and-properties-to-tie-all-of-these-together)

Other:
- [Running Tests](https://github.com/TurnUpTheMike/CamouflagePuzzle/blob/master/README.md#running-tests)
- [Packaging and Creating Artifacts](https://github.com/TurnUpTheMike/CamouflagePuzzle/blob/master/README.md#packaging-and-creating-artifacts)

______________________________________________________________________
Rules of the Puzzle
-------------------

Place each of the 26 letters of the alphabet once in the grid below to form a common word of <i>five or more letters</i> reading across in each line. Not all the letters in each line will be used; it's up to you to determine which ones are needed. Some letters may fit in more than one of the empty squares to form familiar words; however, only one arrangment of all of the letters of the alphabet will complete a word in each row. Hyphenated words, proper nouns, and plurals are not used.

The Coding Competition
----------------------

When: May 23rd - June 6th
This coding competition will be announced on May 23rd.  I'll accept submissions for the competition until June 6th.

Who can enter: Anyone who makes a branch and pull request to the master branch will be considered. Team submissions are also accepted however only one prize is awarded.  

What are we doing / How do you win: The goal is to consistently create challenging-generated-puzzles.  You must also provide the execution command to execute (documentation is nice, and I need to know the various flag values).  I expect that most of the submissions will be extensions to the AnswerKeyGenerator and/or the PuzzleGenerator.  A submission must also respect the instructions of the puzzle (found at the top of the example).

How is the winner determined: Myself and other judges will attempt to solve puzzles from each of the submissions.  If you would like to be a judge, please send me an email at michael.pantaleano@wpengine.com.

The Prize: The winning submission will be awarded a one-year subscription to GAMES magazine.  I'm estimating that the judges can come to a conclusion in a two week period.  I will attempt to announce and contact the winner on June 20th.

______________________________________________________________________
Create a Word Bank
------------------

No hypenated word
No proper nouns
No plurals
Minimum length of 5 letters
Maximum length of 13 letters
We should read a directory of AnswerKeys to create a NegativeWord Bank to not have the same word appear in multiple AnswerKeys

Should this Word Bank really be 26 separate word banks?
'a' => Bank of Words for letter 'a'


Create an AnswerKey From the Word Bank
--------------------------------------

Choose words from the Word Bank
The letter chosen must be index 6 of the word, and the word must fit within the puzzle.
Write to a ?txt? file this answer key for future negative word banks

How well can we choose words such that letters could go in multiple places?


Create a Puzzle From the Answer Key
-----------------------------------

Randomize the rows the of the answer
Add letters to pad out the length of the answer key to 13 characters
Do we add more common letters to make the word less obvious?


Create a tangible output from a Puzzle
--------------------------------------

I'm thinking of a .pdf or a .html file.  Something that we can print out.


Structure and properties to tie all of these together
-----------------------------------------------------

How do we kick this off?  command line?
What properties do we accept?

WordBank source dir?
Negative wordbank source dir?
Output dir?
Puzzle row character length?  currently 13
Minimum word length?          currently 5



Other Questions
---------------

What determines puzzle difficulty? How can we make more difficult puzzles?


Running Tests
-------------

Running Unit Tests
```
cd CamouflagePuzzle/camo

Run all the tests
python3 -m unittest

Run a specific test
python3 -m unittest solution.test.testpuzzle.TestPuzzleGenerator.test_create_right_padding
```

Running End To End

```
cd CamouflagePuzzle/camo

Run with all defaults
python3 camouflage.py

Run hardcoded version
python3 camouflage.py --bank-generator hardcoded

Run Pants way
python3 camouflage.py --bank-generator flatfiles

Run Alan way
python3 camouflage.py --bank-generator alan
```

Packaging and Creating Artifacts
--------------------------------
```
This flag will create a pdf and an answerkey txt
python3 camouflage.py --do-package-puzzle

The default answerkey filename is answerkey_{}.txt and a timestamp will be formatted into the filename
You can override the output answerkey filename with
python3 camouflage.py --do-package-puzzle --answerkey-txt-name favorite_puzzle_name.txt

You can override the output puzzle pdf name with
python3 camouflage.py --do-package-puzzle --puzzle-pdf-name favorite_puzzle.pdf
```
