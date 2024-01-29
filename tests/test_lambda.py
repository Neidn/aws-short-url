import os
from unittest import TestCase
from unittest.mock import patch, MagicMock


class TestLambda(TestCase):
    def test_lambda(self):
        self.assertEqual(1, 1)
