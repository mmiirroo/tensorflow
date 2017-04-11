
# coding: utf-8

# In[ ]:

# Import the os module, for the os.walk function
import os
from PIL import Image
import string

# Set the directory you want to start from
rootDir = '/mnt/temp/capture/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    '''for aDir in subdirList:
        print('aDir =: %s' % aDir)
        os.makedirs('/mnt/temp/crop/'+aDir)
    '''
    for fname in fileList:
        imagefile =dirName+'/'+fname
        destFile = string.replace(imagefile, 'capture', 'crop')
        print('\tdestFile = %s' % destFile)

        im=Image.open(imagefile)
        box=(120, 0, 419, 299)
        im_crop=im.crop(box)
        im_crop.save(destFile)
    


# In[ ]:



