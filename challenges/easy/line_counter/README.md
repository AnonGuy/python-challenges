Line Counter
============

**Write a program that takes a filename as a command-line argument and prints the number 
of lines in that file.**

Example output
--------------

```batch
> python __init__.py file_with_four_lines.txt
4
```

Research Topics
---------------

* `sys.argv`
* `open()`
* `os.path.exists()`
* `os.path.isfile()`

Points
------

* Pass the tests
* PEP8 compliance
* Bonus: Detect missing or invalid filenames and don't error

Tests
-----

Your program will be tested against the following:

* Test 1: A file with 20 numbered lines
* Test 2: A file with 25 empty lines
* Bonus: An invalid file path
