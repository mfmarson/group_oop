
#refracting from example in OOP
#adding class using keyword class, name is uppercase first, colon
class Person: 
    #create descriptor
    #name,email,phone are attributes 
    def __init__(self, name, email, phone): #ALWAYS START WITH SELF ---MAKE SURE THERE IS A SPACE BETWEEN DEF AND INIT 
        self.name = name 
        self.email = email
        self.phone = phone
        self.friend = []
        
        
    #this shows defining a method of class (it says "Hi I am ...")  
    def greet(self, person2):
        print(f'Hello {person2.name}, I am {self.name}!') #f string interpolation use {}
        

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name},'s phone number: {self.phone}")
        
    def add_friend(self,friend):
        self.friend.append(friend.name)
    
    
        

    #this is a static method and is applied to the class     
    def is_valid_phone(phone): 
        return len(phone) == 10 
    
#add a new person  
sonny = Person('Sonny', 'sonny@aol.com', '999-867-5309')
jordan = Person("Jordan", "jordan@aol.com", "815-555-1111")



#call who you want to execute greet 
sonny.greet(jordan)
jordan.greet(sonny)
sonny.print_contact_info()

jordan.friends.append(sonny)
sonny.friends.append(jordan)

#sonny and jordan are instances of person class, meaning we have a class called person having 3 attributes and one method (they can greet other people/instances)