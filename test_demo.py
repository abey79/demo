# Basic test file. Is automatically found by pytest thanks to its name starting with "test_". All functions starting
# with "test_" are automatically discovered and run by pytest.
#
# More complex project would have many `test_XXX.py` files in a `tests/` directory.

from demo import add


def test_add():
    assert add(1, 2) == 3
