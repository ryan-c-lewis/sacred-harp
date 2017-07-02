import csv
import io
import logging
import music21
import os


def analyze_directory(directory_path, max_num = 0):
    logging.info("Analyzing files at: " + directory_path)
    file_names = os.listdir(directory_path)
    results = []
    if max_num > 0:
        file_names = file_names[:max_num]
    for file_name in file_names:
        file_path = os.path.join(directory_path, file_name)
        result = analyze_file(file_path)
        results.append(result)
    return AnalyzerResultSet(results)


def analyze_file(file_path):
    logging.info("Analyzing file: " + file_path)
    score = music21.converter.parse(file_path)
    return AnalyzerResult(score)


def write_to_csv(result_set, file_path):
    logging.info("Writing results to file: " + file_path)
    with open(file_path, "w") as file:
        file.write(result_set.to_csv())


class AnalyzerResult:
    def __init__(self, score):
        logging.debug("Creating AnalyzerResult out of score: " + str(score))
        self.score = score
        self.title = score.metadata.title
        self.composer = score.metadata.composer
        self.key = score.analyze('key')
        self.range = score.analyze('range')
        self.parts = list(score.parts)


class AnalyzerResultSet:
    def __init__(self, results):
        logging.debug("Creating ResultSet out of " + str(len(results)) + " results")
        self.results = results

    def get_pretty_results(self):
        pretty_results = []
        for result in self.results:
            pretty_results.append({
                'Title': result.title,
                'Composer': result.composer,
                'Tonic': result.key.tonic,
                'Mode': result.key.mode,
                'RangeStart': result.range.noteStart,
                'RangeEnd': result.range.noteEnd
            })
        return pretty_results

    def to_csv(self):
        logging.debug("Converting AnalyzerResultSet to CSV")
        pretty_results = self.get_pretty_results()
        output = io.StringIO()
        writer = csv.DictWriter(output, pretty_results[0].keys())
        writer.writeheader()
        writer.writerows(pretty_results)
        return output.getvalue()