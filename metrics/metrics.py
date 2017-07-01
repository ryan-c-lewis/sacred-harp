import music21
import os


def analyze_directory(directory_path):
    file_names = os.listdir(directory_path)
    for file_name in file_names:
        file_path = os.path.join(directory_path, file_name)
        analyze_file(file_path)


def analyze_file(file_path):
    score = music21.converter.parse(file_path)
    results = {
        'key': score.analyze('key'),
        'range': score.analyze('range')
    }
    return results
