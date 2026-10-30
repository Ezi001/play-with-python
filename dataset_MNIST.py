import os

import numpy as np

import torch

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

import torchvision.transforms as transforms


class MNISTDataset(Dataset):
    def __init__(self, image_path, label_path, transform=None):
        self.images = self._read_images(image_path)
        self.labels = self._read_labels(label_path)
        self.transform = transform

    def _read_images(self, path):
        with open(path, "rb") as f:
            magic = int.from_bytes(f.read(4), byteorder="big")
            if magic != 2051:
                raise ValueError(f"Bad image magic: {magic}")

            num_images = int.from_bytes(f.read(4), byteorder="big")
            rows = int.from_bytes(f.read(4), byteorder="big")
            cols = int.from_bytes(f.read(4), byteorder="big")

            data = np.frombuffer(f.read(), dtype=np.uint8)
            images = data.reshape(num_images, rows, cols)

        return images

    def _read_labels(self, path):
        with open(path, "rb") as f:
            magic = int.from_bytes(f.read(4), byteorder="big")
            if magic != 2049:
                raise ValueError(f"Bad label magic: {magic}")

            num_labels = int.from_bytes(f.read(4), byteorder="big")
            labels = np.frombuffer(f.read(), dtype=np.uint8)

        if len(labels) != num_labels:
            raise ValueError("Label count mismatch")

        return labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        image = self.images[idx].astype(np.float32)   # shape: (28, 28)
        label = int(self.labels[idx])

        # optional transforms
        if self.transform is not None:
            image = self.transform(image)

        # if your transform is not converting to tensor, do it here:
        # image = torch.from_numpy(image).float()
        # image = image.unsqueeze(0)  # (1, 28, 28)

        return image, label




MNIST=MNISTDataset("data/train-images.idx3-ubyte", "data/train-labels.idx1-ubyte")



img, label = MNIST[0]
print(img.shape)   # e.g. torch.Size([1, 28, 28]) or [28, 28]
print(label)

import matplotlib.pyplot as plt


plt.imshow(img, cmap="gray")
plt.show()