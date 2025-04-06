from scaler import get_scaler
from serializer import SerializerSettings, serialize_arr, deserialize_str
import numpy as np
import fourier_transforms as ft
import pandas as pd

def normal_transform(input_arrs, scalers):
    steps = len(input_arrs[0])
    settings = SerializerSettings(base=10, prec=3, signed=True, time_sep=', ', bit_sep='', minus_sign='-')

    transformed_input_arrs = np.array([scaler.transform(input_array) for input_array, scaler in zip(input_arrs, scalers)])
    print(f"transformed_input_arrs: {transformed_input_arrs}")
    serialize_arr_output = [serialize_arr(scaled_input_arr, settings) for scaled_input_arr in transformed_input_arrs]
    print(f"serialize_arr: {serialize_arr_output}")

    deserialize_arr = [deserialize_str(input_str, settings, ignore_last=False, steps=steps) for input_str in serialize_arr_output]
    print(f"normal_transform:deserialize_strs: {deserialize_arr}")
    revert_results = np.array([scaler.inv_transform(deserialize_str) for deserialize_str, scaler in zip(deserialize_arr, scalers)])
    print(f"revert_results: {revert_results}")


def ft_transform(input_arrs):
    steps = len(input_arrs[0])
    settings = SerializerSettings(base=10, prec=3, signed=True, time_sep=', ', bit_sep='', minus_sign='-')

    ft_result = ft.fourier_transform(input_arrs)
    print(f"ft_transform:fourier transform result: {ft_result}")
    ft_input_serialize = [serialize_arr(scaled_input_arr, settings) for scaled_input_arr in ft_result]
    print(f"ft_transform: ft_input_serialize: {ft_input_serialize}")
    deserialize_arr = [deserialize_str(input_str, settings, ignore_last=False, steps=steps) for input_str in ft_input_serialize]
    print(f"ft_transform:deserialize_strs: {deserialize_arr}")
    deserialize_arr = [1043.0005, -42.1445]
    print(f"ft_transform:new_deserialize_strs: {deserialize_arr}")
    ft_revert_result = ft.inverse_fourier_transform(deserialize_arr)
    print(f"ft_transform:inverse_fourier_transform: {ft_revert_result}")


def ft_normal_transform(input_arrs, scalers):
    steps = len(input_arrs[0])
    settings = SerializerSettings(base=10, prec=3, signed=True, time_sep=', ', bit_sep='', minus_sign='-')

    transformed_input_arrs = np.array([scaler.transform(input_array) for input_array, scaler in zip(input_arrs, scalers)])
    print(f"transformed_input_arrs: {transformed_input_arrs}")
    serialize_arr_output = [serialize_arr(scaled_input_arr, settings) for scaled_input_arr in transformed_input_arrs]
    print(f"serialize_arr: {serialize_arr_output}")

    deserialize_arr = [deserialize_str(input_str, settings, ignore_last=False, steps=steps) for input_str in serialize_arr_output]
    print(f"normal_transform:deserialize_strs: {deserialize_arr}")
    revert_results = np.array([scaler.inv_transform(deserialize_str) for deserialize_str, scaler in zip(deserialize_arr, scalers)])
    print(f"revert_results: {revert_results}")


if __name__ == "__main__":
    # Create a unique scaler for each series
    input_arrs = np.array([112,118,132,129,121,135,148,148])
    print(f"input_arrs: {input_arrs}")
    train = pd.Series(input_arrs)
    train = [train]

    input_arrs = [train[i].values for i in range(len(train))]
    alpha = 0.3
    beta = 0.3
    basic = True
    scalers = [get_scaler(train[i].values, alpha=alpha, beta=beta, basic=basic) for i in range(len(train))]
    print(f"------- normal transform start ---------")
    normal_transform(input_arrs, scalers)
    print(f"------- normal transform end ---------")

    print(f"------- fourier transform start ---------")
    ft_transform(input_arrs)
    print(f"------- fourier transform end ---------")