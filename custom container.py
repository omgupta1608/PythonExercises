class Tags:

    def __init__(self):
        self.tags = {}

    def __len__(self):
        return len(self.tags)

    def __getitem__(self, tag):
        return (self.tags[tag.lower()])

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

t = Tags()
t.add("python")
t.add("python")
t.add("Python")

print(t.tags)