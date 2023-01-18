class MapBounds:
    """ """
    def __init__(self):
        self.grid = [(None, None), (None, None)]

    @property
    def lowerBounds(self):
        """Get the lower bound from the grid property"""
        return self.grid[0]

    @property
    def upperBounds(self):
        """Get the lower bound from the grid property"""
        return self.grid[1]

    def getLowerBound(self, pos):
        """Get the x/y bound from the lower bounds
        
        Args:
            pos: x/y bound
        Returns:
            bound value
        """
        match pos.lower():
            case 'x':
                value = self.lowerBounds[0]
            case 'y':
                value = self.lowerBounds[1]
            case _:
                value = -1
        return  value

    def getUpperBound(self, pos):
        """Get the x/y bound from the upper bounds
        
        Args:
            pos: x/y bound
        Returns:
            bound value
        """
        match pos.lower():
            case 'x':
                value = self.upperBounds[0]
            case 'y':
                value = self.upperBounds[1]
            case _:
                value = -1
        return  value


    