import unittest
from src.metrics.metrics_general import MetricsGeneral


class TestMetrics(unittest.TestCase):
    def test_results_to_csv(self):
        metrics = MetricsGeneral.from_files([
            "..\\lib\\books\\denson\\124.xml",
            "..\\lib\\books\\denson\\47b.xml"
        ])
        csv = metrics.to_csv().split('\n')
        self.assertEqual('Page #,Song Name,Composer,Tonic,Mode,RangeStart,RangeEnd', csv[0].rstrip())
        self.assertEqual('047b,IDUMEA,"Ananias Davisson, 1816",A,minor,A2,G5', csv[1].rstrip())
        self.assertEqual('124,LOVER OF THE LORD,"Arr. - R. H. Reeves, 1869.",A,major,A2,A5', csv[2].rstrip())

if __name__ == '__main__':
    unittest.main()
