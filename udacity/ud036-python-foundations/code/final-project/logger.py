class Logger():
    """Generates messages to be logged to stdout with ASCII colors."""
    
    OK = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    
    def ok(self, message):
        return self.OK + message + self.END    
    
    def warn(self, message):
        return self.WARN + message + self.END
    
    def fail(self, message):
        return self.FAIL + message + self.END