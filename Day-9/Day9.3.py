#Nesting of Dictionaries and lists

# normal dictionary
capitals = {
    "France" : "Paris",
    "Germany": "Berlin"
}

#Nested Dictionaries in Dictionary
travel_log = {
    "India" : {"cities_visited": ["Hyderabad", "Chandigarh", "Mumbai","Bangalore"], "total_visits":12}
}
# print(travel_log)


#Nested Dictionaries in a List
# Nested as [{Key : [List], key2:{Dict} },{Key : value , key2:value } ]
travel_log1 = [
    {
    "country" :"India", 
     "cities_visited": ["Hyderabad", "Chandigarh", "Mumbai","Bangalore"], 
     "total_visits":12,
     },
]
for key in travel_log1:
    print(key["country"])
    print(key["cities_visited"])
    print(key["total_visits"])
    for cities in key["cities_visited"]:
        print(cities)
