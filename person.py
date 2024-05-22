class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        self.unique_greeted.append(other_person.name)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, friend):
        self.friends.append(friend.name)

    def num_of_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: Name - {}, Email - {}, Phone - {}'.format(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        uniques = set(self.unique_greeted)
        uniques_greeted = list(uniques)
        print(len(uniques_greeted))

Sonny = Person('sonny@hotmail.com', '483-485-4948')
Jordan = Person('jordan@aol.com', '495-586-3456')


