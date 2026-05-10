import pychrome

class BrowserWindow:
    class BrowserTab(Tab):
        def __init__(self, tab_id, url):
            super().__init__(tab_id)
            self.url = url
            
    def __init__(self, name: str, tabs: list[BrowserTab], length: int, width: int, x: int, y: int, origin: str):
        super().__init__(name, tabs, length, width, x, y, origin)
