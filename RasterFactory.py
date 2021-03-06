import matplotlib.pyplot as plt
import numpy as np
import math
from pprint import pprint


class RasterFactory:
    """
    Class used to raster a line onto a matrix and display it
    """

    # keeping old values
    oX1 = 0
    oX2 = 0
    oY1 = 0
    oY2 = 0

    # values used for iteration
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    dX = dY = 0
    b = 0
    m = 0

    matrix = None
    resolution = 0
    resolutions = [
        (64, 48),
        (128, 96),
        (320, 240),
        (720, 480),
        (1024, 768),
        (1366, 768),
        (1920, 1080),
        (3840, 2160),
    ]

    def __repr__(self):
        return "RasterFactory X({}, {}) Y({}, {}) ({})".format(
            self.x1, self.x2, self.y1, self.y2, self.resolutions[self.resolution]
        )

    def set_resolution(self, resolution: int):
        """
        Set resolution that will be used by the factory, and guarantee that matrix is None
        :param resolution: integer representing which resolution set should be used
        """
        try:
            self.resolution = resolution

        except IndexError as e:
            print(
                "Resolução não cadastrada, definindo para {}".format(
                    self.resolutions[0]
                )
            )
            self.resolution = 0

    def set_values(self, x1: float, y1: float, x2: float, y2: float):
        """
        Set coordinates of line
        :param x1: x1 of line
        :param y1: y1 of line
        :param x2: x2 of line
        :param y2: y2 of line
        :return:
        """

        self.oX1 = abs(x1)
        self.oX2 = abs(x2)
        self.oY1 = abs(y1)
        self.oY2 = abs(y2)

    def __preload(self) -> bool:
        """
        Do preload of matrix and calculate constants
        :return:  boolean that indicates if there was not errors
        """

        # TODO: validations should return False

        self.__scale()
        self.matrix = np.zeros(self.resolutions[self.resolution])

        self.dX = self.x2 - self.x1
        self.dY = self.y2 - self.y1

        # if dX or dY is zero, m = 0, else m = dY/dX
        self.m = self.dY / self.dX if self.dX else 0
        self.b = self.y1 - (self.m * self.x1)

        return True

    def add_line(self):
        """
        Display matrix using pyplot
        :return:
        """
        matrix = self.matrix
        if matrix is not None:
            plt.imshow(matrix.T, cmap=plt.cm.gray, origin="lower")
            # plt.show()

    @staticmethod
    def show():
        """
        Display pyplot graph
        """
        plt.show()

    def raster(self):
        """
        raster a line into a matrix
        :return:
        """
        if not self.__preload():
            print("Não foi possivel realizar a rasterização")

        if abs(self.dX) > abs(self.dY):
            xi, xf = sorted((self.x1, self.x2))

            while xi < xf:
                yi = int(round(self.m * xi + self.b))
                self.__draw_point(xi, yi)
                xi += 1
        else:
            yi, yf = sorted((self.y1, self.y2))

            while yi < yf:
                try:
                    xi = int(round((yi - self.b) / self.m))
                except ZeroDivisionError:
                    xi = self.x1

                self.__draw_point(xi, yi)
                yi += 1

    def __scale(self):
        """
        scale the line to the chosen resolution
        :return:

        """

        self.x1, self.y1 = (
            self.oX1 * self.resolutions[self.resolution][0],
            self.oY1 * self.resolutions[self.resolution][1],
        )
        self.x2, self.y2 = (
            self.oX2 * self.resolutions[self.resolution][0],
            self.oY2 * self.resolutions[self.resolution][1],
        )

    def __draw_point(self, x: float, y: float):
        """
        Write a point on the matrix
        :param x: index x
        :param y: index y
        :return:
        """
        self.matrix[math.floor(x)][math.floor(y)] = 1


if __name__ == "__main__":
    raster = RasterFactory()


    # # set 1, m=positive
    # raster.set_values(
    #     x1=0.2,
    #     y1=0.4,
    #     x2=0.8,
    #     y2=0.6,
    # )

    # set 2, m=negative
    raster.set_values(
        x1=0.2,
        y1=0.4,
        x2=0.8,
        y2=0.2,
    )

    # # set 3, m=undefined
    # raster.set_values(
    #     x1=0.2,
    #     y1=0.05,
    #     x2=0.2,
    #     y2=0.9,
    # )


    # # set 4, m=0
    # raster.set_values(
    #     x1=0.2,
    #     y1=0.05,
    #     x2=0.9,
    #     y2=0.05,
    # )

    raster.set_resolution(resolution=2)
    raster.raster()
    raster.add_line()

    raster.show()
