from uuid import uuid1


class MenuItem:
    def __init__(self, label, selected=False):
        self.id = str(uuid1())
        self.label = label
        self.selected = selected

    def __eq__(self, other):
        return self.id == other.id
