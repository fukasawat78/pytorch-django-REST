from PIL import Image
import json
import cv2
import numpy as np
import torch
import torch.nn as nn
from torchvision import transforms
from .model import resnet_model

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
softmax = torch.nn.Softmax(dim=1)
model = resnet_model()
def predict(img):
    # json
    with open("./app/resnet/config/imagenet_class_index.json", 'r') as f:
        image_dict = json.load(f)
    # img
    img = Image.open(img)
    img = img.convert('RGB')
    img = np.array(img)
    img = preprocess(transforms.ToPILImage()(img)).unsqueeze(0)

    # prediction
    predict = model(img).data
    prob = softmax(predict)[0].tolist()
    best_ten = np.argsort(prob)[::-1][:10]

    response = []
    for i,rank in enumerate(best_ten,1):
        label = image_dict[str(rank)][1]
        response.append({"rank":i,"prob":prob[rank],"label":label})

    return response