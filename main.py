from solidangle import solid_angle
from solarflux import solar_flux, absorbed_flux, blackbody_flux, reflected_flux, temperature_from_peak_wavelength
from angulardiameter import angular_diameter
import yaml

AU = 1.496e11 # m

with open("object_config.yaml") as config:
    data = yaml.load(config, Loader = yaml.FullLoader)

object_name = data["object"]
distance_to_sun = data["distance"]
albedo = data["albedo"]
temperature = data["temperature"]
peak_wavelength = data["peak_wavelength"]
radius = data["radius"]

solid_angle_subtended = solid_angle(radius, distance_to_sun)
solar_flux = solar_flux(distance_to_sun)
flux_absorbed = absorbed_flux(albedo, solar_flux)
blackbody_flux = blackbody_flux(temperature)
flux_reflected = reflected_flux(albedo, solar_flux)
temperature_peak_wavelength = temperature_from_peak_wavelength(peak_wavelength)
angular_diameter = angular_diameter(2*radius, distance_to_sun*AU)

print("Solid Angle Subtended by {} at Sun is {} sr".format(object_name, solid_angle_subtended))
print("Solar Flux Incident At {} is {} W/m^2".format(object_name, solar_flux))
print("Flux absorbed by the {} is {} W/m^2".format(object_name, flux_absorbed))
print("Blackbody Flux of {} is {} W/m^2".format(object_name, blackbody_flux))
print("Flux Reflected from {} is {} W/m^2".format(object_name, flux_reflected))
print("Temperature of {} from Peak of Black Body Spectrum is {} K".format(object_name, temperature_peak_wavelength))
print("Angular Diameter of {} from Sun is {}".format(object_name, angular_diameter))
