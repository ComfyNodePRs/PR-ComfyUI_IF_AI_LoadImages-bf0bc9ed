import os
import glob
import shutil
import sys
import folder_paths

from .IFLoadImagesNodeS import IFLoadImagess




NODE_CLASS_MAPPINGS = {
    "IF_LoadImagesS": IFLoadImagess,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IF_LoadImagesS": "IF Load ImagesS 🖼️",
}

WEB_DIRECTORY = "./web"
__all__ = [
    "NODE_CLASS_MAPPINGS", 
    "NODE_DISPLAY_NAME_MAPPINGS", 
    "WEB_DIRECTORY", 
    ]
