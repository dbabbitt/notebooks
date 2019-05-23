
# coding: utf-8

# This is one of the 100 recipes of the [IPython Cookbook](
# http://ipython-books.github.io/), the definitive guide to high-performance 
# scientific computing and data science in Python.   3.7. Processing webcam 
# images in real-time from the notebook  In this recipe, we show how to 
# communicate data in both directions from the notebook to the Python kernel, 
# and conversely. Specifically, we will retrieve the webcam feed from the 
# browser using HTML5's `<video>` element, and pass it to Python in real time 
# using the interactive capabilities of the IPython notebook 2.0+. This way, 
# we can process the image in Python with an edge detector (implemented in 
# scikit-image), and display it in the notebook in real time.  Most of the 
# code for this recipe comes from [Jason Grout's example](
# https://github.com/jasongrout/ipywidgets).


from IPython.html.widgets import DOMWidget
from IPython.utils.traitlets import Unicode, Bytes, Instance
from IPython.display import display

from skimage import io, filter, color
import urllib
import base64
from PIL import Image
from io import BytesIO
import numpy as np
from numpy import array, ndarray
import matplotlib.pyplot as plt


# We define two functions to convert images from and to base64 strings. This 
# conversion is a common way to pass binary data between processes (here, the 
# browser and Python).

'''
img_data = io.BytesIO()
self.fig.savefig(img_data, format='jpeg')
img_data.seek(0)
uri = 'data:image/jpeg;base64,' + urllib.request.quote(base64.b64encode(img_data.getbuffer()))
img_data.close()
clear_output(wait=True)
display_html(HTML('<img src="' + uri + '">'))
'''


def to_b64(img):
    imgdata = BytesIO()
    pil = Image.fromarray(img)
    pil.save(imgdata, format='PNG')
    imgdata.seek(0)
    return urllib.parse.quote(base64.b64encode(imgdata.getvalue()))


def from_b64(b64):
    im = Image.open(BytesIO(base64.b64decode(b64)))
    return array(im)


# We define a Python function that will process the webcam image in real time.
# It accepts and returns a NumPy array. This function applies an edge 
# detector with the `roberts()` function in scikit-image.


def process_image(image):
    img = filter.roberts(image[:,:,0]/255.)
    return (255-img*255).astype(np.uint8)


# Now, we create a custom widget to handle the bidirectional communication of 
# the video flow from the browser to Python and reciprocally.


class Camera(DOMWidget):
    _view_name = Unicode('CameraView', sync=True)
    
    # This string contains the base64-encoded raw
    # webcam image (browser -> Python).
    imageurl = Unicode('', sync=True)
    
    # This string contains the base64-encoded processed 
    # webcam image(Python -> browser).
    imageurl2 = Unicode('', sync=True)

    # This function is called whenever the raw webcam
    # image is changed.
    def _imageurl_changed(self, name, new):
        head, data = new.split(',', 1)
        if not data:
            return
        
        # We convert the base64-encoded string
        # to a NumPy array.
        image = from_b64(data)
        
        # We process the image.
        image = process_image(image)
        
        # We convert the processed image
        # to a base64-encoded string.
        b64 = to_b64(image)
        
        self.imageurl2 = 'data:image/png;base64,' + b64