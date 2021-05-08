from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser("Pass in the file names")
parser.add_argument("--object", action = "store")
parser.add_argument("--flat", action = "store")
parser.add_argument("--bias", action = "store")
args = parser.parse_args()

with fits.open(args.object) as object_hdul:
    object_data = object_hdul[0].data
    object_name = object_hdul[0].header["Object"]

with fits.open(args.flat) as flat_hdul:
    flat_data = flat_hdul[0].data

with fits.open(args.bias) as bias_hdul:
    bias_data = bias_hdul[0].data

flat_bias = flat_data - bias_data
object_bias = object_data - bias_data
average_flat_bias = np.average(flat_bias)
norm_flat_bias = flat_bias / average_flat_bias
final_object = object_bias / norm_flat_bias

plt.imshow(final_object, cmap = "gray")
plt.colorbar()
plt.savefig(object_name + ".png")

