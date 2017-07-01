import metrics
import music21
import unittest


class TestMetrics(unittest.TestCase):
    def test_analyze_file(self):
        result = metrics.analyze_file("..\\..\\books\\denson\\47b.xml")
        self.assertEqual(music21.key.Key('A', 'minor'), result['key'])
        self.assertEqual(music21.pitch.Pitch('A2'), result['range'].noteStart)
        self.assertEqual(music21.pitch.Pitch('G5'), result['range'].noteEnd)


if __name__ == '__main__':
    unittest.main()