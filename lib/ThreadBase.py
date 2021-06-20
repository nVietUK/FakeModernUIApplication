class setup:
    def __init__(self, trigger) -> None:
        self.run = True
        self.trigger = trigger
        self.alive = False
    def shoot(self):
        self.alive = True
    def is_alive(self):
        return self.alive
    def shut(self):
        self.run = False
    def main(self, definition, *arg):
        while self.run:
            if self.trigger or self.alive:
                definition(*arg)
                self.alive = False
import threading
class storage:
    def __init__(self, definition, trigger, *arg) -> None:
        self.cmd = setup(trigger)
        self.core = threading.Thread(target= self.cmd.main, args= (definition, *arg,))