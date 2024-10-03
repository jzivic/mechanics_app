import unittest

import matplotlib.pyplot as plt
import numpy as np
from src import stage_3


class TestDiagramsForces(unittest.TestCase):
    load_dict = {
        "F1": {"type": "F", "value": 10, "position": 20},
        "F2": {"type": "F", "value": 15, "position": 25},
        "q1": {"type": "q", "value": 30, "position": (0, 50)},
        "q2": {"type": "q", "value": 35, "position": (50, 70)},
    }

    beam_geometry = {
        "length": [70]
    }

    def setUp(self):
        self.diag = stage_3.Diagrams_forces(self.load_dict, self.beam_geometry)

    def test_create_coordinates_f(self):
        result = self.diag.create_coordinates_f()

        self.assertIsInstance(result, dict)
        self.assertListEqual(result['z'], [0, 20, 25, 50, 70])
        self.assertListEqual(result['q'], [0, 10, 25, 55, 90])

    def test_plot_graph(self):
        plt.switch_backend('Agg')
        fg = plt.figure()
        ax = fg.add_subplot(111)
        lines = ax.plot(range(10))

        self.diag.plot_graph()

        self.assertIsInstance(ax.lines[0], plt.Line2D)


if __name__ == '__main__':
    unittest.main()
