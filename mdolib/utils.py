"""Small helpers shared across chapters."""


class Counted:
    """Wrap a function to count evaluations: g = Counted(f); g(x); g.n."""
    def __init__(self, fun):
        self.fun, self.n = fun, 0
    def __call__(self, *args, **kwargs):
        self.n += 1
        return self.fun(*args, **kwargs)
