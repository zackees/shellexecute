"""
Test pyflutterinstall
"""

import unittest
import os
import sys
from threading import Thread, Event

from shellexecute import execute

HERE = os.path.abspath(os.path.dirname(__file__))
ACCEPT_PY = os.path.join(HERE, "accept.py")


class FakeStream:
    """Fake input stream."""

    def __init__(self) -> None:
        self.buffer = ""

    def write(self, data: str) -> None:
        """Writes to the buffer."""
        self.buffer += data
        sys.stdout.write(data)

    def flush(self) -> None:
        """Flushes the buffer."""
        sys.stdout.flush()


class ExecuteTester(unittest.TestCase):
    """Tests pyflutterinstall"""

    def test_platform_executable(self) -> None:
        """Tests the platform executable"""

        event = Event()

        def kill():
            if not event.wait(5):
                print("ERROR TIMEOUT")
                os.kill(os.getpid(), 9)

        Thread(target=kill, daemon=True).start()
        fake_stream = FakeStream()

        rtn = execute(
            f"python {ACCEPT_PY}",
            send_confirmation=[("Accept? (y/n): ", "y")],
            timeout=5,
            outstream=fake_stream,
        )
        event.set()
        if sys.platform != "win32":
            self.assertIn("ok - y", fake_stream.buffer)
        self.assertEqual(rtn, 0)


if __name__ == "__main__":
    unittest.main()
