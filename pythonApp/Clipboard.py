class Clipboard(object):
    """description of class"""
    c = []
    def __init__ (self):
        self.c = "init content"
    def __del__ (self):
        self.c = None
    def add(self, content):
        self.c = content
        print("added content: %s" % self.c)
    def get(self):
        print("content: %s" % self.c)
        return self.c
