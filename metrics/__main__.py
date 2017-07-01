import sys
import metrics


def main(directory_path):
    print("Analyzing files at: " + directory_path)
    metrics.analyze_directory(directory_path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: Pass a directory containing MusicXML files to analyze")
        exit()
    main(sys.argv[1])
