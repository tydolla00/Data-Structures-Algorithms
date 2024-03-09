import os
# Script to create a new folder with ts,js,cs,py for each DS/algo  
# Will not create if folder already exists
# Allow user to input custom file extensions. 
    # Have default list of extensions and then ask if 
    # they want to add more, and then give the ability to 
    # save new list as default config. 
# create class names already with folder name.

def create_files(folder_name):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

        # Create files with folder name
        file_extensions = ['ts', 'java', 'py', 'cs']
        for ext in file_extensions:
            file_name = os.path.join(folder_name, f"{folder_name}.{ext}")
            with open(file_name, 'w') as f:
                f.write(f"# This is a {ext} file for {folder_name}")
        
        # Write template to Readme 
        file_name = os.path.join(folder_name, "README.md")
        with open(file_name, "w") as file:
            template = f"""
# **{folder_name}**
Description:

# Applications/When to use a {folder_name}
- *item*: description
- 

# Advantages 
- *item*: description
- 

# Disadvantages
- *item*: description
- 

# Support
### Built in ✅ | Not Built In ❌
- **C#**:  [✅] [❌]   
- **Java**: ✅ ❌
- **Python**: ✅ ❌
- **TS**: ✅ ❌
            """
            file.write(template)
    else:
        print("Folder exists already")
    
if __name__ == "__main__":
    folder_name = input("Enter folder name: ")
    create_files(folder_name)
