import unittest
from random import randrange
import string


class Rack():
    def __init__(self):
        self.items = []

    def quick_sort(self, sort_list):
        if sort_list == []:
            return sort_list
        else:
            pivot = sort_list.pop(randrange(len(sort_list)))
            lesser = self.quick_sort([x for x in sort_list if x < pivot])
            greater = self.quick_sort([x for x in sort_list if x >= pivot])
            return lesser + [pivot] + greater

    def add(self, item):
        if isinstance(item, basestring):
            item = item.replace(' ', '').lower().translate(None,
                                                           string.punctuation)
            for each in item:
                self.items.append(each)
        else:
            self.items.append(item)
        self.items = self.quick_sort(self.items)

    def items_string(self):
        return ''.join(self.items)


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        rack = Rack()
        self.assertEqual([], rack.items)
        rack.add(20)
        self.assertEqual([20], rack.items)
        rack.add(10)
        self.assertEqual([10, 20], rack.items)
        rack.add(30)
        self.assertEqual([10, 20, 30], rack.items)
        rack.add(20)
        self.assertEqual([10, 20, 20, 30], rack.items)
        rack.add(5)
        self.assertEqual([5, 10, 20, 20, 30], rack.items)
        rack.add(2)
        self.assertEqual([2, 5, 10, 20, 20, 30], rack.items)

        rack = Rack()
        rack.add('When not studying nuclear physics, Bambi likes to play ' +
                 'beach volleyball')
        self.assertEqual('aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsss' +
                         'stttuuvwyyyy', rack.items_string())

if __name__ == '__main__':
    unittest.main()
