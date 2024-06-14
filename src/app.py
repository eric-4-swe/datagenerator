import datagenerators


datagenerators.generate_file_from_types(desc= {
    "fistname": "names",
    "middlename": "names",
    "salary": "numbers"
    
}, num_rows=300, file_name="file2.csv")












# dict_ ={'fistname': ['Noah', 'Benjamin', 'Liam', 'Aiden'], 'middlename': ['Harper', 'Gabriel', 'Sofia', 'Harper'], 'salaries': [1038, 1397, 1148, 1626]}
# # e_dict = {}
# # for key in dict_.keys():
# #     e_dict[key] = None 
    
# # print(e_dict)

# print({key:None for key in dict_.keys()})
# # {'fistname': None, 'middlename': None, 'salaries': None}
    

