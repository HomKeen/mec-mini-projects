


import pydicom as dcm
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import sys
import tensorflow as tf
from joblib import Parallel, delayed
import PIL
from PIL import Image
import multiprocessing as mp
import warnings


img_dir_train = '/home/jupyter/rsna-intracranial-hemorrhage-detection/stage_2_train/'
png_dir_train = '/home/jupyter/rsna-intracranial-hemorrhage-detection/stage_2_train_imgs/'
img_dir_test = '/home/jupyter/rsna-intracranial-hemorrhage-detection/stage_2_test/'
png_dir_test = '/home/jupyter/rsna-intracranial-hemorrhage-detection/stage_2_test_imgs/'
n_err = 0
warnings.filterwarnings('ignore')


# In[ ]:


def get_center_and_width(dicom):
    return tuple([int(x[0]) if type(x) == dcm.multival.MultiValue else int(x) for x in [dicom.WindowCenter, dicom.WindowWidth]])
def normalize_minmax(img):
    mi, ma = img.min(), img.max()
    if mi == ma:
        return img-mi
    return (img - mi) / (ma - mi)

def window_filter(img, center, width, slope, intercept):
    out = np.copy(img)
    out = out*slope + intercept
    lowest_visible = center - width//2
    highest_visible = center + width//2
    
    out[out < lowest_visible] = lowest_visible
    out[out > highest_visible] = highest_visible
    return normalize_minmax(out) * 255

def get_img_tensor(img_path):
    dicom = dcm.dcmread(img_path, force=True)
    
    img = dicom.pixel_array
    center, width = get_center_and_width(dicom)
    slope, intercept = dicom.RescaleSlope, dicom.RescaleIntercept
    brain = window_filter(img, 40, 80, slope, intercept)
    subdural = window_filter(img, 80, 200, slope, intercept)
    tissue = window_filter(img, 40, 380, slope, intercept)
    
    return np.stack([brain, subdural, tissue], axis=2).astype(np.int8)

def write_to_png(img_id, png_dir, img_dir):
    global n_err
    try:
        img_array = get_img_tensor(img_dir+img_id+'.dcm')
        if img_array.shape == (512,512,3):
            img = Image.fromarray(img_array, 'RGB')
            img.save(png_dir+img_id+'.png')
        else:
            n_err += 1
    except Exception as e:
        n_err += 1

def write_all_to_png(png_dir, img_dir):
    present = set(map(lambda x: x.split('.')[0], os.listdir(png_dir)))
    total = set(map(lambda x: x.split('.')[0], os.listdir(img_dir)))
    to_compute = list(total.difference(present))
    _ = Parallel(n_jobs=-1)(delayed(write_to_png)(img_name, png_dir, img_dir) for img_name in tqdm(to_compute))        


# In[ ]:


write_all_to_png(png_dir_train, img_dir_train)


# In[ ]:


write_all_to_png(png_dir_test, img_dir_test)


# In[ ]:


print(f'{n_err} errors')
