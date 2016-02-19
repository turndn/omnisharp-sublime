import sublime
import sys
import os
import math
from unittest import TestCase

# module naming is different in ci than in sublime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib import omnisharp

done = False


def busywork():
    for x in range(0, 10):
        i = math.factorial(x)
    print("Busyworking...")

    return True

def cb(results):
    print(results)
    global done
    done = results
    print("Done!")


class test_omnisharp(TestCase):
    def test_execute_command(self):
        omnisharp.execute_command(busywork, cb)

        while not done:
            pass

        self.assertEqual(True, done)
