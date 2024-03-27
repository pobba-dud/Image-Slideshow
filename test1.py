import cv2
import numpy as np
import time
import os

def load_images_from_folder(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = cv2.imread(os.path.join(directory, filename))
            if img is not None:
                images.append(img)
    return np.array(images)

def cycle_through_images(image_array):
    for i in range(image_array.shape[0]):
        cv2.imshow('Image', image_array[i])
        time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

directory = '/path/to/your/directory'
image_array = load_images_from_folder(directory)
cycle_through_images(image_array)
