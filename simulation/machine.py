class Pin:
    OUT = 1
    def __init__(self, name, mode):
        self.state = 0
    def toggle(self):
        self.state = 1- self.state
        print("LED ON" if self.state else "LED OFF")
