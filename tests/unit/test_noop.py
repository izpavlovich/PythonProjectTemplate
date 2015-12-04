from tests.unit import test


class NoopTestCase(test.TestCase):
    """Probe unit test"""

    def test_noop(self):
        self.assertEqual(4, 2 + 2)
