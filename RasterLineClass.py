import matplotlib as mpl
import numpy as np

from pprint import pprint

class RasterLine():
    size = 0
    def __init__(self, size: int):
        """

        :param size: matriz size
        """
        self.size = size

    @staticmethod
    def show_line(matrix):
        pprint(matrix)
    def raster(self):
        """

        :return: raster a line into a matrix
        """
    def scale(self, x, y):
        """
        :param x:
        :param y:
        :return:
            rescale the line
        """