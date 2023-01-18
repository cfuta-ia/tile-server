from framework.util.tablify import printTable

class CoordinateSystem:
    """Image Coordinate Projection Class"""
    _DATUMS = {'default': {'name': 'WGS-84', 'bounds': {'latitude': (-180.0, 180.0), 'longitude': (-85.05, 85.05)}}}
    def __init__(self, datum='default'):
        self.setDatum(datum)

    # Property
    @property
    def definition(self):
        """Print out the coordinate system definition"""
        printTable(['Name', 'Min Latitude', 'Max Latitude', 'Min Longitude', 'Max Longitude']
            , [[self.name, self.bounds.get('latitude')[0], self.bounds.get('latitude')[1], self.bounds.get('longitude')[0], self.bounds.get('longitude')[1]]]
            , includeStatement=False)
        return None

    # Setter Methods
    def setDatum(self, datum):
        """Set the coordinate system project datum
        
        Args:
            datum: datum dict to project onto the image, if None uses the _default class property
        Returns:
            None
        """
        datum = self._DATUMS.get(datum)
        self.name = datum.get('name', 'Unknown')
        self.bounds = datum.get('bounds', {'latitude': (0.0, 0.0), 'longitude': (0.0, 0.0)})
        return None

    # Getter Methods
    def getBounds(self, dir='all'):
        """Get the coordinate system datum bounds
        
        Args:
            dir: bound direction to get (latitude, longitude, all)
        Returns:
            dict of the datum bounds
        """
        dir = dir.lower()
        match dir:
            case 'all':
                bound = self.bounds
            case 'latitude' | 'longitude':
                bound = self.bounds.get(dir)
            case _:
                bound = {}
        return bound

    # Properties 
    @property
    def minLongitude(self):
        """Minimum longitude bound"""
        return self.bounds.get('longitude')[0]

    @property
    def maxLongitude(self):
        """Maximum longitude bound"""
        return self.bounds.get('longitude')[1]

    @property
    def minLatitude(self):
        """Minimum latitude bound"""
        return self.bounds.get('latitude')[0]

    @property
    def maxLatitude(self):
        """Minimum latitude bound"""
        return self.bounds.get('latitude')[1]

    