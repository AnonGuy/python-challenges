# coding=utf-8
import importlib
import os
import subprocess
from types import ModuleType

from typing import List, Any, Dict

__author__ = "Gareth Coles"


def run_flake8(filename: str):
    filename = "challenges" + os.sep + filename
    try:
        result = subprocess.run(
            ["flake8", filename, "--config", "./tox.ini"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8"
        )
    except subprocess.CalledProcessError as e:
        result = e
    except FileNotFoundError:
        return None  # No Flake8

    lines = result.stdout.strip().split("\n")
    return [line for line in lines if line.strip()]


def run_console_challenge(location: str, *args: str):
    # Unless you're checking types, please only use `returncode` and `stdout` on the returned object
    try:
        result = subprocess.run(
            ["python", "challenges" + os.sep + location + os.sep + "__init__.py"] + list(args),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8"
        )
    except subprocess.CalledProcessError as e:
        result = e

    result.stdout = result.stdout.strip().split("\n")
    return result


def run_importable_challenge(module_name: str, function_name: str, *args: Any, **kwargs: Any):
    mod = importlib.import_module(module_name)
    importlib.reload(mod)  # To be on the safe side

    func = getattr(mod, function_name)
    return func(*args, **kwargs)


def get_modules(directory) -> List[ModuleType]:
    directory = os.path.normpath(directory)

    files = filter(
        lambda x: os.path.isfile(os.path.join(directory, x)) and x.endswith(".py") and not x.startswith("__init__"),
        os.listdir(directory)
    )

    modules = []

    for filename in files:
        fn = filename.rsplit(".", 1)[0]
        modules.append(importlib.import_module(directory.replace(os.sep, ".") + "." + fn))

    return modules
