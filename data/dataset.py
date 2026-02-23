import torch
from torch.utils.data import Dataset

class ArabicTextDataset(Dataset):
    def __init__(self, texts, labels):
        """
        Args:
            texts (list): A list of Arabic text strings.
            labels (list): A list of labels corresponding to the texts.
        """
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        return text, label
