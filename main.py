from PIL import Image
from roboflow import Roboflow
import cv2
import os
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
# from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
import re
import numpy as np
import requests
import json
import matplotlib.pyplot as plt


def obtain_thresh_image(ar: np.asarray):
    image = Image.fromarray(ar)
    resized = image.resize((1000,1000))
    opencv_image = np.array(resized)
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2GRAY)
    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    Image.fromarray(binary_image).save(f"./images/test.png")
    return binary_image


def cropping_image(path, prediction):
    center_x = prediction["x"]
    center_y = prediction["y"]
    w, h = prediction["width"], prediction["height"]
    im = Image.open(path)
    top_left = center_x - int(w/2)
    upper_left = center_y - int(h/2)
    down_right = center_x + int(w/2) 
    lower_right = center_y + int(h/2) 
    im_cropped = im.crop((top_left, upper_left,down_right,lower_right))
    im_cropped_pixels = np.asarray(im_cropped)
    new_img = obtain_thresh_image(im_cropped_pixels)
    return new_img 

def get_crop_image():
    rf = Roboflow(api_key="V9qEIrKTpyQTYNn5m42p")
    project = rf.workspace().project("vatican")
    model = project.version(2).model
    path = "./images/carte_classique.jpg"
    info = model.predict(path, confidence=40, overlap=30).json()
    images = []
    if type(info["predictions"]) == list:
        for prediction in info["predictions"]:
            new_img = cropping_image(path, prediction)
            images.append(new_img)
    return images

def translate(images):
    # letters = images[0]
    # let_img = Image.fromarray(letters)
    let_resized = images.resize((1024,256))
    max_new_tokens = 20
    conv = let_resized.convert("RGB")
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
    pixel_values = processor(conv, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values, max_new_tokens=max_new_tokens)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text + " "

def get_from_file():
    with open("./translation.txt", "r") as f:
        phrases = f.readlines()
        for item in phrases:
            print(item[:-2])

image_to_crop = Image.open("./images/test.png")
im = image_to_crop.crop((0, 0, 1000, 200))
wine = translate(im).strip()
name_wt_punctuation = re.sub(r'\.', '', wine)
print(name_wt_punctuation)
