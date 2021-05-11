# Reads the headers of all FITS files placed in the same folder and exports it 
# as YAML file's

from astropy.io import fits
import json
import glob

for filename in glob.glob("*.fits"):
    with fits.open(filename) as hdul:
        hdr = hdul[0].header # FITS Header

    hdr_keys = list(hdr.keys())

    with open(filename + "_header.yaml", "w+") as f:
        for i in range(len(hdr)):
            f.write(hdr_keys[i] + ": " + str(hdr[i]) + " " + "# " + hdr.comments[i] + "\n")
