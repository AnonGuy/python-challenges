# coding=utf-8
import importlib
import os
import subprocess

from typing import List, Any, Dict

__author__ = "Gareth Coles"


def run_flake8(filename: str):
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


def run_console_challenge(filename: str, *args: List[str]):
    try:
        return subprocess.run(
            ["python", filename] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8"
        )
    except subprocess.CalledProcessError as e:
        return e


def run_importable_challenge(module_name: str, function_name: str, *args: List[Any], **kwargs: Dict[Any, Any]):
    mod = importlib.import_module(module_name)
    importlib.reload(mod)  # To be on the safe side

    func = getattr(mod, function_name)
    return func(*args, **kwargs)


def get_modules(directory):
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
