class setup:
    def __init__(self) -> None:
        self.run = True
        self.trigger = False
        self.alive = False
    def shoot(self):
        self.trigger = True
    def is_alive(self):
        return self.alive
    def shut(self):
        self.run = False
    def main(self, definition):
        while self.run:
            if self.trigger:
                self.alive = True
                definition()
                self.trigger = False; self.alive = False
import threading
class storage:
    def __init__(self, definition) -> None:
        self.cmd = setup()
        self.core = threading.Thread(target= self.cmd.main, args= (definition,))