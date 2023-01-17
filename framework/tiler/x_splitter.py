from PIL import Image
import numpy as np

class ImageSplitter:
    """Image Spliiter Class for splitting an image into tiles"""
    def __init__(self, image: dict, zoom):
        self.image = image
        self.zoom = zoom
        self.setTileQuantity()
        self.setGridSize()

    def getPixelCoordinateMap(self, zoom, tileSize):
        """Return the upper & lower pixel bounds based on the image and zoom
        
        Args:
            zoom: level of zoom to calculate the pixel bounds for
            tileSize: tile size tuple (height, width)
        Returns:
            list of tuple for the image bounds
        """
        upperBounds = tuple(b * 2**zoom - 1 for b  in tileSize)
        return [(0.0, 0.0), upperBounds]

    def generateQuadKeys(self):
        """Generate tile quad keys"""
        q_key = lambda x, y: f"{self.zoom}{x}{y}"
        rc = int(self.grid_size)
        keys = [[self.quadKey(x,y) for x in range(rc)] for y in range(rc)]
        return np.array(keys)

    def generateXYGrid(self):
        """Generate tile XY grid"""
        return np.array([[f"({x},{y})" for x in range(self.grid_size)] for y in range(self.grid_size)])

    def split(self):
        """Split the input image method"""
        image_data = np.asarray(self.image)

    def quadKey(self, x, y):
        """Generate a single quad key from x,y coordinate
        Args:
            x: tile X
            y: tile Y
        Returns:
            quad key in the form of a string
        """
        qk = []
        for i in reversed(range(1, self.zoom + 1)):
            key_mask = 1 << (i - 1)
            tmp_key = 0
            if key_mask != 0:
                if x != 0:
                    tmp_key += 1
                if y != 0:
                    tmp_key += 2
            qk.append(str(tmp_key))
        print(f"X: {x}, Y: {y}, QK: {qk}")
        return ''.join(qk)
    
    # Property Methods
    @property
    def imageSize(self):
        """Image Size Property"""
        return self.image_data.shape

    # Setter Methods
    def setTileQuantity(self):
        """Set the total number of tiles the image splitter should create"""
        self.tile_quantity = (4**self.zoom)

    def setGridSize(self):
        """Set the grid size as a singular value"""
        self.grid_size = int(2**self.zoom)
    