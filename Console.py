import win32console

class Console(Window):
    class CmdTab(Tab):
        def __init__(self, tab_id, command):
            super().__init__(tab_id)
            self.command = command
            self.text = ""
        def run(self):
            print(f"Running command {self.command} in tab {self.tab_id}")
            self.text = f"Output of {self.command}"
    def __init__(self, name: str, tabs: list[CmdTab], length: int, width: int, x: int, y: int, origin: str):
        super().__init__(name, tabs, length, width, x, y, origin)
