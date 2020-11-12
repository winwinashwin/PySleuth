class Signal(object):
    def __init__(self, *types):
        self._call_types = types
        self._connections = set()

    def connect(self, objPtr, methodName):
        self._connections.add((objPtr, methodName))

    def emit(self, *args):
        if len(args) != len(self._call_types):
            raise ValueError("Invalid Args, must be %s" % self._call_types)

        for i, arg in enumerate(args):
            if isinstance(arg, self._call_types[i]):
                continue

            raise ValueError(
                f"Invalid Arg {arg}, must be {self._call_types[i]}"
            )

        for objPtr, methodName in self._connections:

            cbl = getattr(objPtr, methodName)

            if cbl:
                cbl(*args)
