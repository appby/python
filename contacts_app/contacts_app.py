import os

contacts={	              "Name":"",
			      "Surname":"",
			      "Phone":"",
			      "Job":""	}

result_text=""
path=r"YOUR_PATH" #sample --> /home/Py/contacts_app
take_dir_cnt=len(os.listdir(path))

try:
	for i in list(contacts.keys()):
		if i=="Phone":
			contacts[i]=int(input(i+": "))
		else:
			contacts[i]=input(i+": ")

	for keys, values in contacts.items():
		result_text+="{}: {}\n".format(keys,values)

	try:
		with open("contacts_{}.txt".format(take_dir_cnt),"w+") as f:
			f.write(result_text)
		print("Record has been created successfully.")
	except:
		print("An error occurred while creating the file, inform admin.")
except:
	print("There was an error writing the phone value, try again!")
