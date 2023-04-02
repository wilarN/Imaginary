import bisect
import csv
import hashlib
import random
import string
import uuid

import names
import datetime

import src_files.headers as head
from faker import Faker
import src_files.globals as glob
import src_files.generate as gen

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

DUMMY_BANKS = [
    {"name": "Hanshin Banking Corporation", "location": "Osaka, Japan", "postal_code": "541-8570"},
    {"name": "Indonesia Eximbank", "location": "Jakarta, Indonesia", "postal_code": "12190"},
    {"name": "Bank of China", "location": "Beijing, China", "postal_code": "100818"},
    {"name": "Korea Development Bank", "location": "Seoul, South Korea", "postal_code": "04510"},
    {"name": "KfW Bankengruppe", "location": "Frankfurt, Germany", "postal_code": "60325"},
    {"name": "Industrial and Commercial Bank of China", "location": "Beijing, China", "postal_code": "100033"},
    {"name": "Hua Xia Bank", "location": "Beijing, China", "postal_code": "100033"},
    {"name": "Mitsubishi UFJ Financial Group", "location": "Tokyo, Japan", "postal_code": "100-8324"},
    {"name": "Bank of Tokyo-Mitsubishi UFJ", "location": "Tokyo, Japan", "postal_code": "100-0005"},
    {"name": "Mizuho Financial Group", "location": "Tokyo, Japan", "postal_code": "100-8141"},
    {"name": "National Australia Bank", "location": "Melbourne, Australia", "postal_code": "3000"},
    {"name": "Commonwealth Bank of Australia", "location": "Sydney, Australia", "postal_code": "2000"},
    {"name": "Westpac Banking Corporation", "location": "Sydney, Australia", "postal_code": "2000"},
    {"name": "National Bank of Canada", "location": "Montreal, Canada", "postal_code": "H3C 3X6"},
    {"name": "Scotiabank", "location": "Toronto, Canada", "postal_code": "M5H 1H1"}
]

ANNOTATIONS_AND_CRIMES = ["Cybercrime", "Human Smuggling", "Human Trafficking", "Illegal Possession Of Firearms",
                          "Cannabis Cultivation", "Fraud",
                          "Real Estate", "Benefit Fraud", "Evasion Of Social Insurance Payments",
                          "Crime At Travellers' Sites", "Theft",
                          "Driving Under The Influence", "Speeding", "Red Light Violation",
                          "Driver’s License Suspension", "Aggravated Assault", "Kidnapping",
                          "Manslaughter: Involuntary", "Money Laundering", "Manslaughter: Voluntary", "Child Abuse",
                          "Credit / Debit Card Fraud",
                          "Prostitution", "Domestic Violence", "Disturbing The Peace", "Rape",
                          "Drug Trafficking / Distribution",
                          "Vandalism", "Wire Fraud", "Identity Theft", "Homicide", "Hate Crimes", "Harassment"]

JOBS = ['Software Developer', 'Physician',
        'Information Security Analyst', 'Data Scientist', 'IT Manager',
        'Statistician', 'Marketing Manager', 'Financial Manager', 'Database Administrator',
        'Physical Therapist', 'Operations Manager', 'Nurse Practitioner',
        'Speech-Language Pathologist', 'Psychologist', 'Web Developer',
        'Accountant', 'Occupational Therapist', 'Civil Engineer',
        'Human Resources Manager', 'Sales Manager', 'Mechanical Engineer',
        'Industrial Engineer', 'Management Analyst', 'Electrical Engineer',
        'Market Research Analyst', 'Business Operations Manager',
        'Financial Analyst', 'Medical and Health Services Manager',
        'Construction Manager', 'Diagnostic Medical Sonographer', 'Dentist',
        'Pharmacist', 'Physician Assistant', 'Computer Systems Analyst',
        'Software Quality Assurance Engineer', 'Technical Writer',
        'Physical Therapist Assistant', 'IT Security Specialist',
        'Computer Network Architect', 'Public Relations Specialist',
        'Lawyer', 'Social Worker', 'Software Applications Developer',
        'Market Researcher', 'Computer Programmer', 'Computer and Information Research Scientist',
        'Graphic Designer', 'Management Accountant', 'Environmental Engineer']

EDUCATION = ["Primary school", "Secondary school", "Vocational education", "Associate's degree",
                 "Bachelor's degree in Arts", "Bachelor's degree in Science",
                 "Bachelor's degree in Engineering", "Bachelor's degree in Business",
                 "Bachelor's degree in Education", "Bachelor's degree in Nursing",
                 "Master's degree in Arts", "Master's degree in Science",
                 "Master's degree in Engineering", "Master's degree in Business",
                 "Master's degree in Education", "Master's degree in Nursing",
                 "Doctoral degree"]


