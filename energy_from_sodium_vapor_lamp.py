from numpy import pi

def calculate_energy_from_sodium_vapor_lamp(lambda_1, lambda_2, total_power):
    E_1 = total_power * (lambda_1 / (lambda_1 + lambda_2))
    E_2 = total_power - E_1
    return E_1, E_2

if __name__ == "__main__":
    import yaml
    with open("config.yaml") as config:
        data = yaml.load(config, Loader = yaml.FullLoader)

    lambda_1 = data["sodium_vapor_lamp"]["lambda_1"]
    lambda_2 = data["sodium_vapor_lamp"]["lambda_2"]
    total_power = data["sodium_vapor_lamp"]["total_power"]
    energy_from_lambda_1, energy_from_lambda_2 = calculate_energy_from_sodium_vapor_lamp(lambda_1, lambda_2, total_power)
    print("Energy from {} angstroms is {} W".format(lambda_1 / 1e-10, energy_from_lambda_1))
    print("Energy from {} angstroms is {} W".format(lambda_2 / 1e-10, energy_from_lambda_2))

