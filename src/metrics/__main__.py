import logging
import sys
from src.metrics.metrics_general import MetricsGeneral
from src.metrics.metrics_notes import MetricsNotes

logLevel = logging.INFO

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: Pass a directory containing MusicXML files to analyze")
        exit()
    logging.basicConfig(stream=sys.stderr, level=logLevel)
    MetricsGeneral.from_directory(sys.argv[1]).to_file('out\\metrics_general.csv')
    MetricsNotes.from_directory(sys.argv[1]).to_file('out\\metrics_notes.csv')
