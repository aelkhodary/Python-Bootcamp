import unittest
import cap
class TestCap(unittest.TestCase):

    def test_one_world(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result , 'Python')

    def test_many_words(self):
        text = 'welcome python unit test learning'
        result = cap.cap_text(text)
        self.assertEqual(result , 'Welcome Python Unit Test Learning')
    
if __name__ == '__main__':
            unittest.main()
