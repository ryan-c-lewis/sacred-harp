import unittest
import music21
from src.shapenotesong import ShapeNoteSong


class TestShapeNoteSong(unittest.TestCase):
    def assert_47b_loaded_correctly(self, song):
        self.assertEqual(music21.key.Key('A', 'minor'), song.key)
        self.assertEqual(music21.pitch.Pitch('A2'), song.range.noteStart)
        self.assertEqual(music21.pitch.Pitch('G5'), song.range.noteEnd)
        self.assertEqual(4, len(song.parts))

    def test_load_music_info(self):
        result = ShapeNoteSong.from_file_path("..\\lib\\books\\denson\\47b.xml")
        self.assert_47b_loaded_correctly(result)

    def test_output_to_xml(self):
        out_to_xml = ShapeNoteSong.from_file_path("..\\lib\\books\\denson\\47b.xml").to_musicxml()
        # I can't think of a good way to test the output except to make sure we can read it back in correctly...
        from_xml = ShapeNoteSong.from_xml(out_to_xml)
        self.assert_47b_loaded_correctly(from_xml)

    def test_load_metadata(self):
        result = ShapeNoteSong.from_file_path("..\\lib\\books\\denson\\167.xml")
        self.assertEqual('PRAY, BRETHREN, PRAY, 167', result.raw_title)
        self.assertEqual('167', result.page_number)
        self.assertEqual('PRAY, BRETHREN, PRAY', result.song_name)
        self.assertEqual('The Minstrel of Zion, 1845.', result.composer)

if __name__ == '__main__':
    unittest.main()
