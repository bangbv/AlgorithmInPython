import torch
import torch.nn as nn

def nll():
    # Define the negative log likelihood loss function
    nll_loss = nn.NLLLoss()

    # Example prediction probabilities (log probabilities, because NLL works with log probabilities)
    # Suppose we have a 3-class classification problem with batch size of 2
    log_probs = torch.tensor([[ -0.5, -1.0, -2.0],
                              [ -0.2, -0.8, -1.5]])
    # Ground truth labels (index of correct class for each example)
    targets = torch.tensor([0, 2])
    # Calculate the NLL loss
    loss = nll_loss(log_probs, targets)
    print("NLL Loss: ", loss.item())


def gaussian_nll_loss(y_true, y_pred_mean, y_pred_std):
    # Assuming y_pred_std is the standard deviation
    nll = 0.5 * torch.log(2 * torch.pi * (y_pred_std ** 2)) + ((y_true - y_pred_mean) ** 2) / (2 * y_pred_std ** 2)
    return torch.mean(nll)


def nll_per_dimension(nll_total, num_dimensions):
    return nll_total / num_dimensions


# main function
if __name__ == "__main__":
    # Example: y_true = ground truth values, y_pred_mean = predicted mean values, y_pred_std = predicted std deviations
    y_true = torch.tensor([3.0, 5.0])
    y_pred_mean = torch.tensor([2.8, 5.2])
    y_pred_std = torch.tensor([0.5, 0.3])
    # Calculate Gaussian NLL loss
    loss = gaussian_nll_loss(y_true, y_pred_mean, y_pred_std)
    print("Gaussian NLL Loss: ", loss.item())

    # nll_loss = gaussian_nll_loss(y_true, y_pred_mean, y_pred_std)
    # nll_per_dim = nll_per_dimension(nll_loss,
    #                                 y_true.shape[1])  # assuming y_true is of shape (batch_size, num_dimensions)
    # print("NLL Per Dimension: ", nll_per_dim.item())
