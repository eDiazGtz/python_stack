#Data Types
    # boolean
    # float
    # int
    # String
    # list
    # objects
    # tuples

# name = 2
# lst=[]
# range(int(len(lst)/2))

#typecasting --- type of something into another type
# name = "edgar" + str(1)
# "edgar1"

numbers = [2, 6, 20, 999]

# print(numbers[3])

hero = {
    'first_name':'Link',
    'last_name':'Hyrule',
    'email':'link@hyrule.gov',
    'favorite_numbers':[3, 7, 5, 19],
	'numOfDungeonsCleared':3,
    'favorite_num': 999,
    'inventory' : {'accessory' : "deku stick", "weapon" : "sword", "shield" : "wooden shield"}
}

for val in hero['inventory'].values():
    print(val)

# print(hero['inventory']['weapon'])

# print(user['favorite_numbers'][1])

users = {
    'link' : {'first_name':'Link','last_name':'Hyrule'},
    'ganon' : {'first_name':'Ganon','last_name':'Gerudo'},
    'zelda' : {'first_name':'Princess','last_name':'Zelda'},
}

# for i_know, what_you_did_last_summer in users.items():
#     print(what_you_did_last_summer['first_name'])

# print(users)
# print(users[0])
# print(users[0]['first_name'])

for user in users: #for each_value in list:
    print(user['first_name'])

# print(user)