#my_file = open("my_file.txt", "r")
#my_file.write(" Hello there this is my first file handling assignment.")
#my_file.write("\n This is week 5 of learning python in plp programme.")
#my_file.write("\n Date: 29/08/2024")
#print(my_file.read())
#my_file.write("\n Python is fun!")
#my_file.write("\n We practice the append,write and read function")
#my_file.write("\n Also including file handling errors")
#my_file.close()
try:
    
    my_file = open("my_file.txt", "a")
    
    
    my_file.write(" Hello there this is my first file handling assignment.")
    my_file.write("\n This is week 5 of learning python in PLP programme.")
    my_file.write("\n Date: 29/08/2024")
    

    print(my_file.read())


    my_file.close()

    
    my_file = open("my_file.txt", "a")
    my_file.write("\n Python is fun!")  
    my_file.write("\n We practice the append, write, and read function")  
    my_file.write("\n Also including file handling errors")  

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You do not have permission to access 'my_file.txt'.")
except IOError as e:
    print(f"An unexpected error occurred: {e}")
finally:
    
    try:
        my_file.close()
        print("File closed successfully.")
    except NameError:
        
        print("File was never opened, so nothing to close.")
    except Exception as e:
        
        print(f"An error occurred while closing the file: {e}")
