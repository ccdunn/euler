import solutions
import importlib


for module in solutions.__all__:
    importlib.import_module("solutions." + module)


def test_answer():

    assert solutions.e001.solve(10) == 23
