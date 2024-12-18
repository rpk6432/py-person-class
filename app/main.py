class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        name, age = person["name"], person["age"]
        Person(name, age)

    for person in people:
        name = person["name"]
        spouse = person.get("wife") or person.get("husband")
        if spouse:
            setattr(Person.people[name],
                    "wife" if "wife" in person else "husband",
                    Person.people[spouse])

    return list(Person.people.values())
