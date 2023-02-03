import pymongo
from misc import personMaster

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["imaginaryMaster"]
mycol = mydb["people"]


total_people = []


def generate_people(amount: int):
    total_people.clear()

    for person in range(0, amount):
        person_obj = personMaster()
        pers_dict = [person_obj]
        # print(person_obj.__dict__)
        # print(pers_dict)
        total_people.append(pers_dict)


def main():
    generate_people(10)
    for people in total_people:
        print(people)
    #
    # for person in total_people:
    #     x = mycol.insert_one(person)


if __name__ == '__main__':
    main()