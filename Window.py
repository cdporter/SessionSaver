import pywin32

class Window:
    class Tab(ABCTab):
        def __init__(self, tab_id, url):
            self.tab_id = tab_id
            self.url = url
        def open(self):
            print(f"Opening tab {self.tab_id} with URL {self.url}")
        def save(self):
            print(f"Saving tab {self.tab_id} with URL {self.url}")
        def close(self):
            print(f"Closing tab {self.tab_id} with URL {self.url}")

    def __init__(self, window_id: str, tabs: list[Tab], length: int, width: int, x: int, y: int, origin: str):
        self.window_id = window_id
        self.tabs = tabs
        self.dimensions = (length, width, x, y, origin)
    def open(self):
        print(f"Opening window {self.window_id} with {self.tabs} tabs at {self.dimensions}")
    def save(self):
        print(f"Saving window {self.window_id} with {self.tabs} tabs at {self.dimensions}")
    def close(self):
        print(f"Closing window {self.window_id} with {self.tabs} tabs at {self.dimensions}")
    def move(self, x, y):
        self.dimensions = (self.dimensions[0], self.dimensions[1], x, y, self.dimensions[4])
        print(f"Moving window {self.window_id} to {self.dimensions}")
    def resize(self, length, width):
        self.dimensions = (length, width, self.dimensions[2], self.dimensions[3], self.dimensions[4])
        print(f"Resizing window {self.window_id} to {self.dimensions}")