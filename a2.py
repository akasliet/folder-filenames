get_ipython().magic('reset -sf')
import os
import numpy as np

path = 'H:/TCGAKIRC/'

directory_contents = os. listdir(path)
print(directory_contents)
i=0
for item in directory_contents: 
    if os. path. isdir(item):
        i=i+1
        print(item)
print(i)
num_img_per_pat = np.zeros(i)

thisdir = path
# r=root, d=directories, f = files
i=0
temp=0
for r, d, f in os.walk(thisdir):
    temp=temp+1
    if(temp==1):
        i=i+1
    print(r," bi", d)
    for file in f: 
        if file.endswith(".JPG"):
            print()
            #print(r, " hi ", d,os.path.join(r, file),"\n")
print(i)
  