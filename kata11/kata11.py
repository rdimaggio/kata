import unittest
from random import randrange


class Rack():
    def __init__(self):
        self.balls = []

    def quick_sort(self, sort_list):
        if sort_list == []:
            return sort_list
        else:
            pivot = sort_list.pop(randrange(len(sort_list)))
            lesser = self.quick_sort([x for x in sort_list if x < pivot])
            greater = self.quick_sort([x for x in sort_list if x >= pivot])
            return lesser + [pivot] + greater

    def add(self, ball):
        self.balls.append(ball)
        self.balls = self.quick_sort(self.balls)


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        rack = Rack()
        self.assertEqual([], rack.balls)
        rack.add(20)
        self.assertEqual([20], rack.balls)
        rack.add(10)
        self.assertEqual([10, 20], rack.balls)
        rack.add(30)
        self.assertEqual([10, 20, 30], rack.balls)
        rack.add(20)
        self.assertEqual([10, 20, 20, 30], rack.balls)
        rack.add(5)
        self.assertEqual([5, 10, 20, 20, 30], rack.balls)
        rack.add(2)
        self.assertEqual([2, 5, 10, 20, 20, 30], rack.balls)


if __name__ == '__main__':
    unittest.main()
