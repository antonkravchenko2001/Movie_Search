import torch
import yaml
from torch.nn import Module
from annoy import AnnoyIndex
from .bert import BertEncoder


class SymmetricModel():

    def __init__(self):
        self.config = load_search_config()['symmetric']
        self.model = load_model(self.config['checkpoint_path'])
        self.index = load_index(self.config['index_path'])


class AsymmetricModel():
    def __init__(self):
        self.config = load_search_config()['asymmetric']
        self.model = load_model(self.config['checkpoint_path'])
        self.index = load_index(self.config['index_path'])
    


def load_index(index_path: str) -> AnnoyIndex:
    index = AnnoyIndex(512, 'angular')
    index.load(index_path)
    return index


def load_model(checkpoint_path: str) -> Module:
    model = BertEncoder()
    checkpoint = torch.load(checkpoint_path)
    model.load_state_dict(checkpoint['model_state_dict'])
    return model


def load_search_config():
    with open('./algorithms/algorithms_config.yaml') as f:
        config = yaml.safe_load(f)
    return config['search']
