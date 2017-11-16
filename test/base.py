# coding=utf-8
import os

from test.utils import run_flake8

__author__ = "Gareth Coles"


class TestCase:
    points = 0  # Number of points earned
    max_points = 0  # Maximum number of points
    passed = False  # Whether this challenge was passed
    flake8 = False  # Whether this challenge passed Flake8's compliance test
    flake8_messages = []  # Messages from Flake8, formatted for the user

    # Bonus points breakdown and whether each bonus point was achieved
    # { "friendly info line": True/False }
    # EG: { "Don't break on an invalid file path": True }
    breakdown = {}

    title = "Easy: Line Counter"  # Friendly name for this challenge
    test_path = "easy/line_counter"  # Path within the challenges dir to this challenge

    def __init__(self):
        self.points = 0
        self.passed = False
        self.flake8 = False
        self.flake8_messages = []
        self.breakdown = {}

        self.test_path = self.test_path.replace("\\", "/").strip("/")  # Pls

    def do_test(self):
        # How you run your tests is up to you
        raise NotImplementedError

    def do_flake8(self):
        # Override this if you're not happy with the default behaviour
        self.flake8_messages = []
        self.flake8 = False

        result = run_flake8(self.test_path)

        if result is None:  # No Flake8
            self.flake8_messages.append("Unable to run Flake8 - it appears to not be installed.")
            return
        elif not result:  # Empty, so no errors
            self.flake8 = True
            self.points += 1
            return

        for line in result:
            parts = line.split(" ", 1)
            file_info = parts[0].split(":")
            filename = file_info[0][len(self.test_path) + 12:]  # Challenges dir plus trailing slash
            line_number = file_info[1]

            self.flake8_messages.append("{} (L{}) - {}".format(filename, line_number, parts[1]))
