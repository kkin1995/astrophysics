from solidangle import solid_angle, calculate_number_of_objects_in_sky
from solarflux import solar_flux

if __name__ == "__main__":
    import yaml
    import argparse
    with open("config.yaml") as config:
        data = yaml.load(config, Loader = yaml.FullLoader)

    parser = argparse.ArgumentParser()
    parser.add_argument("--object", action = "store")
    args = parser.parse_args()

    if args.object.lower() == "moon":
        distance_to_earth = float(data["moon"]["distance_to_earth"])
        albedo_moon = float(data["moon"]["albedo"])
        radius_moon = float(data["moon"]["radius"])
        AU = 1.496e11 # m
        distance_to_sun = float(data["moon"]["distance"]) # AU
        distance_to_sun_in_m = distance_to_sun * AU # m
        incident_flux = solar_flux(distance_to_sun)
        reflected_flux = albedo_moon * incident_flux
        print("Flux reflected from the moon is {} W/m^2".format(reflected_flux))
        solid_angle_moon_at_earth = solid_angle(radius_moon, distance_to_earth)
        no_of_moons_to_cover_sky = calculate_number_of_objects_in_sky(solid_angle_moon_at_earth)
        total_flux = no_of_moons_to_cover_sky * reflected_flux
        print("If {} moons cover the sky, the amount of flux received at Earth is {} W/m^2".format(no_of_moons_to_cover_sky, total_flux))
        print("Compared to the above, the flux received at Earth from the Sun is {} W/m^2".format(solar_flux(1)))

