class User:
    def __init__(self ,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

#display all user data
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print("Current points:",self.gold_card_points)

#Create a user and ensure same user cannot enroll. Add 200 points with enrollment
    def enroll(self):
        if self.is_rewards_member:
            print("User already exists!")
            return False
        
        self.is_rewards_member = True
        self.gold_card_points = self.gold_card_points + 200
        print(self.display_info)

#Allow users to spend points but ensure the user has enough points to spend
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            return self.gold_card_points
        else:
            self.gold_card_points = self.gold_card_points - amount

#create user instances
person_1 = User("Kenny","Lam","kenny@email.com", 31)

#test methods
person_1.enroll()
person_1.spend_points(250)
person_1.display_info()

