import csv
import string
import names
import random
import datetime

import src.generate
from src.headers import *

NATIONALITIES = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean',
                 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi',
                 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese',
                 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese',
                 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian',
                 'Chilean', 'Chinese', 'Colombian', 'Comoran', 'Congolese', 'Costa Rican', 'Croatian', 'Cuban',
                 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman',
                 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian',
                 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German',
                 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian',
                 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian',
                 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani',
                 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian',
                 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian',
                 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican',
                 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican',
                 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan',
                 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan',
                 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari',
                 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean',
                 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean',
                 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish',
                 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik',
                 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish',
                 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh',
                 'Yemenite', 'Zambian', 'Zimbabwean']

EYE_COLOURS = ['Brown', 'Blue', 'Black', 'Red', 'Pink', 'Purple', 'Green', 'Grey', 'Orange', 'White']

NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

SEX = ["Male", "Female"]

CAR_COLOURS = ["Black", "Blue", "Green", "Purple", "Yellow", "Silver", "Red", "Pink", "Grey", "Orange", "White",
               "Brown", "Cyan"]


###################################################
######### CAR SECTION #############################
###################################################

def get_car_data():
    with open('C:/Users/william/Desktop/gitStuff/Imaginary/src/data/2014.csv', 'r') as file:
        reader = csv.reader(file)
        reader = list(reader)

        return_value = reader[random.randint(0, len(reader) - 1)]
    file.close()
    return return_value


def get_random_car_colour():
    return CAR_COLOURS[random.randint(0, len(CAR_COLOURS) - 1)]


def get_random_annotations():
    pass


def get_random_car_plate(car_object=None):
    letters = string.ascii_uppercase
    first_section = ''.join(random.choice(letters) for i in range(3))
    if car_object is not None:
        if int(car_object.year) >= 2017:
            # 16 februari 2017 tog regeringen beslut om att Transportstyrelsen ska få tilldela registreringsnummer där
            # det sista tecknet blir alfanumeriskt
            second_section = ''
            for i in range(2):
                second_section = second_section + str(random.randint(0, 9))
            second_section = second_section + random.choice(letters)
        else:
            second_section = ''
            for i in range(3):
                second_section = second_section + str(random.randint(0, 9))
    else:
        second_section = ''
        for i in range(2):
            second_section = second_section + str(random.randint(0, 9))
        second_section = second_section + random.choice(letters)

    return first_section + "-" + second_section


class carMaster:
    def __init__(self, owner=None, spec_plate=None):
        data = get_car_data()
        self.model = data[1]
        self.manufacturer = data[2]
        self.colour = get_random_car_colour()
        self.year = data[0]
        self.annotations = None
        self.car_body = data[3]
        if spec_plate is None:
            self.plate = get_random_car_plate(self)
        else:
            self.plate = spec_plate

        if owner is None:
            self.owner = None
        else:
            self.owner = owner

    def get_plate(self):
        return self.plate

    def print_self(self):
        print(self.__dict__)


###################################################
######### IDENTITY SECTION ########################
###################################################


def get_random_height():
    return random.randint(130, 205)


def get_random_nationality():
    return NATIONALITIES[random.randint(0, len(NATIONALITIES) - 1)]


def get_random_age():
    return random.randint(18, 100)


def get_random_eye_colour():
    return EYE_COLOURS[random.randint(0, len(EYE_COLOURS) - 1)]


def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0


def generate_identification_number(years_old: int, gender, length: int = 8):
    # letters = string.digits
    rand_month = random.randint(1, 13)
    if len(str(rand_month)) == 1:
        rand_month = "0" + str(rand_month)
    rand_day = random.randint(1, 31)
    if len(str(rand_day)) == 1:
        rand_day = "0" + str(rand_day)

    born_place = random.randint(0, 99)
    if len(str(born_place)) == 1:
        born_place = "0" + str(born_place)

    cant_bother_with_luhn_number = random.randint(1, 9)

    # C'mon I'm far too tired to do this the right way alright don't judge me.
    # Anyway, this works for now even though it's utterly fucking retarded.
    # But does it look like I care? No. So let it work as long as it does.
    if gender == "Male":
        # Male
        while True:
            gender_num = random.randrange(1, 9)
            if gender_num % 2 == 0:
                pass
            else:
                break
    else:
        # Female
        while True:
            gender_num = random.randrange(1, 9)
            if gender_num % 2 == 0:
                break
            else:
                pass

        # gender_num = random.randrange(1, 9, 2)

    # rand_string = ''.join(random.choice(letters) for i in range(length))
    return ''.join(
        str((datetime.datetime.now().year - years_old)) + str(rand_month) + str(rand_day) + "-" + str(born_place) + str(
            gender_num) + str(cant_bother_with_luhn_number))


def get_random_sex():
    return SEX[random.randint(0, 1)]


def get_car(person_in_question):
    chance = random.randint(0, 10)
    # 50 / 50 Chance kinda-
    if chance >= 5:
        # Create car with plate and return plate

        owned_plate = get_random_car_plate()
        print(owned_plate)
        generated_car = src.generate.generate_vehicle(specific_plate=str(owned_plate), ownership=f"{person_in_question.first_name} {person_in_question.last_name}")
        return owned_plate
    else:
        # No car.
        return False


class personMaster:
    def __init__(self):
        self.sex = get_random_sex()
        if self.sex == "Female":
            self.first_name = names.get_first_name(gender='female')
        else:
            self.first_name = names.get_first_name(gender='male')
        self.last_name = names.get_last_name()
        self.nationality = get_random_nationality()
        self.age = get_random_age()
        self.height = get_random_height()
        self.eye_colour = get_random_eye_colour()
        self.personal_identification_number = generate_identification_number(years_old=self.age, gender=self.sex)
        potential_car = get_car(self)
        if not potential_car:
            self.cars = []
        else:
            self.cars = [potential_car]

    def print_information(self):
        print(self.__dict__)
