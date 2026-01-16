import pickle

# -------------------------------------------------
# User class represents a simple user object
# -------------------------------------------------
class User:
    def __init__(self, name, age, height):
        # Initialize object attributes
        self.name = name
        self.age = age
        self.height = height

    def give_info(self):
        # Print user information
        print(f"{self.name} : {self.age} : {self.height}")

    def increase_age(self, age):
        # Increase user's age by the given value
        self.age += age


# -------------------------------------------------
# Creating User objects
# -------------------------------------------------
u1 = User("Nirzar", 21, 180)
u2 = User("Ansh", 25, 200)

# -------------------------------------------------
# Displaying and modifying object data BEFORE pickling
# -------------------------------------------------
u1.give_info()
u1.increase_age(6)
u1.give_info()

# -------------------------------------------------
# PICKLING (SERIALIZATION TO FILE)
# pickle.dump() stores Python objects in binary format
# into a file for later retrieval
# -------------------------------------------------

with open("userdata.pickle", "wb") as file:
    pickle.dump(u1, file)  # Store first User object
    pickle.dump(u2, file)  # Store second User object


# -------------------------------------------------
# UNPICKLING (DESERIALIZATION FROM FILE)
# pickle.load() reads ONE object at a time from the file
# -------------------------------------------------

with open("userdata.pickle", "rb") as file:
    user1 = pickle.load(file)  # Load first object
    user2 = pickle.load(file)  # Load second object


# -------------------------------------------------
# Displaying information AFTER unpickling
# -------------------------------------------------
print("After pickling:")
user1.give_info()
user2.give_info()


# -------------------------------------------------
# PICKLING WITHOUT FILE (USING dumps & loads)
# pickle.dumps() → converts object to bytes (in memory)
# pickle.loads() → converts bytes back to object
# -------------------------------------------------

print("Without file (in-memory pickling):")

# Store multiple objects inside a list
users = [u1, u2]

# Convert objects to binary bytes (no file involved)
temp_storage = pickle.dumps(users)

# Restore objects from binary bytes
new_users = pickle.loads(temp_storage)

# Use restored objects
for u in new_users:
    u.give_info()
