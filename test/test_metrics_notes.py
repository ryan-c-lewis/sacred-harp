import unittest
from src.metrics.metrics_notes import MetricsNotes


class TestMetricsNotes(unittest.TestCase):
    def test_results_to_csv(self):
        metrics = MetricsNotes.from_files([
            "..\\lib\\books\\denson\\102a.xml",
            "..\\lib\\books\\denson\\117a.xml"
        ])
        csv = metrics.to_csv().replace("\r\n", "\n")
        self.assertEqual(csv,
                         """Song,Part,Average Pitch,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
102,treble,8.55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.025,0,0.0625,0,0.4375,0.0125,0,0.275,0,0.1875,0,0,0,0,0,0,0,0
102,alto,0.26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0625,0,0,0.1375,0,0.475,0,0.15,0.1625,0,0.0125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
102,tenor,4.39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.025,0,0.275,0,0.025,0.1,0,0.2,0,0.2375,0.0375,0,0.0375,0,0.0625,0,0,0,0,0,0,0,0
102,bass,-1.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0.025,0,0.15,0,0,0.2125,0,0.5625,0,0,0.05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
117,treble,5.84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.31,0,0.11,0,0.44,0.06,0,0.08,0,0,0,0,0,0,0,0,0,0
117,alto,0.28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.05,0.14,0.6,0,0.11,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
117,tenor,5.45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.17,0,0.12,0.13,0,0.1,0,0.26,0.02,0,0.07,0,0.09,0,0.04,0,0,0,0,0,0
117,bass,-0.46,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0,0,0.12,0,0.485,0,0,0.135,0,0.02,0,0.04,0,0,0,0,0,0,0,0,0,0,0,0,0
""")


if __name__ == '__main__':
    unittest.main()
