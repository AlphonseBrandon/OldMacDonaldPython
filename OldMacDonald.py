def main():
    file_name = input("Enter the name of the file listing the animals on Old McDonald's farm: ")
    file_object = open(file_name)
    line = file_object.readline()
    while line != "":
        list_info = line.strip().split(",")
        print(list_info)
        line = file_object.readline() 
    show_song()
    
def show_song():
    index = 0
    for J in range(index,-1,-1):
        animal = list_info([index][0])
        sound = list_info([index][1])
        index = index + 1
        oldMcLine()
        animal_line(animal)
        sound_lines(sound)
               
def eio():
    print("E-I-E-I-O")
        
def oldMcLine():
    print("Old MacDonald had a farm")
    eio()
        
def animal_line(animal):
    print("And on that farm he had a",animal)
    eio()
    
def sound_lines(sound):
    print("With a",sound,sound,"here")
    print("And a", sound,sound,"there")
    print("Here a",sound,"there a",sound)
    print("Everywhere a", sound, sound)
    oldMcLine()
    eio()
        
    
     
main()

