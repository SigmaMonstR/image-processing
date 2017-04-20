
#example
import os
path = "/Users/jeff/Documents/Github/image-processing/test"
os.chdir(path)

import PIL
import pandas as pd
import numpy as np

img = 'a1.jpg-0.jpeg'

def imgToDF(img):
    with open(img, 'r+b') as f:
        with Image.open(f) as image:
            arr = np.array(image)
            arr = arr.ravel()
            df = pd.DataFrame(arr).transpose()
    return df


