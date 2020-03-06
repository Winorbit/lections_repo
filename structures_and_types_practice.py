REQ_CURS = ("USD", "EUR", "RUB")


some_test_val = 11111111

currencys_descrition_info = [{"Cur_ID":1,
"Cur_ParentID":1,
"Cur_Code":"008",
"Cur_Abbreviation":"ALL",
"Cur_Name":"Албанский лек",
"Cur_Name_Bel":"Албанскі лек",
"Cur_Name_Eng":"Albanian Lek",
"Cur_QuotName":"1 Албанский лек",
"Cur_QuotName_Bel":"1 Албанскі лек",
"Cur_QuotName_Eng":"1 Albanian Lek",
"Cur_NameMulti":"",
"Cur_Name_BelMulti":"",
"Cur_Name_EngMulti":"",
"Cur_Scale":1,
"Cur_Periodicity":1,
"Cur_DateStart":"1991-01-01T00:00:00",
"Cur_DateEnd":"2007-11-30T00:00:00"},

{"Cur_ID":2,
"Cur_ParentID":2,
"Cur_Code":"012",
"Cur_Abbreviation":"DZD",
"Cur_Name":"Алжирский динар",
"Cur_Name_Bel":"Алжырскі дынар",
"Cur_Name_Eng":"Algerian Dinar",
"Cur_QuotName":"1 Алжирский динар",
"Cur_QuotName_Bel":"1 Алжырскі дынар",
"Cur_QuotName_Eng":"1 Algerian Dinar",
"Cur_NameMulti":"","Cur_Name_BelMulti":"",
"Cur_Name_EngMulti":"",
"Cur_Scale":1,
"Cur_Periodicity":1,
"Cur_DateStart":"1991-01-01T00:00:00",
"Cur_DateEnd":"2016-06-30T00:00:00"},

{"Cur_ID":5,
"Cur_ParentID":5,
"Cur_Code":"032",
"Cur_Abbreviation":"ARS",
"Cur_Name":"Аргентинское песо",
"Cur_Name_Bel":"Аргенцінскае песа",
"Cur_Name_Eng":"Argentine Peso",
"Cur_QuotName":"1 Аргентинское песо",
"Cur_QuotName_Bel":"1 Аргенцінскае песа",
"Cur_QuotName_Eng":"1 Argentine Peso",
"Cur_NameMulti":"",
"Cur_Name_BelMulti":"",
"Cur_Name_EngMulti":"",
"Cur_Scale":1,
"Cur_Periodicity":1,
"Cur_DateStart":"1991-01-01T00:00:00",
"Cur_DateEnd":"2016-06-30T00:00:00"},

{"Cur_ID":6,
"Cur_ParentID":6,
"Cur_Code":"100",
"Cur_Abbreviation":"BGL",
"Cur_Name":"Болгарский лев",
"Cur_Name_Bel":"Балгарскі леў",
"Cur_Name_Eng":"Bulgarian Lev",
"Cur_QuotName":"1 болгарский лев",
"Cur_QuotName_Bel":"1 балгарскі леў",
"Cur_QuotName_Eng":"1 Bulgarian Lev",
"Cur_NameMulti":"болгарский лев",
"Cur_Name_BelMulti":"балгарскі леў",
"Cur_Name_EngMulti":"Bulgarian Lev",
"Cur_Scale":1,"Cur_Periodicity":0,
"Cur_DateStart":"1991-01-01T00:00:00",
"Cur_DateEnd":"2002-12-31T00:00:00"},
]


tesd_curr_dict = {"Cur_ID":6,
"Cur_ParentID":6,
"Cur_Code":"100",
"Cur_Abbreviation":"BGL",
"Cur_Name":"Болгарский лев",
"Cur_Name_Bel":"Балгарскі леў",
"Cur_Name_Eng":"Bulgarian Lev",
"Cur_QuotName":"1 болгарский лев",
"Cur_QuotName_Bel":"1 балгарскі леў",
"Cur_QuotName_Eng":"1 Bulgarian Lev",
"Cur_NameMulti":"болгарский лев",
"Cur_Name_BelMulti":"балгарскі леў",
"Cur_Name_EngMulti":"Bulgarian Lev",
"Cur_Scale":1,"Cur_Periodicity":0,
"Cur_DateStart":"1991-01-01T00:00:00",
"Cur_DateEnd":"2002-12-31T00:00:00"}


new_currencies_info = []

for curr_info in currencys_descrition_info:

	cur_id = curr_info["Cur_ID"]

	curr_abrev = curr_info["Cur_Abbreviation"]

	new_curr_info = {curr_abrev : cur_id}

	new_currencies_info.append(new_curr_info)




for curr_info in currencys_descrition_info:
	transformed_dict = {curr_info["Cur_Abbreviation"]: curr_info["Cur_ID"]}
	new_currencies_info.append(transformed_dict)



new_currencies_info = [{'USD': 145}, {'RUB': 298}, {'EUR': 292}, {'ALL': 1}, {'DZD': 2}, {'ARS': 5}, {'BGL': 6}]


currency_info = {
				"USD": {"Cur_ID":145,"Date":"2020-02-27T00:00:00","Cur_Abbreviation":"USD","Cur_Scale":1,"Cur_Name":"Доллар США","Cur_OfficialRate":2.2378},
				"RUB": {"Cur_ID":298,"Date":"2020-02-27T00:00:00","Cur_Abbreviation":"RUB","Cur_Scale":100,"Cur_Name":"Российских рублей","Cur_OfficialRate":3.4137},
				"EUR": {"Cur_ID":292,"Date":"2020-02-27T00:00:00","Cur_Abbreviation":"EUR","Cur_Scale":1,"Cur_Name":"Евро","Cur_OfficialRate":2.4334},
				 }

for curr in new_currencies_info:

	CUR_ABR = list(curr.keys())[0]

	if CUR_ABR in REQ_CURS:
		
		rate = currency_info[CUR_ABR]["Cur_OfficialRate"]
		scale = currency_info[CUR_ABR]["Cur_Scale"]
			
		message = "Сегодняшний курс : "+CUR_ABR+" "+str(rate/scale)

		print(message)
			
