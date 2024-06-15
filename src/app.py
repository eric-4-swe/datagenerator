import datagenerators

desc= {
    "fistname": "names",
    "middlename": "names",
    "salary": "numbers"
    
}


num_rows=3000



file_name="nam.csv"



datagenerators.generate_file_from_types(desc, num_rows, file_name)












# dict_ ={'fistname': ['Noah', 'Benjamin', 'Liam', 'Aiden'], 'middlename': ['Harper', 'Gabriel', 'Sofia', 'Harper'], 'salaries': [1038, 1397, 1148, 1626]}
# # e_dict = {}
# # for key in dict_.keys():
# #     e_dict[key] = None 
    
# # print(e_dict)

# print({key:None for key in dict_.keys()})
# # {'fistname': None, 'middlename': None, 'salaries': None}
    

