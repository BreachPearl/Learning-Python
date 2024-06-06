student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Covert scores into grades.
for student in student_scores:
  score = student_scores[student]           #getting the scores of the student by calling the key in the student score dictionary 
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    
print(student_grades)

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",               #dictionary_name={key:value}   #this is the basic syteax of dictionary
  "Function": "A piece of code that you can easily call over and over again.",
}
#Create an empty dictionary.
empty_dictionary = {}
#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."                #the way to add is dictionary_name[key]=value
#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#Lets see how nesting works:
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary using lists
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
travel_log["France"].append("lyon")    #to add something to the list we use " append "
print(travel_log)

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]