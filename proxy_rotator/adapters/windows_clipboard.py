from __future__ import annotations

import subprocess
import sys


class WindowsClipboardAdapter:
    """Copy text to the Windows clipboard via clip.exe."""

    def copy(self, text: str) -> bool:
        if sys.platform != "win32":
            return False
        try:
            subprocess.run("clip", input=text.encode("utf-16-le"), check=True, shell=True)
            return True
        except subprocess.SubprocessError:
            return False