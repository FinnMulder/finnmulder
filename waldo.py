import random
stoel = 0
people = ["eef","joris","bart","nick","finn","Waldo","jim","pieter", "shane","jens","tjidde","sem","damian","isabelle","amber", "bo", "bas","jasper","chiel", "mees"]
random.shuffle(people)
for w in people:
    stoel += 4
    if w == "Waldo":
        print(people)
        print('Waldo is op stoel', stoel, 'Gevonden!')
        break
