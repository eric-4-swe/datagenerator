import csv


# e_dict = {}
# for key in dict.keys():
#     e_dict[key] = None 
    


def write_csv(data,file_name, row_num):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = list(data.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(row_num):
            writer.writerow({key:value[i] for key,value in data.items()})
            
    