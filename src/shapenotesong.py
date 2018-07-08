import logging
import music21
from music21.musicxml import m21ToXml


class ShapeNoteSong:
    @classmethod
    def from_file_path(cls, file_path):
        logging.debug("Loading file: " + file_path)
        score = music21.converter.parse(file_path)
        return cls(score)

    @classmethod
    def from_xml(cls, xml):
        logging.debug("Loading xml: " + xml)
        score = music21.converter.parseData(xml)
        return cls(score)

    def __init__(self, score):
        logging.debug("Creating ShapeNoteSong from music21 score: " + str(score))
        self.score = score
        self.raw_title = score.metadata.title
        self.composer = score.metadata.composer
        self.key = score.analyze('key')
        self.range = score.analyze('range')
        self.parts = list(score.parts)

        # Assuming title format is "SONG NAME, PAGE #"
        self.song_name = self.raw_title[:self.raw_title.rfind(',')].strip()
        self.page_number = self.raw_title[self.raw_title.rfind(',')+1:].strip()
        # If page # is between 10 and 99, add a leading '0' so it's 3 digits
        if sum(c.isdigit() for c in self.page_number) == 2:
            self.page_number = '0' + self.page_number

    def to_score(self):
        # TEMPORARY. This only works as long as we don't change the ShapeNoteSong at all.
        return self.score

    def to_musicxml(self):
        return m21ToXml.GeneralObjectExporter(self.to_score()).parse().decode('utf-8')
