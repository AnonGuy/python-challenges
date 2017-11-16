Python Challenges
=================

[Join us on Discord!](https://discord.gg/8NWhsvT)

This repository contains challenges for users that wish to learn more about Python 3. It is designed for the users
of the Python community Discord server, but anyone may participate!

Getting Started
---------------

The first thing you should do is [fork this repository](https://github.com/gdude2002/python-challenges/fork). This will 
create a copy of the repository under your own GitHub account. Once you've done this, go ahead and look in the 
`challenges` folder - each challenge contains two files.

* `README.md` - Offers an overview of the challenge and what is expected of you.
* `__init__.py` - Should contain your solution to the challenge. Note that you're free to add more files and import them

You may use any editor you like (including the GitHub web interface) to complete your challenges. When you're ready to
submit your answers for testing, you should [create a pull request](https://github.com/gdude2002/python-challenges/compare).
Once your pull request has been submitted, CircleCI will test your answers and grade them accordingly.

Feel free to continue working on your challenges as long as you want - practise makes perfect! You won't have to create
a new PR every time, so go nuts!

If you'd like to take a stab at a challenge introduced after you made your pull request, feel free to merge the changes
in yourself. Alternatively, you can always delete your fork and create a new fork.

Requirements
------------

Please bear the following things in mind:

* If you're on the Discord server, please include your Discord user ID in the `user.py` file. 
We will notify you on Discord when your grade is available. If you don't know how to find this, see below:
    * Open your [user settings](https://dl.dropboxusercontent.com/s/b5r4py1wo69hvit/DiscordCanary_2017-11-16_11-03-51.png) on Discord, 
    [head to the `Appearance` section, and enable `Developer Mode`](https://dl.dropboxusercontent.com/s/6bygzblcgazwl8f/DiscordCanary_2017-11-16_11-04-28.png).
    * Find yourself in the user list on a server or find a message that you sent, right-click your avatar, and [click `Copy ID`](https://dl.dropboxusercontent.com/s/18u6gebweck8066/DiscordCanary_2017-11-16_11-05-25.png).
* Do not modify the tests if you're attempting the challenges.
    * While we don't explicitly check this, if you modify the tests then why bother attempting the challenges in the first place?
* All challenges will be tested for [PEP8 compliance](https://www.python.org/dev/peps/pep-0008/).
    * We use the excellent [Flake8 tool](http://flake8.pycqa.org/en/latest/) for this.
    * Failing this test will not fail your challenge entirely, but you will lose points.
    * Our line limit is set to 120 characters (instead of 80) for the sake of sanity.
* Obviously, don't break the build process. You're here to attempt the challenges - unless you're contributing challenges
or tests yourself, please only try to solve the challenges. Anything else will get you blocked from the repo.
    
Libraries
---------

The following libraries are available for you to use in your challenges.

* [Requests](http://docs.python-requests.org/en/master/)

Contributing
============

Are you an experienced Python developer? We're always looking for new challenges and fixes to the existing test suite! Feel
free to submit a pull request that follows our naming conventions, or join us on Discord to discuss any changes you're
not sure about.
