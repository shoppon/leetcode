class FileSystem:

    def __init__(self):
        self.paths = {}
        self.values = {}

    def createPath(self, path: str, value: int) -> bool:
        if not path.startswith('/') or path.endswith('/'):
            return False
        dirs = path[1:].split('/')
        pre = self.paths
        for d in dirs[:-1]:
            cur = pre.get(d)
            if cur is None:
                return False
            pre = cur
        if pre.get(dirs[-1]) is not None:
            return False
        pre[dirs[-1]] = {}

        self.values[path] = value
        return True

    def get(self, path: str) -> int:
        return self.values.get(path, -1)
