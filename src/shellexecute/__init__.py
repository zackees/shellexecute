"""
Shared utility functions
"""

# pylint: disable=consider-using-with,global-statement,too-many-arguments,too-many-locals,fixme,too-many-statements,chained-comparison

import subprocess
import sys
from typing import Optional
from colorama import just_fix_windows_console  # type: ignore

if sys.platform == "win32":
    from wexpect import spawn, EOF  # type: ignore # pylint: disable=import-error
else:
    from pexpect import spawn, EOF  # type: ignore # pylint: disable=import-error


just_fix_windows_console()  # Fixes color breakages in win32


def execute(
    command,
    cwd=None,
    send_confirmation: Optional[list[tuple[str, str]]] = None,
    ignore_errors=False,
    timeout=None,
    encoding="utf-8",
    outstream=None,
) -> int:
    """Execute a command"""

    out = ""
    out += "####################################\n"
    out += f"Executing\n  {command}\n"
    if cwd:
        out += f"  CWD={cwd}\n"
    out += "####################################\n"

    sys.stdout.write(out)
    sys.stdout.flush()

    if send_confirmation is None:
        completed_process = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            check=not ignore_errors,
            timeout=timeout,
            encoding=encoding,
        )
        return completed_process.returncode
    # temporary buffer for stderr
    child = spawn(command, cwd=cwd, encoding=encoding, timeout=timeout)
    child.logfile = outstream or sys.stdout
    eof_reached = False
    for expect, answer in send_confirmation:
        which = child.expect_exact([expect, EOF], timeout=timeout)
        if which == 1:
            eof_reached = True
            break  # EOF
        child.sendline(answer)
    if not eof_reached:
        child.expect(EOF)
    if sys.platform != "win32":
        child.close()
    else:
        child.wait()
    if child.exitstatus != 0 and not ignore_errors:
        raise RuntimeError("Command failed: " + command)
    return child.exitstatus
