from PIL import Image
import numpy as np

class ImageSplitter:
    """Image Spliiter Class for splitting an image into tiles"""
    def __init__(self, imagePath, zoom=1):
        self.image = Image.open(imagePath)
        self.image_data = np.asarray(self.image)
        self.zoom = zoom

    @property
    def num_tiles(self):
        """Calculate the number of tiles from the zoom property"""
        return self.zoom

    @property
    def imageSize(self):
        """Image Size Property"""
        return self.image_data.shape