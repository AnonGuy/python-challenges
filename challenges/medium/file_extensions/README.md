File Extensions
=============

**Write a program that takes a list of file extensions as command-line arguments and prints all the files from the current directory matching the extensions given.**

Example output
--------------

```
C:\files>dir /b
csv_file.csv
file_extensions.py
text_file.txt
```
```
C:\files>file-extensions.py txt csv
text_file.txt
csv_file.csv
```
Research Topics
---------------
* `sys.argv`
* `for` loops
* `os.listdir()`
* `string.endswith()`
* `json.load()`
* `open()`

Points
------

* Pass the tests
* PEP8 compliance
* Bonus: Support "categories" of files - for example, the `"c"` category could match `.c` and `.h` files.
* Bonus 2: Support configurable "categories" read from a configuration file.
