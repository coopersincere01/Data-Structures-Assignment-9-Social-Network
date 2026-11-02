class Person:
    """
    Represents a person in the social network.

    Attributes:
        name (str): The person's name.
        friends (list): A list of Person objects.

    Methods:
        add_friend(friend): Adds a person to the friends list.
    """

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Prevent duplicate friendships
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """
    Represents a social network using an adjacency list.

    Attributes:
        people (dict): Stores each person by their name.

    Methods:
        add_person(name): Adds a person to the network.
        add_friendship(person1_name, person2_name): Connects two people.
        print_network(): Displays everyone and their friends.
    """

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        # Add a new person if they are not already in the network
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} is already in the network.")

    def add_friendship(self, person1_name, person2_name):
        # Make sure both people exist before creating a friendship
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # A person cannot be friends with themselves
        if person1 == person2:
            print("A person cannot be friends with themselves.")
            return

        # Create the friendship in both directions
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        # Display each person and their connections
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            friends = ", ".join(friend_names)

            print(f"{name} is friends with: {friends}")


# Test the social network
if __name__ == "__main__":

    network = SocialNetwork()

    # Add six people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Create eight friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Test adding a person who already exists
    print("TEST: Duplicate Person")
    network.add_person("Alex")

    # Test creating a friendship with someone who does not exist
    print("\nTEST: Missing Person")
    network.add_friendship("Jordan", "Johnny")

    # Test adding the same friendship again
    print("\nTEST: Duplicate Friendship")
    network.add_friendship("Alex", "Jordan")

    # Test someone trying to be friends with themselves
    print("\nTEST: Self-Friendship")
    network.add_friendship("Alex", "Alex")

    # Print the completed network
    print("\nSOCIAL NETWORK")
    network.print_network()

    # Check the number of people and unique friendships
    total_people = len(network.people)
    total_friendships = sum(
        len(person.friends) for person in network.people.values()
    ) // 2

    print(f"\nTotal People: {total_people}")
    print(f"Total Friendships: {total_friendships}")


# DESIGN MEMO
#
# I chose a graph for this social network because friendships are based
# on connections between people rather than a specific order or hierarchy.
# Each person represents a node and each friendship represents an
# undirected edge. I used a dictionary to store the people and a list
# inside each Person object to keep track of their connections. This
# allows friendships to be represented in both directions.
#
# A regular list could store everyone's names, but it would not clearly
# show how people are connected. I would need additional information to
# track each relationship. A tree wouldn't be as effective either
# because it follows a parent-child structure. Social networks don't
# have one main person that everyone branches from. People can have
# multiple friendships including connections that form cycles.
#
# One performance trade off I noticed is that adding people is fairly
# efficient because the dictionary allows quick lookups by name.
# Adding friendships takes additional work because the program checks
# each person's friends list to prevent duplicate connections. As the
# number of friends increases these checks can take longer. Printing
# the network also requires going through every person and their
# friendships so larger networks take more time to display.
#
# I think an adjacency list is a better choice than an adjacency matrix
# for this project because it only stores existing connections. Most
# people are not friends with every other person in a social network,
# so storing every possible relationship would waste memory. This
# structure keeps the project simple while allowing the network to grow.
