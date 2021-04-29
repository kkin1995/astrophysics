# What is the value of the solar flux incident on a particular object
# Defining albedo as the ratio of the reflected flux to the incident flux, compute the absorbed flux for the given object.
# Given the temperature of an object, compute it's blackbody temperature
# How does the blackbody flux of the given object compare with its reflected flux

from numpy import pi
import argparse
import yaml

def solar_flux(distance_to_object):
    AU = 1.496e11 # m
    luminosity_of_the_sun = 3.826e26 # W
    distance_to_object = distance_to_object * AU
    flux = luminosity_of_the_sun / (4 * pi * (distance_to_object**2))
    return flux

def absorbed_flux(albedo, incident_flux):
    absorbed_to_incident_flux = 1 - albedo
    absorbedFlux = absorbed_to_incident_flux * incident_flux
    return absorbedFlux

def blackbody_flux(temperature):
    stefan_boltzmann_constant = 5.6703e-8 # W m^-2 K ^-4
    return stefan_boltzmann_constant * (temperature**4)

def reflected_flux(albedo, incident_flux):
    return albedo * incident_flux

def temperature_from_peak_wavelength(peak_wavelength):
    wiens_constant = 2.898e-3 # m K
    return wiens_constant / peak_wavelength

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Object Name")
    parser.add_argument("--object", action = "store", help = "Usage: solar_flux.py --object [name_of_object]")
    args = parser.parse_args()

    with open("config.yaml") as config:
        planet_data = yaml.load(config, Loader = yaml.FullLoader)

    if args.object.lower() == "jupiter":
        distance_to_jupiter = planet_data["jupiter"]["distance"] # AU
        albedo_jupiter = planet_data["jupiter"]["albedo"]
        temperature_jupiter = planet_data["jupiter"]["temperature"] # K
        peak_wavelength_from_jupiter = planet_data["jupiter"]["peak_wavelength"] # m
        flux_at_jupiter = solar_flux(distance_to_jupiter)
        absorbedFluxJupiter = absorbed_flux(albedo_jupiter, flux_at_jupiter)
        blackbody_flux_jupiter = blackbody_flux(temperature_jupiter)
        reflected_flux_jupiter = reflected_flux(albedo_jupiter, flux_at_jupiter)
        temperature_jupiter_from_peak_wavelength = temperature_from_peak_wavelength(peak_wavelength_from_jupiter)
        print("Solar Flux at Jupiter is {} W/m^2".format(flux_at_jupiter))
        print("Jupiter absorbs {} W/m^2".format(absorbedFluxJupiter))
        print("Blackbody Flux from Jupiter is {} W/m^2".format(blackbody_flux_jupiter))
        print("Reflected Flux from Jupiter is {} W/m^2".format(reflected_flux_jupiter))
        print("Observed Temperature of Jupiter is {}".format(temperature_jupiter_from_peak_wavelength))
    elif args.object.lower() == "earth":
        distance_to_earth = planet_data["earth"]["distance"] # AU
        albedo_earth = planet_data["earth"]["albedo"]
        temperature_earth = planet_data["earth"]["temperature"] # K
        peak_wavelength_from_earth = planet_data["earth"]["peak_wavelength"] # m
        flux_at_earth = solar_flux(distance_to_earth)
        absorbedFluxEarth = absorbed_flux(albedo_earth, flux_at_earth)
        blackbody_flux_earth = blackbody_flux(temperature_earth)
        reflected_flux_earth = reflected_flux(albedo_earth, flux_at_earth)
        temperature_earth_from_peak_wavelength = temperature_from_peak_wavelength(peak_wavelength_from_earth)
        print("Solar Flux at Earth is", flux_at_earth)
        print("Earth absorbs {} W/m^2".format(absorbedFluxEarth))
        print("Blackbody Flux from Earth is {} W/m^2".format(blackbody_flux_earth))
        print("Reflected Flux from Earth is {} W/m^2".format(reflected_flux_earth))
        print("Observed Temperature of Earth is {}".format(temperature_earth_from_peak_wavelength))
