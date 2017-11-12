import logging
import sys
from src.metrics.metrics import Metrics

logLevel = logging.INFO
output_file = 'out\\analysis.csv'


def main(directory_path):
    logging.info("Gathering metrics for directory: " + directory_path)
    metric_gatherer = Metrics.from_directory(directory_path)
    logging.info("Writing results to file: " + output_file)
    with open(output_file, "w") as file:
        file.write(metric_gatherer.to_csv())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: Pass a directory containing MusicXML files to analyze")
        exit()
    logging.basicConfig(stream=sys.stderr, level=logLevel)
    main(sys.argv[1])
