import os
import numpy as np
from PIL import Image
from fractions import Fraction
from framework.tiler.file_writer import Writer

class TileImage:
    """Tile Image class to be used by the imiage tiler"""
    _tileSize = (256.0, 256.0)
    def __init__(self, imagePath, directory):
        self.path = imagePath
        self.directory = self.makeValidDirectory(directory)
        with Image.open(imagePath) as img:
            self.data = np.asarray(self.img)
    
    # Functions
    def createRootDirectory(self):
        """ """
        Writer.createDirectory(self.directory)
        return None

    def createConfigDirectory(self, config):
        """ """
        pass

    # Static Methods
    @staticmethod
    def makeValidDirectory(value: str):
        """Convert incoming value into a valid directory name format
        
        Args:
            value: incoming string value
        Returns:
            formatted string
        """
        return value.lower().replace(' ', '-')

    