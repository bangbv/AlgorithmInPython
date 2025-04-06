from dataclasses import dataclass
import numpy as np


@dataclass
class Scaler:
    """
    Represents a data scaler with transformation and inverse transformation functions.

    Attributes:
        transform (callable): Function to apply transformation.
        inv_transform (callable): Function to apply inverse transformation.
    """
    transform: callable = lambda x: x
    inv_transform: callable = lambda x: x

def get_scaler(history, alpha=0.95, beta=0.3, basic=False):
    """
    Generate a Scaler object based on given history data.

    Args:
        history (array-like): Data to derive scaling from.
        alpha (float, optional): Quantile for scaling. Defaults to .95.
        # Truncate inputs
        tokens = [tokeniz]
        beta (float, optional): Shift parameter. Defaults to .3.
        basic (bool, optional): If True, no shift is applied, and scaling by values below 0.01 is avoided. Defaults to False.

    Returns:
        Scaler: Configured scaler object.
    """
    history = history[~np.isnan(history)]
    if basic:
        history_abs = np.abs(history)
        # print(f"get_scaler: history_abs: {history_abs}")
        his_quantile = np.quantile(history_abs, alpha)
        # print(f"get_scaler: his_quantile: {his_quantile}")
        q = np.maximum(his_quantile,.01)
        # print(f"get_scaler: maximum: {q}")
        def transform(x):
            result = x / q
            # print(f"get_scaler: transform: result: {result}")
            return result
        def inv_transform(x):
            return x * q
    else:
        min_ = np.min(history) - beta*(np.max(history)-np.min(history))
        q = np.quantile(history-min_, alpha)
        if q == 0:
            q = 1
        def transform(x):
            # print_debug(my_print, f"transform from :", x, log_debug)
            # print_debug(my_print, f"transform to new:", (x - min_) / q, log_debug)
            return (x - min_) / q
        def inv_transform(x):
            # print_debug(my_print, f"revert transform from :", x, log_debug)
            # print_debug(my_print, f"revert transform to new:", (x - min_) / q, log_debug)
            return x * q + min_
    return Scaler(transform=transform, inv_transform=inv_transform)