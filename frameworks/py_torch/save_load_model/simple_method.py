# https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
import torch
import torchvision.models as models


# Saving and Loading Model Weights
def save_load_weights():
    # save the model
    model = models.vgg16(weights='IMAGENET1K_V1')
    torch.save(model.state_dict(), 'model_weights.pth')

    # load the model
    model = models.vgg16()  # we do not specify ``weights``, i.e. create untrained model
    model.load_state_dict(torch.load('model_weights.pth', weights_only=True))
    model.eval()


# Saving and Loading Models with Shapes
def save_load_shapes():
    # save the model
    model = models.vgg16(weights='IMAGENET1K_V1')
    torch.save(model, 'model.pth')

    # load the model
    model = torch.load('model.pth', weights_only=False),  # weights_only=False to load the entire model
    model.eval()


if __name__ == "__main__":
    # save_load_weights()
    save_load_shapes()