Downgrade to Palindrome
=============

**Write a function that is given a string, and returns the smallest contiguous substring you can remove to create a palindrome.**

Example output
--------------

```python
>>> downgrade('800233008')
'2'
>>> downgrade('racecarFOOL')
'FOOL'
>>> downgrade('abcdedcba')
''
>>> downgrade('ngryL Myrgn')
'L ' # OR ' M'
>>> downgrade('123456789')
'12345678' # OR '23456789'
```
**Only printable ASCII characters will appear in the input (no newlines, keep it simple)**

Points
------

* Pass the tests
* PEP8 compliance
