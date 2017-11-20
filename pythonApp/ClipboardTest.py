import unittest
from Clipboard import Clipboard

class Test_ClipboardTest(unittest.TestCase):
    def setUp(self):
        self.clipboard = Clipboard()
    def tearDown(self):
        self.clipboard = None
    def test_clipboard_add(self):
        #Arrange
        content = "this is content"
        #Act
        self.clipboard.add(content)
        #Assert
        self.assertEqual(self.clipboard.c, content)
if __name__ == '__main__':
    unittest.main()
