# coding=utf-8
from test.base import TestCase
from test.utils import run_console_challenge

__author__ = "Gareth Coles"


class Case(TestCase):
    title = "Easy: Line Counter"
    test_path = "easy/line_counter"

    max_points = 3

    def do_test(self):
        self.breakdown["Don't break on an invalid file path"] = False

        result_one = run_console_challenge(self.test_path, "test/samples/easy_line_counter/20.txt")
        passed_one = False

        if result_one.returncode == 0:
            if "20" in result_one.stdout[0]:
                passed_one = True
            else:
                print("Test 1 | Expected \"20\" in the first line of output; got \"{}\"".format(result_one.stdout[0]))
        else:
            print("Test 1 | Expected a return code of 0; got {}".format(result_one.returncode))

        result_two = run_console_challenge(self.test_path, "test/samples/easy_line_counter/25_empty.txt")
        passed_two = False

        if result_two.returncode == 0:
            if "25" in result_two.stdout[0]:
                passed_two = True
            else:
                print("Test 2 | Expected \"25\" in the first line of output; got \"{}\"".format(result_two.stdout[0]))
        else:
            print("Test 2 | Expected a return code of 0; got {}".format(result_two.returncode))

        if passed_one and passed_two:
            self.points += 1
            self.passed = True

        if not self.passed:
            return

        result_three = run_console_challenge(self.test_path, "test/samples/easy_line_counter/bad_path.txt")

        if result_three.returncode == 0:
            self.points += 1
            self.breakdown["Don't break on an invalid file path"] = True
