import pandas
user_input=input("enter a word: ").upper()

data=pandas.read_csv('NATOalph_Conv/nato_phonetic_alphabet.csv')
phonec_dict={rows.letter:rows.code for (index,rows) in data.iterrows()}
NATO_Words=[phonec_dict[letter] for letter in user_input]
print(NATO_Words)

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key,value)


# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(index)
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.



