"""Used in testing."""

import sys

prompt = input("Accept? (y/n): ")
print(f"ok - {prompt}")
sys.exit(0 if prompt == "y" else 1)
