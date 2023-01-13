from PIL import Image
from splitter import ImageSplitter

class ImageTiler:
    """Image Tiler Class"""
    def __init__(self, imagePath, minZoom=0, maxZoom=18):
        self.imagePath = imagePath
        self.zoom = (minZoom, maxZoom)