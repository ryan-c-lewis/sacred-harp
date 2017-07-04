import unittest
import music21
import src.metrics.analyzer as analyzer


class TestMetrics(unittest.TestCase):
    def test_analyze_file_music(self):
        result = analyzer.analyze_file("lib\\books\\denson\\47b.xml")
        self.assertEqual(music21.key.Key('A', 'minor'), result.key)
        self.assertEqual(music21.pitch.Pitch('A2'), result.range.noteStart)
        self.assertEqual(music21.pitch.Pitch('G5'), result.range.noteEnd)
        self.assertEqual(4, len(result.parts))

    def test_analyze_file_metadata(self):
        result = analyzer.analyze_file("lib\\books\\denson\\167.xml")
        self.assertEqual('PRAY, BRETHREN, PRAY, 167', result.raw_title)
        self.assertEqual('167', result.page_number)
        self.assertEqual('PRAY, BRETHREN, PRAY', result.song_name)
        self.assertEqual('The Minstrel of Zion, 1845.', result.composer)

    def test_results_to_csv(self):
        results = analyzer.AnalyzerResultSet([
            analyzer.analyze_file("lib\\books\\denson\\124.xml"),
            analyzer.analyze_file("lib\\books\\denson\\47b.xml")
        ])
        csv = results.to_csv().split('\n')
        self.assertEqual('Page #,Song Name,Composer,Tonic,Mode,RangeStart,RangeEnd', csv[0].rstrip())
        self.assertEqual('047b,IDUMEA,"Ananias Davisson, 1816",A,minor,A2,G5', csv[1].rstrip())
        self.assertEqual('124,LOVER OF THE LORD,"Arr. - R. H. Reeves, 1869.",A,major,A2,A5', csv[2].rstrip())


if __name__ == '__main__':
    unittest.main()