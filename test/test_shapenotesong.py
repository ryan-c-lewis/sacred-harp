import unittest
import music21
from src.shapenotesong import ShapeNoteSong


class TestShapeNoteSong(unittest.TestCase):
    def test_load_music_info(self):
        result = ShapeNoteSong.from_file_path("..\\lib\\books\\denson\\47b.xml")
        self.assertEqual(music21.key.Key('A', 'minor'), result.key)
        self.assertEqual(music21.pitch.Pitch('A2'), result.range.noteStart)
        self.assertEqual(music21.pitch.Pitch('G5'), result.range.noteEnd)
        self.assertEqual(4, len(result.parts))

    def test_load_metadata(self):
        result = ShapeNoteSong.from_file_path("..\\lib\\books\\denson\\167.xml")
        self.assertEqual('PRAY, BRETHREN, PRAY, 167', result.raw_title)
        self.assertEqual('167', result.page_number)
        self.assertEqual('PRAY, BRETHREN, PRAY', result.song_name)
        self.assertEqual('The Minstrel of Zion, 1845.', result.composer)

if __name__ == '__main__':
    unittest.main()
