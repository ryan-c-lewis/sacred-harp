import analyzer
import music21
import unittest


class TestMetrics(unittest.TestCase):
    def test_analyze_file_music(self):
        result = analyzer.analyze_file("..\\..\\books\\denson\\47b.xml")
        self.assertEqual(music21.key.Key('A', 'minor'), result.key)
        self.assertEqual(music21.pitch.Pitch('A2'), result.range.noteStart)
        self.assertEqual(music21.pitch.Pitch('G5'), result.range.noteEnd)
        self.assertEqual(4, len(result.parts))

    def test_analyze_file_metadata(self):
        result = analyzer.analyze_file("..\\..\\books\\denson\\124.xml")
        self.assertEqual('LOVER OF THE LORD, 124', result.title)
        self.assertEqual('Arr. - R. H. Reeves, 1869.', result.composer)

    def test_results_to_csv(self):
        results = analyzer.AnalyzerResultSet([
            analyzer.analyze_file("..\\..\\books\\denson\\47b.xml"),
            analyzer.analyze_file("..\\..\\books\\denson\\124.xml")
        ])
        csv = results.to_csv().split('\n')
        self.assertEqual('Title,Composer,Tonic,Mode,RangeStart,RangeEnd', csv[0].rstrip())
        self.assertEqual('"IDUMEA, 47b","Ananias Davisson, 1816",A,minor,A2,G5', csv[1].rstrip())
        self.assertEqual('"LOVER OF THE LORD, 124","Arr. - R. H. Reeves, 1869.",A,major,A2,A5', csv[2].rstrip())


if __name__ == '__main__':
    unittest.main()