import torch
import torch.nn as nn

class DrivingModel(nn.Module):

    def __init__(self):
        super(DrivingModel, self).__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(3,16,5,stride=2),
            nn.ReLU(),
            nn.Conv2d(16,32,5,stride=2),
            nn.ReLU()
        )

        self.fc = nn.Sequential(
            nn.Linear(32*22*22,128),
            nn.ReLU(),
            nn.Linear(128,3)
        )

    def forward(self,x):

        x=self.conv(x)
        x=x.view(x.size(0),-1)
        x=self.fc(x)

        return x