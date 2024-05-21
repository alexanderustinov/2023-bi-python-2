from typing import ContextManager


class MyManager(ContextManager):
    def __init__(self):
        self.data = 42

    def __enter__(self):
        print("entering")
        return self

    def __exit__(self, *exc):
        print("finished")
        # print(*exc, sep='|')


with MyManager() as m:
    print(m.data, type(m))
    raise RuntimeError("achtung")
