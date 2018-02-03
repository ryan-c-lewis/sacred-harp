import csv
import io
import logging
import os
from music21.note import Note
from src.shapenotesong import ShapeNoteSong

# TODO: Some outputs are shifted up an octave too high.
# Need to figure out how to tell when that's happening and shift them down.

# The output numbers are percentages of note duration for each half-step relative to the tonic.
# So if the song's tonic is C4 and 10 of 50 of the treble's quarter notes are an E4,
# then the number 4 (4th half-step above tonic) for the treble will be 0.20 (10 / 50)


class MetricsNotes:
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
        for song in sorted(self.songs, key=lambda x: x.page_number):
            song_metrics = SongNoteMetrics(song)
            for part_metrics in song_metrics.part_metrics:
                metric_output = {
                    'Song': song.page_number,
                    'Part': part_metrics.part.partName,
                    'Average Pitch': part_metrics.average_pitch
                }
                for midi in range(-20, 21):
                    if midi in part_metrics.note_duration_percents.keys():
                        metric_output[midi] = part_metrics.note_duration_percents[midi]
                    else:
                        metric_output[midi] = 0
                metrics.append(metric_output)
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


class SongNoteMetrics:
    def __init__(self, song):
        self.song = song
        self.part_metrics = []
        for part in song.parts:
            self.part_metrics.append(PartNoteMetrics(part, song.key.tonic.midi))

        # All of the songs need to have either the bass part moved up an octave or the other parts moved down an octave
        # I'm not sure *why* this is, but this seems like a good heuristic for figuring out which one.
        tenor_average = next(metrics for metrics in self.part_metrics if metrics.part.partName.lower() == "tenor").average_pitch
        if tenor_average < 12:
            bass_part_metrics = \
                next(metrics for metrics in self.part_metrics if metrics.part.partName.lower() == "bass")
            for key in reversed(sorted(bass_part_metrics.note_duration_percents.keys())):
                bass_part_metrics.note_duration_percents[key + 12] = bass_part_metrics.note_duration_percents.pop(key)
            bass_part_metrics.average_pitch = round(bass_part_metrics.average_pitch + 12, 2)

        else:
            non_bass_part_metrics = \
                [metrics for metrics in self.part_metrics if metrics.part.partName.lower() != "bass"]
            for part_metrics in non_bass_part_metrics:
                for key in sorted(part_metrics.note_duration_percents.keys()):
                    part_metrics.note_duration_percents[key - 12] = part_metrics.note_duration_percents.pop(key)
                part_metrics.average_pitch = round(part_metrics.average_pitch - 12, 2)


class PartNoteMetrics:
    def __init__(self, part, tonic_midi):
        self.part = part
        notes = [note for note in part.flat.elements if isinstance(note, Note)]
        note_duration_quarters = {}
        for note in notes:
            half_step = note.pitch.midi - tonic_midi
            duration = note.duration.quarterLength
            if half_step in note_duration_quarters:
                note_duration_quarters[half_step] += duration
            else:
                note_duration_quarters[half_step] = duration
        total_duration = sum(note_duration_quarters.values())
        self.note_duration_percents = {key: note_duration_quarters[key] / total_duration for key in
                                       note_duration_quarters.keys()}
        self.average_pitch = 0
        for pitch in self.note_duration_percents.keys():
            self.average_pitch += pitch * self.note_duration_percents[pitch]
        self.average_pitch = round(self.average_pitch, 2)
