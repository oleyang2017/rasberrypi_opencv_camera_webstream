# coding: utf-8
import os

cwd = os.path.split(os.path.realpath(__file__))[0]
classify_path = cwd + "/venv/lib/python3.5/site-packages/tensorflow/models/image/imagenet/classify_image.py"

model_path = "tensorflow/model"

image_path = "image-1.jpg"

print("已开始识别,请稍等....")
fouput = os.popen("python " + classify_path + " --model_dir " + model_path + " --image_file " + image_path)
result = fouput.readlines()

for i in result:
    i = i.strip('\n')
    print(i)
