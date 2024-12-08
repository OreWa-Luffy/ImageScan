import random, torch, os, numpy as np
import torch.nn as nn
import config
import copy



def save_checkpoint(model, optimizer, filename="my_checkpoint.pth.tar"):
    print("=> Saving Checkpoint")
    checkpoint = {
        "state_dict": model.state_dict(),
        "optimizer": optimizer.state_dict(),
    }
    torch.save(checkpoint, filename)
    
    

def load_checkpoint(checkpoint_file, model, optimizer, lr):
    print("=> loading checkpoint")
    checkpoint = torch.load(checkpoint_file, map_location=config.DEVICE)
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])
    
    for param_group in optimizer.param_group:
        param_group["ir"] = lr
    
    