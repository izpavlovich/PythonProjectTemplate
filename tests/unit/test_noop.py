from tests.unit import test


class NoopTestCase(test.TestCase):
    """Test case base class for all unit tests."""

    def test_noop(self):
        self.assertEqual(4, 2 + 2)

    def test_noop1(self):
        self.assertEqual(2, 1 + 1)

    def test_noop2(self):
        self.assertIsNot(2, 31)
