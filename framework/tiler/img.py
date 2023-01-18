import os
import numpy as np
from PIL import Image
from fractions import Fraction
from framework.tiler.file_writer import Writer
from framework.util.tablify import printTable

class TileImage:
    """Tile Image class to be used by the imiage tiler"""
    def __init__(self, imagePath: str, maintainAspectRatio: bool):
        self.path = imagePath
        self.name = os.path.split(self.path)[-1]
        self.size = [256.0, 256.0]
        self.setImage()

    # Setter Methods
    def setImage(self):
        """Set the image and corresponding properties for the image"""
        with Image.open(self.path) as img:
            self.data = np.asarray(img)

    def setTileSize(self,  maintainAspectRatio):
        """Resize the base tile size to preserve the image aspect ratio
        
        Args:
            maintainAspectRatio: image aspect ratio as the fraction class
        Returns:
            None
        """
        if maintainAspectRatio:
            aspectRatio = self.aspect_ratio
            if aspectRatio >= 1:
                self.size[1] = self.size[1]/aspectRatio
            elif aspectRatio < 1:
                self.size[1] = self.size[1]/aspectRatio
        return None

    # Properties
    @property
    def dimensions(self):
        """Get image dimensions (height, width)"""
        return self.data.shape[:2]

    @property
    def height(self):
        """Image height property"""
        return self.dimensions[0]

    @property
    def width(self):
        """Image width property"""
        return self.dimensions[1]

    @property
    def aspect_ratio(self):
        """Image aspect ratio"""
        return Fraction(*self.dimensions)

    @property
    def definition(self):
        """Print out the image definition"""
        printTable(['Width (px)', 'Height (px)', 'Aspect Ratio', 'Tile Size']
            , [[self.width, self.height, str(self.aspect_ratio), '{:.0f}x{:.0f}'.format(*self.size)]]
            , includeStatement=False)
        return None
    
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

    