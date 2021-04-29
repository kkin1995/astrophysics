from numpy import pi

def solid_angle(radius, distance_to_object):
    cross_area = pi * (radius**2)
    return cross_area / (distance_to_object**2)

if __name__ == "__main__":
    import yaml
    import argparse
    with open("config.yaml") as config:
        data = yaml.load(config, Loader = yaml.FullLoader)

    parser = argparse.ArgumentParser(description = "Choose a planet")
    parser.add_argument("--object", action = "store", help = "Usage: solid-angle.py --object [Object]")
    args = parser.parse_args()

    if args.object.lower() == "moon":
        radius_of_moon = float(data["moon"]["radius"])
        distance_moon_to_earth = float(data["moon"]["distance_to_earth"])
        solid_angle_subtended_by_moon = solid_angle(radius_of_moon, distance_moon_to_earth)
        print("The Solid Angle subtended by the moon in the sky is {} sr".format(solid_angle_subtended_by_moon))

    elif args.object.lower() == "pluto":
        radius_of_pluto = float(data["pluto"]["radius"])
        distance_at_apogee = float(data["pluto"]["distance_at_apogee"])
        distance_at_perigee = float(data["pluto"]["distance_at_perigee"])
        solid_angle_pluto_at_apogee = solid_angle(radius_of_pluto, distance_at_apogee)
        solid_angle_pluto_at_perigee = solid_angle(radius_of_pluto, distance_at_perigee)
        print("Variation in Solid Angle at Apogee and Perigee for Pluto is {} sr".format(abs(solid_angle_pluto_at_apogee - solid_angle_pluto_at_perigee)))
