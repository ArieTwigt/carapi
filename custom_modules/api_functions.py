import requests


def get_car_by_plate(plate):
    resp = requests.get(f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate}")
    resp_dict = resp.json()
    if len(resp_dict) == 0:
        return None
    
    car = resp_dict[0]
    return car


def get_random_cars_brand(brand, color):
    resp = requests.get(f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}&eerste_kleur={color}")
    resp_list = resp.json()
    return resp_list


    
