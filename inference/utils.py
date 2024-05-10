from torch.utils.data import Dataset
from torchvision import transforms
#from torchvision.io import read_image
from PIL import Image

import os
import pandas as pd
import PIL


class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, str(self.img_labels.image_id.iloc[idx]))
        #image = read_image(img_path + '.png')
        image = PIL.Image.open(img_path + '.png')
        image = transforms.functional.to_tensor(image)
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image
