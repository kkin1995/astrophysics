import numpy as np

def angular_diameter(diameter_of_object, distance_to_object):
    theta = 2 * np.arctan2(diameter_of_object/2, distance_to_object)
    theta_in_degrees = theta * (180 / np.pi)
    return theta_in_degrees

if __name__ == '__main__':
    distance_to_moon = 384400e3 # meters
    diameter_moon = 3473.2e3 
    print("Angular Diameter of the Moon is {}".format(angular_diameter(diameter_moon, distance_to_moon)))

    distance_to_moon_apogee = 406512e3 # meters
    apogee_moon = angular_diameter(diameter_moon, distance_to_moon_apogee)
    print("Angular Diameter of the Moon at Apogee is {}".format(apogee_moon))

    distance_to_moon_perigee = 356794e3 # meters
    perigee_moon = angular_diameter(diameter_moon, distance_to_moon_perigee)
    print("Angular Diameter of the Moon at Perigee is {}".format(perigee_moon))

    average_apogee_perigee = (apogee_moon + perigee_moon) / 2
    print("Average Angular Diameter of the Moon is {}".format(average_apogee_perigee))

    distance_to_sun = 147.45e9
    diameter_sun = 1.3972e9
    print("Angular Diameter of the Sun is {}".format(angular_diameter(diameter_sun, distance_to_sun)))

    distance_to_mercury = 7.7e10 # meters
    diameter_of_mercury = 2 * 2.4397e6
    print("Angular Diameter of Mercury is {}".format(angular_diameter(diameter_of_mercury, distance_to_mercury)))
