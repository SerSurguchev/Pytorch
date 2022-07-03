import random
import numpy as np
import copy
import torch
import torch.nn as nn
from config import DEVICE

def save_checkpoint(model, optimizer, filename = "my_checkpoint.pth.tar"):

    print('=> Saving checkpoint')
    
    torch.save({
        'state_dict': model.state_dict(),
        'optimizer': optimizer.state_dict()
    }, filename)

def load_checkpoint(checkpoint_file, model, optimizer, lr):

    print("=> Loading checkpoint")
    checkpoint = torch.load(checkpoint_file, map_location=DEVICE)
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])

    # If we don't do this then it will just have learning rate of old checkpoint
    # and it will lead to many hours of debugging \:
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr


def seed_everything(seed=42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
