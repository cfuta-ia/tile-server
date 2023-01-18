from PIL import Image
import numpy as np
from fractions import Fraction
from framework.tiler.splitter import ImageSplitter
from framework.tiler.projection import CoordinateSystem
from framework.tiler.img import TileImage
from framework.util.tablify import printTable
from typing import Type

class TileServer:
    """Tile server image splitter"""
    def __init__(self, image: dict, projection: dict, server: dict):
        self.config = {'image': image, 'projecttion': projection, 'server': server}
        self.tile_image = TileImage(**image)
        self.coordinate_system = CoordinateSystem(**projection)



class ImageTiler:
    """Image Tiler Class"""
    def __init__(self, imagePath: str, directory: str, minZoom=0, maxZoom=18, reshapeTileSize=True, coordinateSystem={}):
        self.tiles = (256.0, 256.0)
        self.zoom = (minZoom, maxZoom)
        self.coordinates = CoordinateSystem(datum=coordinateSystem)

        # Initialization Function Calls
        self.setImage(imagePath, directory)
        self.setTileSize(reshapeTileSize)
        

    def splitImage(self):
        """Split Image Function"""
        pass

    # Setter Methods
    def setImage(self, imagePath, directory):
        """Convert image data in numpy array and set as the data property in the class image dict"""
        self.image = {'path': imagePath, 'image': Image.open(imagePath),}
        self.image['data'] = np.asarray(self.image.get('image'), [])
        self.image['directory'] = directory
        return None

    def setTileSize(self, reshapeTileSize):
        """Set the default tile size for the image"""
        if reshapeTileSize:
            self.tiles = (256.0, (self.getImageScale()*256).__float__())
        return None

    # Getter Methods
    def __imageDimensions(self):
        """Convenience methods to return the numpy image array shape (height, width)"""
        return self.image.get('data').shape

    def getImageDescription(self):
        """Get the image dimensions for the class image path"""
        dimensions = self.__imageDimensions()
        headers = ['Height (px)', 'Width (px)', 'Scale', 'Tile Size']
        data = [[dimensions[0], dimensions[1], '{:.2f}'.format(self.getImageScale().__float__()), "{:.0f}x{:.0f}".format(*self.tiles)]]
        printTable(headers, data, includeStatement=False)
        return None

    def getImageHeight(self):
        """Get the image height (in pixels)"""
        height = self.__imageDimensions()[0]
        return height

    def getImageWidth(self):
        """Get the image width (in pixels)"""
        width = self.__imageDimensions()[1]
        return width

    def getImageScale(self):
        """Get the image scale (width/height)"""
        dimensions = self.__imageDimensions()
        scale = Fraction(*dimensions[::-1][-2:])
        return scale

    def getTileSize(self):
        """Get the image tile size that it is split into"""
        return self.tiles.get('size', (256.0, 256.0))