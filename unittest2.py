import unittest

import full_name


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(full_name.full_name('Масюк', 'Александр', 'Николаевич'), 'Масюк Александр Николаевич')

    def test_big(self):
        self.assertEqual(full_name.full_name('МАСЮК', 'АЛЕКСАНДР', 'НИКОЛАЕВИЧ'), 'Масюк Александр Николаевич')

    def test_small(self):
        self.assertEqual(full_name.full_name('масюк', 'александр', 'николаевич'), 'Масюк Александр Николаевич')


if __name__ == '__main__':
    unittest.main()
