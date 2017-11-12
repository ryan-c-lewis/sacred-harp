import logging
import music21


class ShapeNoteSong:
    @classmethod
    def from_file_path(cls, file_path):
        logging.info("Analyzing file: " + file_path)
        score = music21.converter.parse(file_path)
        return cls(score)

    def __init__(self, score):
        logging.debug("Creating AnalyzerResult out of score: " + str(score))
        self.score = score
        self.raw_title = score.metadata.title
        self.composer = score.metadata.composer
        self.key = score.analyze('key')
        self.range = score.analyze('range')
        self.parts = list(score.parts)

        # Assuming title format is "SONG NAME, PAGE #"
        self.song_name = self.raw_title[:self.raw_title.rfind(',')].strip()
        self.page_number = self.raw_title[self.raw_title.rfind(',')+1:].strip()
        if sum(c.isdigit() for c in self.page_number) == 2: # If page # is between 10 and 99
            self.page_number = '0' + self.page_number
