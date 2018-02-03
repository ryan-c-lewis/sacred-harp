import csv
import io
import logging
import os
from src.shapenotesong import ShapeNoteSong


class MetricsGeneral:
    @classmethod
    def from_directory(cls, directory_path, max_num_files=0):
        logging.info("Analyzing files at: " + directory_path)
        file_names = os.listdir(directory_path)
        file_paths = []
        if max_num_files > 0:
            file_names = file_names[:max_num_files]
        for file_name in file_names:
            file_path = os.path.join(directory_path, file_name)
            file_paths.append(file_path)
        return cls.from_files(file_paths)

    @classmethod
    def from_file(cls, file_path):
        logging.info("Analyzing file: " + file_path)
        song = ShapeNoteSong.from_file_path(file_path)
        return cls([song])

    @classmethod
    def from_files(cls, file_paths):
        logging.info("Analyzing files: " + ",".join(file_paths))
        songs = []
        for file_path in file_paths:
            song = ShapeNoteSong.from_file_path(file_path)
            songs.append(song)
        return cls(songs)

    def __init__(self, songs):
        self.songs = songs

    def gather_metrics(self):
        metrics = []
        for result in sorted(self.songs, key=lambda x: x.page_number):
            metrics.append({
                'Page #': result.page_number,
                'Song Name': result.song_name,
                'Composer': result.composer,
                'Tonic': result.key.tonic,
                'Mode': result.key.mode,
                'RangeStart': result.range.noteStart,
                'RangeEnd': result.range.noteEnd
            })
        return metrics

    def to_file(self, file_path):
        logging.info("Writing results to file: " + file_path)
        with open(file_path, "w", newline="") as file:
            file.write(self.to_csv())

    def to_csv(self):
        logging.debug("Converting metrics to CSV")
        metrics = self.gather_metrics()
        output = io.StringIO()
        writer = csv.DictWriter(output, metrics[0].keys())
        writer.writeheader()
        writer.writerows(metrics)
        return output.getvalue()
