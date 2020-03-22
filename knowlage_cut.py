def check_type(some_data):
	print(type(some_data))


def check_type(some_data):
	data_type = type(some_data)
	return data_type
	pass







def say_hello(name):
	if type(name) == str:
		print("Hello freiend, my name is")


# say_hello("Egor")






service_users = [{"name": "Adrian kulhatsker",  "email": "lamo@gmail.com", "userpick": None},
				 {"name": "A.Jensen", "email": "fuckmylife@dog.com", "userpick": "CyberPepe.png"},
				 {"name": "Azimov", "email": "sdsdsdsd@yandex.ru", "userpick": "OldscoolCompute.jpg"}]




# service_users = ( 

# 	             {"name": "Adrian kulhatsker", "email": "lamo@gmail.com", "userpick": None},
# 				 {"name": "A.Jensen", "email": "fuckmylife@dog.com", "userpick": "CyberPepe.png"},
# 				 {"name": "Azimov", "email": "sdsdsdsd@yandex.ru", "userpick": "OldscoolCompute.jpg"}

# 				 )



####################

# service_users = set([{"name": "Adrian kulhatsker", "email": "lamo@gmail.com", "userpick": None},
# 				     {"name": "A.Jensen", "email": "fuckmylife@dog.com", "userpick": "CyberPepe.png"},
# 				     {"name": "Azimov", "email": "sdsdsdsd@yandex.ru", "userpick": "OldscoolCompute.jpg"}])


# service_users = frozenset([{"name": "Adrian kulhatsker", "email": "lamo@gmail.com", "userpick": None},
# 				 {"name": "A.Jensen", "email": "fuckmylife@dog.com", "userpick": "CyberPepe.png"},
# 				 {"name": "Azimov", "email": "sdsdsdsd@yandex.ru", "userpick": "OldscoolCompute.jpg"}])

########################








new_user = {"name": "Slim Shady", "email": "fuckdetroit@mail.kz", "userpick":"dtr/gtrpr.jpeg"}


def check_unique_fields(user_info):
	if type(user_info) == dict:
	
		if "name" and "email" in user_info.keys():
			if "@" in user_info["email"]:
				return True

			else:
				print("sory, your email ____  in wrong format")
		else:
			print("Please, fill fields 'name' and 'email' in your profile ")

	print("Wrong data type - _____")




# check_unique_fields(new_user)



# def check_unique_fields(user_info):
# 	if type(user_info) == dict:
# 		if "name" and "amail" in user_info.keys():
# 			if "@" in user_info["email"]:
# 				return True
# 			else:
# 				print("Sorry, your email {} not correct".format(new_user["email"]))
# 		else:
# 			print("Please, fill fields 'name' and 'email' in your profile")
	
# 	print("Not correct data type - {}, fkn_idiot!!!".format(type(user_info)))

# # check_unique_fields(new_user)













# def register_new_user(user_info):
# 	if check_unique_fields(user_info):
# 		for user in service_users:
# 			if user_info["name"] == user["name"]:
# 				break
# 				print("Sorry this username already exist")
# 			else:
# 				if user_info["email"] == user["email"]:
# 					break
# 					print("Sorry this username already exist")









def add_new_user(user_info):
	if check_unique_fields(user_info):
		if new_user["name"] not in [user["name"] for user in service_users]:
			if new_user["email"] not in  [user["email"] for user in service_users]:
				service_users.append(user_info)

	





print(service_users)
add_new_user(new_user)
print(service_users)


