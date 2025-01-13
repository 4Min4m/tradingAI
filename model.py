import torch
import torch.nn as nn
import torch.optim as optim

class CryptoAgentModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(CryptoAgentModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x