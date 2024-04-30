# =============================================================================
# Python context managers - file context manager
# =============================================================================
#
# Sample for reading our file for the introduction
# (analog the open context manager).
#
# References:
# - https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager
# - https://www.pythontutorial.net/advanced-python/python-context-managers/
# =============================================================================

class File:
    def __init__(self, filename, mode):
        print("Create file context")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Run __enter__: Open file:", self.filename)
        self._file = open(self.filename, self.mode)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Run __exit__ : Close file:", self.filename)
        if not self._file.closed:
            self._file.close()
        return False


with File('data.txt', 'r') as f:
     print(int(next(f)))

# =============================================================================
# The end.
