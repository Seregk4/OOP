class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not hasattr(self, "logs"):
            self.logs = []

    def log(self, message : str):
        self.logs.append(message)
    
    def get_log(self):
        return self.logs

logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_log() == ["First message", "Second message"]
