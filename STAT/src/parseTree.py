class Data:
    def __init__(self, name, type):
        self.name = name
        # 0 for name and nonzero for number
        self.dataType = type


class Function:
    def __init__(self, type, left, right, op, data):
        # 0 for two children, 1 for a single child, and 2 for a data value
        self.type = type
        self.left = left
        self.right = right
        self.op = op
        self.data = data
