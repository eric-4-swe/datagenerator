from generators import generate_names, generate_numbers
from writter import write_csv


def generate_file_from_types(desc, num_rows, file_name):
    data = desc.copy()
    for k , v in desc.items():
        if v == "names":
            data[k] = [generate_names() for i in range(num_rows)]
        if  v == "numbers":
            data[k] = [generate_numbers(1000, 2000) for i in range(num_rows)]
            
    write_csv(data, file_name, num_rows)
            
        
