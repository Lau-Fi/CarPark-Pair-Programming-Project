class Park:
    maxNum = 3

    def __init__(self, name):
        self.name = name
        self.spaces = {}

    def __str__(self):
        return f"Car Park Name: {self.name}\nTotal Parking Spaces: {len(self.spaces)}"

    def add(self, spaces):
        for space in spaces:
            if space.startswith('e') and len(self.spaces) >= self.maxNum:
                raise MaxNumError("Maximum number of eLots reached.")
            self.spaces[space] = True

    def remove(self, space_id):
        if space_id in self.spaces:
            del self.spaces[space_id]
            return True
        return False


class MaxNumError(Exception):
    pass