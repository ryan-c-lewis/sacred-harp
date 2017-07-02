import logging
import analyzer
import sys

logLevel = logging.INFO
output_file = 'output\\analysis.csv'


def main(directory_path):
    result_set = analyzer.analyze_directory(directory_path)
    analyzer.write_to_csv(result_set, output_file)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: Pass a directory containing MusicXML files to analyze")
        exit()
    logging.basicConfig(stream=sys.stderr, level=logLevel)
    main(sys.argv[1])
