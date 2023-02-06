# shellexecute

[![Linting](../../actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)

[![MacOS_Tests](../../actions/workflows/push_macos.yml/badge.svg)](../../actions/workflows/push_macos.yml)
[![Ubuntu_Tests](../../actions/workflows/push_ubuntu.yml/badge.svg)](../../actions/workflows/push_ubuntu.yml)
[![Win_Tests](../../actions/workflows/push_win.yml/badge.svg)](../../actions/workflows/push_win.yml)

`pip install shellexecute`

```python
from shellexecute import execute
rtn = execute(
    f"echo HI",
    send_confirmation=[("HI", "y")],
)
```

Cross platform way to run shell commands using pexpect (wexpect on windows). VERY useful for installers where
you want to automate accepting prompts.

To develop software, run `. ./activate.sh`

# Windows

This environment requires you to use `git-bash`.

# Linting

Run `./lint.sh` to find linting errors using `pylint`, `flake8` and `mypy`.


# Versions
  * 1.0.4: Timeout is now set to None by default.