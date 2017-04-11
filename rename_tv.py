
# coding: utf-8

# In[20]:

# Import the os module, for the os.walk function
import os
import string

# Set the directory you want to start from
rootDir = '/mnt/temp/tv/'
imagefile=''
for dirName, subdirList, fileList in os.walk(rootDir):
    print('dirName = %s' % dirName)

    for fname in fileList:
        imagefile =dirName+'/'+fname
        print('\timagefile = %s' % imagefile)
        baseDirName = os.path.basename(dirName)
        print('\tbaseDirName = %s' % baseDirName )
        
        destFile = string.replace(imagefile, 'screen',  baseDirName.lower())
        print('\trename to %s' % destFile)
        os.rename(imagefile,destFile)


# In[ ]:




# In[ ]:



