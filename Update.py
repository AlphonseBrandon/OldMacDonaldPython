def main():
    file = "OldMacDonald.csv"

    with open(file) as file_object:
        line = file_object.readline()
        
        while line != "":
            list_info = line.strip().split(",")
            print(list_info)
