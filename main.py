import os
# Script to create a new folder with ts,js,cs,py for each algo  


def create_files(folder_name):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create files with folder name
    file_extensions = ['ts', 'js', 'py', 'cs']
    for ext in file_extensions:
        file_name = os.path.join(folder_name, f"{folder_name}.{ext}")
        with open(file_name, 'w') as f:
            f.write(f"# This is a {ext} file for {folder_name}")
             
    file_name = os.path.join(folder_name, "README.md")
    with open(file_name, "w") as file:
       file.write("Sample Readme")
    
if __name__ == "__main__":
    folder_name = input("Enter folder name: ")
    create_files(folder_name)
