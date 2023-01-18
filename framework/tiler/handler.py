from framework.tiler.projection import CoordinateSystem
from framework.tiler.file_writer import Writer
from framework.tiler.img import TileImage
from framework.util.tablify import printTable
import json

class TileServer:
    """Tile server image splitter"""
    def __init__(self, image: dict, projection: dict, server: dict):
        self.config = {'image': image, 'projection': projection, 'server': server}
        self.tile_image = TileImage(**image)
        self.coordinate_system = CoordinateSystem(**projection)
        self.setServerProperties(server)

    # Setter Methods
    def setServerProperties(self, server):
        """Set the server properties from config dict
        
        Args:
            server: server config dict
        Returns:
            None
        """
        for key, value in server.items():
            setattr(self, key, value)
        return None

    def makeTiles(self):
        """Split image into tiles"""
        Writer.createDirectory(self.directory)
        Writer.createDirectory(self.directory, 'map')
        self.writeConfig()


    @property
    def definition(self):
        """Print out the server definition"""
        printTable(['Directory', 'Min Zoom', 'Max Zoom']
            , [[self.directory, self.minZoom, self.maxZoom]]
            , includeStatement=False)
        return None

    def writeConfig(self):
        """Write config.json file"""
        config = json.dumps(self.config, indent=4)
        Writer.createFile(config, self.directory, 'config.json')
        return None


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