import logging
import sys
import src.metrics.analyzer as analyzer

logLevel = logging.INFO
output_file = 'out\\analysis.csv'


def main(directory_path):
    result_set = analyzer.analyze_directory(directory_path)
    analyzer.write_to_csv(result_set, output_file)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: Pass a directory containing MusicXML files to analyze")
        exit()
    logging.basicConfig(stream=sys.stderr, level=logLevel)
    main(sys.argv[1])
