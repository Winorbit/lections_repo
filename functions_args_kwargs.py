def register_user(username, user_email, userpassword, userpick, user_description):
	# write this data to DB
	pass

# register_user("Testuser", "testemail@.com", "custompass," "custom_pics/users/ssd_1.jpg", "My description")

# register_user("Testuser", "testemail@.com", "custompass")

# register_user("Testuser", "testemail@.com", "zukabazuka_yy", None, None)

# register_user("Testuser", "testemail@.com", "jonediesinthe_e№D","", "", "")


income_new_user_data = {"username":"Miller", 
						"email":"spector@mail.ru", 
						"password":"some_simple_pass", 
						"description":None, 
						"userpick":"my_picture.png"}

# def register_user(username, user_email, userpassword, if not userpick: userpick = "default.png"  user_description):
# 	# write this data to DB
# 	pass



# def register_user(username, user_email, userpassword,  userpick = "default.png",  user_description=""):
# 	pass








# def register_user(username="", user_email="", userpassword=1234567):
# 	print(username)
# 	print(user_email)
# 	print(userpassword)
# 	pass


# register_user()

# register_user(username="Douglas Adams")

# register_user(username="Douglas Adams", userpassword=42)

# register_user(userpassword=42, username="Douglas Adams", user_email="hitchuscker@gmail.com")








# def register_user(username, user_email, userpassword, userpick, user_description):
# 	# write this data to DB
# 	print(username)
# 	pass

# register_user(username, user_email, userpassword, userpick, user_description)



# (username, user_email, userpassword, userpick, user_description)

# username, user_email, userpassword, userpick, user_description




# var = 5


# var


# def register_user(username, user_email, userpassword, userpick, user_description):

# 	аргумент и именем sernam на самом деле просто нулевой элемент тупля, переменная username
# 	а при вызове эта переменная получает свое значение
# 	username = "egor"
# 	ARGUMENTS[0] = username
	
#     print(username) = print(ARGUMENTS[0]) 

# 	pass



# При ВЫЗОВЕ 
# register_user("egor", "egor@emailcom","mypass")

# происходит следующее
# в туплье (username, user_email, userpassword, userpick, user_description)

# первый элемент, usernameб привязвается к "egor"
# username = "egor"

# ввторой - к "email"
# и так далее.


# Поэтому-то такие аргументы тип и называется ПОЗИЦИОННЫМИ.




# def register_user(username="", user_email="", userpassword=1234567):
# 	print(username)
# 	print(user_email)
# 	print(userpassword)
# 	pass









# print("Hello")
# print("Hello", 42)
# print("Hello", 42, 42.5, "Another str")

# def test_args(arg):
# 	pass

# test_args("r")

# test_args( list(1,2,3,4,5, 67, True))






# a = 1
# *a, = 1,2,3,4,"Hello"
# print(a)
# print(type(a))


# a,b, *c = True, None, None, 1, 45.6, "Egor", "", "!!!", 56
# print(a, b)
# print(c)

# a,*b, c = True, None, None, 1, 45.6, "Egor", "", "!!!", 56
# print(b)


# Сработает
# *a, = 1,2,3,4,"Hello"   
# Не сработает
# *a = 1,2,3,4,"Hello"






# test_list = [1,2,3,False, None, 55,6.7]
# print(test_list)
# print(*test_list)


# def test_args(*args):

# 	print(args)


# test_args("Hello!", 42, "BB", False, None, "bprd")




# def show_arg(**dict_arg):
# 	print(dict_arg)

# show_arg(name="Papug", height=1.1, weight=0.2)





def show_arg(**dict_arg):
	print(dict_arg.keys())
	print(dict_arg["message"])

show_arg(name="Papug", height=1.1, weight=0.2, message="Helllo!")




# dict_one = {"age":25, "city":"Nightcity"}
# coords = {"lan":45.67, "lat":98.76}
# new_dict = {**dict_one, **coords}
# print(new_dict)

# def test(arg, arg2, *args, **kwargs)