AGE_RANGES = [0, 18, 25, 35, 45, 55, 65, 75, 100]
PROBABILITIES = [0.0, 0.4, 0.5, 0.3, 0.25, 0.2, 0.15, 0.1, 0.01]


# CRIME_PROBABILITY = {
# # [ AGE AND UP : PROBABILITY 0.0 - 1.0 ]
#     0 : 0.0,
#     18: 0.4,
#     25: 0.5,
#     35: 0.3,
#     45: 0.25,
#     55: 0.2,
#     65: 0.15,
#     75: 0.1
# }


BANK_ACCOUNT_TYPES = ['Checking Account', 'Savings Account', 'Money Market Account',
                      'Certificate of Deposit', 'Individual Retirement Account', 'Credit Account']

fake = Faker()
PHONE_NUMBERS = []


def generate_phone_numbers():
    for i in range(50):
        num = fake.phone_number()
        if not num[0] == "+":
            num = "+" + num
        PHONE_NUMBERS.append(num)


generate_phone_numbers()

###################################################
######### CAR SECTION #############################
###################################################

global_car_data_path = head.os.path.join(head.os.path.dirname(__file__), 'data\\')

CAR_FILES = []

for path in head.os.listdir(global_car_data_path):
    # check if current path is a file
    if head.os.path.isfile(head.os.path.join(global_car_data_path, path)):
        CAR_FILES.append(head.os.path.join(head.os.path.dirname(__file__), 'data\\' + path))
    # print (head.os.path.join (head.os.path.dirname(__file__), 'data\\'+path))


# input()

def get_car_data():
    # print(global_car_data_path)
    selected_file = CAR_FILES[head.random.randint(0, len(CAR_FILES) - 1)]
    with open(f"{selected_file}", 'r') as file:
        reader = csv.reader(file)
        reader = list(reader)

        return_value = reader[head.random.randint(0, len(reader) - 1)]
    file.close()
    return return_value


def get_random_car_colour():
    return CAR_COLOURS[head.random.randint(0, len(CAR_COLOURS) - 1)]


def get_random_car_plate(car_object=None):
    letters = string.ascii_uppercase
    first_section = ''.join(head.random.choice(letters) for i in range(3))
    if car_object is not None:
        if int(car_object.year) >= 2017:
            # 16 februari 2017 tog regeringen beslut om att Transportstyrelsen ska få tilldela registreringsnummer där
            # det sista tecknet blir alfanumeriskt
            second_section = ''
            for i in range(2):
                second_section = second_section + str(head.random.randint(0, 9))
            second_section = second_section + head.random.choice(letters)
        else:
            second_section = ''
            for i in range(3):
                second_section = second_section + str(head.random.randint(0, 9))
    else:
        second_section = ''
        for i in range(2):
            second_section = second_section + str(head.random.randint(0, 9))
        second_section = second_section + head.random.choice(letters)

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
    return head.random.randint(130, 205)


def get_random_nationality():
    return NATIONALITIES[head.random.randint(0, len(NATIONALITIES) - 1)]


def get_random_age():
    return head.random.randint(18, 100)


def get_random_eye_colour():
    return EYE_COLOURS[head.random.randint(0, len(EYE_COLOURS) - 1)]


def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0


def generate_identification_number(years_old: int, gender, length: int = 8):
    # letters = string.digits
    rand_month = head.random.randint(1, 13)
    if len(str(rand_month)) == 1:
        rand_month = "0" + str(rand_month)
    rand_day = head.random.randint(1, 31)
    if len(str(rand_day)) == 1:
        rand_day = "0" + str(rand_day)

    born_place = head.random.randint(0, 99)
    if len(str(born_place)) == 1:
        born_place = "0" + str(born_place)

    cant_bother_with_luhn_number = head.random.randint(1, 9)

    # C'mon I'm far too tired to do this the right way alright don't judge me.
    # Anyway, this works for now even though it's utterly fucking retarded.
    # But does it look like I care? No. So let it work as long as it does.
    if gender == "Male":
        # Male
        while True:
            gender_num = head.random.randrange(1, 9)
            if gender_num % 2 == 0:
                pass
            else:
                break
    else:
        # Female
        while True:
            gender_num = head.random.randrange(1, 9)
            if gender_num % 2 == 0:
                break
            else:
                pass

        # gender_num = head.random.randrange(1, 9, 2)

    # rand_string = ''.join(head.random.choice(letters) for i in range(length))
    return ''.join(
        str((datetime.datetime.now().year - years_old)) + str(rand_month) + str(rand_day) + "-" + str(born_place) + str(
            gender_num) + str(cant_bother_with_luhn_number))


def get_random_sex():
    return SEX[head.random.randint(0, 1)]


