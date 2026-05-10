class App:
    def __init__(self, name: str, windows: list[Window]):
        self.name = name
        self.windows = windows
    def open(self):
        print(f"Opening {self.name} with {self.windows} windows")
    def save(self):
        print(f"Saving {self.name} with {self.windows} windows")
    def move(self, x, y):
        print(f"Moving {self.name} to ({x}, {y})")
    def close(self):
        print(f"Closing {self.name}")
        