import torch
from torchvision import models

def resnet_model():
    MODEL_PATH = "./app/resnet/config/resnet18-5c106cde.pth"
    model = models.resnet18(pretrained=False)
    model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()
    return model