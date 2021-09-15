from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://bolt://localhost:7687", username="neo4j", password="Neo_Example")

# Create some nodes with labels
user = db.labels.create("User")

user1 = db.nodes.create(name="Njuguna")
user.add(user1)

user2 = db.nodes.create(name="Otieno")
user.add(user2)

user3 = db.nodes.create(name="Wafula")
user.add(user3)

user4 = db.nodes.create(name="Mutiso")
user.add(user4)



beer = db.labels.create("Beer")
b1 = db.nodes.create(name="Tusker")
b2 = db.nodes.create(name="Pilsner")
b3 = db.nodes.create(name="WhiteCap")
b4 = db.nodes.create(name="Guiness")


# You can associate a label with many nodes in one go like this
beer.add(b1, b2)
beer.add(b3, b4)


#The second step is all about connecting the dots, 
#which in graph DB terminology means creating the relationships.

# User-likes->Beer relationships
user1.relationships.create("likes", b1)
user1.relationships.create("likes", b2)
user2.relationships.create("likes", b1)

user3.relationships.create("likes", b3)
user4.relationships.create("likes", b4)


# Bi-directional relationship?
user1.relationships.create("friends", user2)

#Now run this code from the Neo4j command line and check out the results
#MATCH (n)-[r]->(m) RETURN n, r, m;