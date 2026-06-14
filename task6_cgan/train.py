import torch
import torch.nn as nn
import torch.optim as optim

from generator import Generator
from discriminator import Discriminator

generator = Generator()

discriminator = Discriminator()

adversarial_loss = nn.BCELoss()

optimizer_G = optim.Adam(
    generator.parameters(),
    lr=0.0002
)

optimizer_D = optim.Adam(
    discriminator.parameters(),
    lr=0.0002
)

print("Training components initialized.")