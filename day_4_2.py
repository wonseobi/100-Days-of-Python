# Lists in Python

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
    "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
    "Hawaii"
]

# Replace an item or element inside the list.
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# Print the whole list variable INCLUDING the altered item or element.
states_of_america.append("Monterrey")
print(states_of_america)

#
states_of_america.extend["Randomland", "New state", "Whateverland"]
print(states_of_america)