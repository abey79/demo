# NOTE: this is a single-file Python module. More complex project should be organized into a package structure, which
# would look like this:
#
# demo/
#   __init__.py (often empty for application)
#   __main__.py (this is executed when running `python -m demo`
#   demo.py (actual code)
#   ... (more actual code in other .py files)


def add(a, b):
    return a + b


def main():
    print(f"1 + 3 = {add(1, 3)}")


if __name__ == "__main__":
    main()
