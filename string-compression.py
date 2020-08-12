"""A simple method for compressing a string is to reduce the amount of repeated information by recording characters and the number of times they repeat (if any).

For example, the compressed version of 'aabbaabb' is 'a2b2a2b2' because 'a' appears twice, followed by 2 'b's, 2 'a's, and 2 'b's.

The compressed version of 'abc' is just 'abc'. That’s because 'a1b1c1' is twice as long as the original string, which would make our compression algorithm pretty useless.

For example:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
 
>>> compress('balloonicorn')
'bal2o2nicorn'"""


