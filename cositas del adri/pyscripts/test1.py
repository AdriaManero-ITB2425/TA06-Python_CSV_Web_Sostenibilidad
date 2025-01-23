import logging

# Configure the logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s - module:%(module)s, function:%(funcName)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

def string_exists_in_file(filepath, target_string):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if target_string in line:
                    return True
        return False
    except FileNotFoundError:
        logging.error(f"The file '{filepath}' was not found.")
    except PermissionError:
        logging.error(f"Permission denied to read the file '{filepath}'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return False

filepath = "/pyscripts/data_sample/precip.P1.MIROC5.RCP60.2006-2100.REGRESION.dat"
target_string = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"

# Check if the string exists in the file
if string_exists_in_file(filepath, target_string):
    print(0)
else:
    logging.info(f"The string '{target_string}' was not found in the file '{filepath}'.")
    print(1)

