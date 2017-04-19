
#Set of functions to random crop parts of images
#Load libraries
import random
import math
from PIL import Image
from resizeimage import resizeimage

#Randomly select x centroids from a bounding space
def centroidPick(width, height, size):
    rightside = width - math.floor(size/2)
    leftside = math.floor(size/2)
    bottom = math.floor(size/2)
    top = height - math.floor(size/2)
    result = []
    for x in range(size):
        temp = {"x": random.randint(leftside, rightside), "y": random.randint(bottom, top)}
        result.append(temp)
    return result

#Function to randomly crop image into squares
def randomTask(img, tasks, size):
    with open(img, 'r+b') as f:
        with Image.open(f) as image:
            cent = centroidPick(image.size[0], image.size[1], size)
            for x in range(0, tasks):
                #place crop code here
                outimage = image.crop(
                    (
                        int(cent[x]['x'] - math.floor(size/2)),
                        int(cent[x]['y'] - math.floor(size/2)),
                        int(cent[x]['x'] + math.floor(size/2)),
                        int(cent[x]['y'] + math.floor(size/2))
                    )
                )
                print x
                outimage.save(img + '-' + str(x) + '.jpeg')


#example
#randomTask('test.jpg',10, 100)