def get_car(person_in_question):
    chance = head.random.randint(0, 10)
    # 50 / 50 Chance kinda-
    if chance >= 5:
        # Create car with plate and return plate

        owned_plate = get_random_car_plate()
        print(owned_plate)
        generated_car = gen.generate_vehicle(specific_plate=str(owned_plate),
                                             ownership=f"{person_in_question.first_name} {person_in_question.last_name}")
        return owned_plate
    else:
        # No car.
        return False


def get_record_and_annotations(age_person):
    temp_total_records = []
    prob_index = bisect.bisect_right(AGE_RANGES, age_person) - 1
    prob = PROBABILITIES[prob_index]

    if head.random.uniform(0.0, 1.0) <= prob:
        # Generate records based on probability for this age range.
        for i in range(3):
            chance = head.random.randint(0, 10)
            if chance <= 3:
                # Get the record from the list for this particular person.
                temp_total_records.append(head.random.choice(ANNOTATIONS_AND_CRIMES))
            else:
                # No record for this person.
                pass
        return temp_total_records
    else:
        return temp_total_records


def get_bank_accounts(f_name, l_name):
    accounts = []
    account_num = head.random.randint(1, 4)
    for i in range(account_num):
        generated_account_num = generate_account_number(account_owner=str(f_name + l_name))
        accounts.append(bank_account(ownership=f_name + " " + l_name, bank_account_num=generated_account_num))
    for i in accounts:
        print(i.account_ownership)

    return accounts


def get_already_existing_phone_numbers(num_to_check):
    existing_customer = glob.mycolPhone.find_one({"phone_numbers": {"$in": [num_to_check]}})
    if existing_customer is not None:
        if len(existing_customer) > 0:
            # Already exists
            return True
        else:
            # Unique
            return False
    else:
        # Unique
        return False


def get_random_job(self):
    if head.random.uniform(0.6, 0.9) >= 0.6:
        return random.choice(JOBS)
    else:
        return ""


def get_random_education():
    if head.random.uniform(0.6, 0.9) >= 0.6:
        return random.choice(EDUCATION)
    else:
        return ""


def get_phone_number(self):
    chance = head.random.randint(0, 10)
    # 50 / 50 Chance kinda-
    if chance >= 5:
        while True:
            # Get phone number
            num = fake.phone_number()
            if not num[0] == "+":
                num = "+" + num

            if get_already_existing_phone_numbers(num):
                pass
            else:
                # Use generate phone number and insert into the phone database and add connection between person and number.
                if num.__contains__("x"):
                    num = num.split("x")[0]
                if num.__contains__("."):
                    num.replace(".", "-")
                phone_number = phone(owner=self.first_name + " " + self.last_name, number=num)
                glob.mycolPhone.insert_one(phone_number.__dict__)
                return num
    else:
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
        self.record_and_annotations = get_record_and_annotations(age_person=self.age)
        self.personal_identification_number = generate_identification_number(years_old=self.age, gender=self.sex)
        potential_car = get_car(self)
        if not potential_car:
            self.cars = []
        else:
            self.cars = [potential_car]
        self.job = get_random_job(self)
        self.education = get_random_education()
        self.bank_accounts = get_bank_accounts(f_name=self.first_name, l_name=self.last_name)
        potential_phone = get_phone_number(self)
        if not potential_phone:
            self.phone_numbers = []
        else:
            self.phone_numbers = [potential_phone]

    def fix_bank_account_numbers_for_insertion(self):
        new_list = []
        for account in self.bank_accounts:
            new_list.append(account.account_identification)
        self.bank_accounts = new_list

    def print_information(self):
        print(self.__dict__)


###################################################
######### BANK SECTION     ########################
###################################################

def generate_account_number(account_owner):
    hashed = hashlib.sha256(str(account_owner + uuid.uuid4().hex).encode('utf-8')).hexdigest()
    return hashed


def get_account_type():
    return head.random.choice(BANK_ACCOUNT_TYPES)


def get_account_balance():
    amount_sec = head.random.randint(0, 10)
    if (amount_sec >= 8):
        return head.random.randint(20000, 3999999)
    elif (2 < amount_sec < 5):
        return head.random.randint(20000, 600000)
    else:
        return head.random.randint(10000, 20000)


def get_bank_account_location():
    selected_bank = head.random.choice(DUMMY_BANKS)
    fixed_string = selected_bank["name"] + " - " + selected_bank[
        "location"] + f"({selected_bank['postal_code']})[{head.random.choice(PHONE_NUMBERS)}]"
    return fixed_string


class bank_account:
    def __init__(self, ownership, bank_account_num):
        self.account_ownership = ownership
        self.account_identification = bank_account_num
        self.balance = get_account_balance()
        self.account_location = get_bank_account_location()
        self.account_type = get_account_type()


class phone:
    def __init__(self, owner, number):
        self.ownership = owner
        self.registered_number = number
