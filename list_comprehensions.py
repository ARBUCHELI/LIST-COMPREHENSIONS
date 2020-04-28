scores = {
             "Rick Sanchez": 70, #dictionary
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

#Creation of the list that retrieves the names of the people with score >= 65
passed = [name for name, score in scores.items() if score >=65]


# write your list comprehension here
print(passed)
