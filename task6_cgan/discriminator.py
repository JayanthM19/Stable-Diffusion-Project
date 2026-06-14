import torch
import torch.nn as nn


class Discriminator(nn.Module):

    def __init__(
        self,
        num_classes=10,
        img_size=28
    ):
        super().__init__()

        self.label_embedding = nn.Embedding(
            num_classes,
            num_classes
        )

        self.model = nn.Sequential(

            nn.Linear(
                img_size * img_size + num_classes,
                512
            ),

            nn.LeakyReLU(
                0.2,
                inplace=True
            ),

            nn.Linear(
                512,
                256
            ),

            nn.LeakyReLU(
                0.2,
                inplace=True
            ),

            nn.Linear(
                256,
                1
            ),

            nn.Sigmoid()
        )

        self.img_size = img_size

    def forward(
        self,
        img,
        labels
    ):

        img = img.view(
            img.size(0),
            -1
        )

        label_embed = self.label_embedding(
            labels
        )

        discriminator_input = torch.cat(
            (
                img,
                label_embed
            ),
            dim=1
        )

        validity = self.model(
            discriminator_input
        )

        return validity