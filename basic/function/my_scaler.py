from dataclasses import dataclass
import numpy as np
import pandas as pd
from functools import partial


def vec_num2repr(val, base, prec, max_val):
    """
    Convert numbers to a representation in a specified base with precision.

    Parameters:
    - val (np.array): The numbers to represent.
    - base (int): The base of the representation.
    - prec (int): The precision after the 'decimal' point in the base representation.
    - max_val (float): The maximum absolute value of the number.

    Returns:
    - tuple: Sign and digits in the specified base representation.

    Examples:
        With base=10, prec=2:
            0.5   ->    50
            3.52  ->   352
            12.5  ->  1250
    """
    base = float(base)
    bs = val.shape[0]
    sign = 1 * (val >= 0) - 1 * (val < 0)
    val = np.abs(val)
    max_bit_pos = int(np.ceil(np.log(max_val) / np.log(base)).item())

    before_decimals = []
    for i in range(max_bit_pos):
        digit = (val / base ** (max_bit_pos - i - 1)).astype(int)
        before_decimals.append(digit)
        val -= digit * base ** (max_bit_pos - i - 1)

    before_decimals = np.stack(before_decimals, axis=-1)

    if prec > 0:
        after_decimals = []
        for i in range(prec):
            digit = (val / base ** (-i - 1)).astype(int)
            after_decimals.append(digit)
            val -= digit * base ** (-i - 1)

        after_decimals = np.stack(after_decimals, axis=-1)
        digits = np.concatenate([before_decimals, after_decimals], axis=-1)
    else:
        digits = before_decimals
    return sign, digits


@dataclass
class SerializerSettings:
    """
    Settings for serialization of numbers.

    Attributes:
    - base (int): The base for number representation.
    - prec (int): The precision after the 'decimal' point in the base representation.
    - signed (bool): If True, allows negative numbers. Default is False.
    - fixed_length (bool): If True, ensures fixed length of serialized string. Default is False.
    - max_val (float): Maximum absolute value of number for serialization.
    - time_sep (str): Separator for different time steps.
    - bit_sep (str): Separator for individual digits.
    - plus_sign (str): String representation for positive sign.
    - minus_sign (str): String representation for negative sign.
    - half_bin_correction (bool): If True, applies half bin correction during deserialization. Default is True.
    - decimal_point (str): String representation for the decimal point.
    """
    base: int = 10
    prec: int = 3
    signed: bool = True
    fixed_length: bool = False
    max_val: float = 1e7
    time_sep: str = ' ,'
    bit_sep: str = ' '
    plus_sign: str = ''
    minus_sign: str = ' -'
    half_bin_correction: bool = True
    decimal_point: str = ''
    missing_str: str = ' Nan'


def serialize_arr(arr, settings: SerializerSettings):
    """
    Serialize an array of numbers (a time series) into a string based on the provided settings.

    Parameters:
    - arr (np.array): Array of numbers to serialize.
    - settings (SerializerSettings): Settings for serialization.

    Returns:
    - str: String representation of the array.
    """
    # max_val is only for fixing the number of bits in nunm2repr so it can be vmapped
    assert np.all(np.abs(arr[~np.isnan(arr)]) <= settings.max_val), f"abs(arr) must be <= max_val,\
         but abs(arr)={np.abs(arr)}, max_val={settings.max_val}"

    if not settings.signed:
        assert np.all(arr[~np.isnan(arr)] >= 0), f"unsigned arr must be >= 0"
        plus_sign = minus_sign = ''
    else:
        plus_sign = settings.plus_sign
        minus_sign = settings.minus_sign

    vnum2repr = partial(vec_num2repr, base=settings.base, prec=settings.prec, max_val=settings.max_val)
    sign_arr, digits_arr = vnum2repr(np.where(np.isnan(arr), np.zeros_like(arr), arr))
    ismissing = np.isnan(arr)

    def tokenize(arr):
        return ''.join([settings.bit_sep + str(b) for b in arr])

    bit_strs = []
    for sign, digits, missing in zip(sign_arr, digits_arr, ismissing):
        if not settings.fixed_length:
            # remove leading zeros
            nonzero_indices = np.where(digits != 0)[0]
            if len(nonzero_indices) == 0:
                digits = np.array([0])
            else:
                digits = digits[nonzero_indices[0]:]
            # add a decimal point
            prec = settings.prec
            if len(settings.decimal_point):
                digits = np.concatenate([digits[:-prec], np.array([settings.decimal_point]), digits[-prec:]])
        digits = tokenize(digits)
        sign_sep = plus_sign if sign == 1 else minus_sign
        if missing:
            bit_strs.append(settings.missing_str)
        else:
            bit_strs.append(sign_sep + digits)
    bit_str = settings.time_sep.join(bit_strs)
    bit_str += settings.time_sep  # otherwise there is ambiguity in number of digits in the last time step
    return bit_str


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
        q = np.maximum(np.quantile(np.abs(history), alpha),.01)
        def transform(x):
            return x / q
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




if __name__ == "__main__":
    # Create a unique scaler for each series
    input_arrs = np.array([112,118,132,129,121,135,148,148])
    train = pd.Series(input_arrs)
    train = [train]

    input_arrs = [train[i].values for i in range(len(train))]
    alpha = 0.95
    beta = 0.3
    basic = False
    scalers = [get_scaler(train[i].values, alpha=alpha, beta=beta, basic=basic) for i in range(len(train))]
    # print(f"scalers: {scalers}")
    transformed_input_arrs = np.array([scaler.transform(input_array) for input_array, scaler in zip(input_arrs, scalers)])
    print(transformed_input_arrs)

    settings = SerializerSettings(base=10, prec=3, signed=True, time_sep=', ', bit_sep='', minus_sign='-')
    final_input_strs = [serialize_arr(scaled_input_arr, settings) for scaled_input_arr in transformed_input_arrs]
    print(f"final_input_strs: {final_input_strs}")