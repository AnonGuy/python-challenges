Comprenez-vous?
=============

**Write a list comprehension to transform data in this format:**
```python
{
    "ids": {
        "<uuid>": "<id>",
        ...
    },
    "names": {
        "<uuid>": "<name>",
        ...
    },
    "roles": {
        "<uuid>": ["<role1>", "<role2>"],
        ...
    }
}
```
**Into the following:**
```python
{
    "<uuid>": {
        "id": "<id>",
        "name": "<name>",
        "roles": [...]
    },
    ...
}
```
**Remember, this has to be a dict comprehension, so a one-liner!**

Example output
--------------

```python
>>> data = {"ids": {"<uuid>": "<id>"}, "names": {"<uuid>": "<name>"}, "roles": {"<uuid>": ["<role1>"]}}
>>> transform(data)
{"<uuid>": {"id": "<id>","name": "<name>","roles": ["<role1>"]}}
```

Research Topics
---------------
* `dict` comprehension

Points
------

* Pass the test
* Make your comprehension as short as possible!
