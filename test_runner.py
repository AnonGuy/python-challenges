# coding=utf-8
from test.utils import get_modules
from challenges import user

__author__ = "Gareth Coles"

failures = 0
total_tests = 0
total_points = 0
max_points = 0

if __name__ == "__main__":
    if user.__learner__ == "123456789012345678":
        print("=> Default user ID found - not running tests")
        exit()

    for mod in get_modules("test/tests"):
        try:
            case = mod.Case()
        except Exception as e:
            print("!> Failed to load test case from {}".format(mod.__name__))
            print(e)
            continue

        print("=== {} ({}) ===".format(case.title, mod.__author__))

        try:
            case.do_test()
        except Exception as e:
            print("!> Error running test: {}".format(e))

        try:
            case.do_flake8()
        except Exception as e:
            print("!> Error running PEP compliance: {}".format(e))

        max_points += case.max_points
        total_tests += 1

        if case.passed:
            print("=> Challenge passed with {}/{} points.".format(case.points, case.max_points))
            total_points += case.points
            print()
            print("-- Bonus breakdown --")

            for key in case.breakdown.keys():
                print("=> {}: {}".format(key, "Passed" if case.breakdown[key] else "Failed"))
        else:
            print()
            print("!> Challenge failed. Please try again!")
            failures += 1

        if not case.flake8:
            print("!> PEP8 compliance check failed. Please see the following messages for more information.")
            print()
            for line in case.flake8_messages:
                if line:
                    print("flake8 => " + line)

        print()

    print("=== Results! ===")
    print("Test passed:   {} / {}".format(total_tests - failures, total_tests))
    print("Points earned: {} / {}".format(total_points, max_points))

    if failures:
        exit(1)
