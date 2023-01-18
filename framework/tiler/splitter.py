from PIL import Image
import numpy as np

class ImageSplitter:
    """Image Spliiter Class for splitting an image into tiles"""
    def __init__(self, image: dict, zoom: int, tileSize: tuple):
        self.image = image
        self.zoom = zoom
        self.tileSize = tileSize

        # Class Function Calls
        self.generateXYGrid()

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
        self.gridXY = np.array([[(x,y) for x in range(self.gridSize)] for y in range(self.gridSize)])
        return None

    def split(self):
        """Split the input image method"""
        image_data = np.asarray(self.image)

    def quadKey(self, tileX, tileY):
        """Generate a single quad key from x,y coordinate
        Args:
            tileX: tile X
            tileY: tile Y
        Returns:
            quad key in the form of a string
        """
        # Convert tileX & tileY to binary
        toBin = lambda v: bin(v)[2:].zfill(self.zoom)
        tx, ty = toBin(tileX), toBin(tileY)
        qk = []
        for idx, lvl in enumerate(reversed(range(1, self.zoom + 1))):
            key_mask = 1 << (lvl - 1)
            tmp_key = 0
            if key_mask != 0:
                if tx[idx] != '0':
                    tmp_key += 1
                if ty[idx] != '0':
                    tmp_key += 2
            qk.append(str(tmp_key))
        return ''.join(qk)
    
    # Property Methods
    @property
    def gridSize(self):
        """Get the size of the grid in XY"""
        return int(2**self.zoom)

    @property
    def nTiles(self):
        """Get the total number of tiles for this zoom level"""
        return int(self.gridSize**2)
    
