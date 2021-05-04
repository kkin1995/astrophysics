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
        full_solid_angle_sky = 4 * pi
        hemisphere_solid_angle = full_solid_angle_sky / 2
        amount_of_sky_occupied_by_moon = solid_angle_subtended_by_moon / hemisphere_solid_angle
        print("The Solid Angle subtended by the moon in the sky is {} sr".format(solid_angle_subtended_by_moon))
        print("{} moons will cover the sky".format(1 / amount_of_sky_occupied_by_moon))

    elif args.object.lower() == "pluto":
        radius_of_pluto = float(data["pluto"]["radius"])
        distance_at_apogee = float(data["pluto"]["distance_at_apogee"])
        distance_at_perigee = float(data["pluto"]["distance_at_perigee"])
        average_distance = (distance_at_apogee + distance_at_perigee) / 2
        hemisphere_solid_angle = 2 * pi
        solid_angle_pluto = solid_angle(radius_of_pluto, average_distance)
        amount_of_sky_occupied_by_pluto = solid_angle_pluto / hemisphere_solid_angle
        solid_angle_pluto_at_apogee = solid_angle(radius_of_pluto, distance_at_apogee)
        solid_angle_pluto_at_perigee = solid_angle(radius_of_pluto, distance_at_perigee)
        print("Variation in Solid Angle at Apogee and Perigee for Pluto is {} sr".format(abs(solid_angle_pluto_at_apogee - solid_angle_pluto_at_perigee)))
        print("{} plutos will cover the sky".format(1 / amount_of_sky_occupied_by_pluto))

    elif args.object.lower() == "jupiter":
        radius_of_jupiter = float(data["jupiter"]["radius"])
        distance_at_apogee = float(data["jupiter"]["distance_at_apogee"])
        distance_at_perigee = float(data["jupiter"]["distance_at_perigee"])
        average_distance = (distance_at_apogee + distance_at_perigee) / 2
        solid_angle_jupiter = solid_angle(radius_of_jupiter, average_distance)
        solid_angle_jupiter_at_apogee = solid_angle(radius_of_jupiter, distance_at_apogee)
        solid_angle_jupiter_at_perigee = solid_angle(radius_of_jupiter, distance_at_perigee)
        solid_angle_of_hemisphere = 2 * pi
        amount_of_sky_occupied_by_jupiter = solid_angle_jupiter / solid_angle_of_hemisphere
        print("Variation in Solid Angle at Apogee and Perigee for Jupiter is {} sr".format(abs(solid_angle_jupiter_at_apogee - solid_angle_jupiter_at_perigee)))
        print("{} jupiters will cover the sky".format(1 / amount_of_sky_occupied_by_jupiter))
