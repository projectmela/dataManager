import os
import argparse 
import platform

def find_files(directory, file_format):
    
    file_paths = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_format):
                # Append the full path to the list
                file_paths.append(os.path.join(root, file))
                          
    return file_paths

def update_file_name(files, queryDate):
    updatedNames = []
    for file in files: 
        # Check if the basefile name already contains the dates 
        baseFile = os.path.basename(file)
        if baseFile.find(queryDate) >= 0: # Returns -1 when text not found in string
            print("The file names already have a date. No update required.")
            return updatedNames
        # Split the name of the file using the date 
        new_name = queryDate + file.split(queryDate)[1]
        # Create a new name for the file starting with the data
        system = platform.system()
        if system == "Windows":
            new_name = new_name.replace("\\","_")
        elif system == "Linux":
            new_name = new_name.replace("/","_")
        # Save the new name in the list
        updatedNames.append(new_name)
        
    return updatedNames

def rename_files(files, updatedNames):
    if len(files) == len(updatedNames):
        for old,new in zip(files, updatedNames):
            target_directory = os.path.dirname(old)
            new_revised_path = os.path.join(target_directory,new)
            print(f"Changed: {old} -> {new_revised_path}")
            os.rename(old,new_revised_path)


def print_files_from_dir(found_files):
    # printing the files 
    print(f"\nTotal no of files: {len(found_files)} \nNaming sample: {found_files[0]}")

def main():
    parser = argparse.ArgumentParser(description="Print an argument")
    parser.add_argument("--input", "-i", type=str, help="The path for data")
    parser.add_argument("--date", "-d", type=str, help="Set the date for which the data is to be produced.")
    parser.add_argument("--format", "-f", type=str, help="Format of the file", default=".SRT")
    parser.add_argument("--rename", "-r", help="Rename the files", action="store_true", default= False)

    args = parser.parse_args()

    print(f"\n The directory for renmaing: {args.input} \n Query = {args.date} \n File format = {args.format} \n Renaming status : {args.rename}")

    file_format_to_find = args.format
    dir_path = args.input
    dir_path_date = ""
    renaming_status = args.rename 
    date = ""

    # If a data is given for processing renaming find suitable files 
    if args.date:
        date = args.date
        dir_path_date = os.path.join(dir_path, date)
        if not os.path.exists(dir_path_date):
            print(f"The give path does not exist, check path or date \n {dir_path_date}")
            exit(0)
    else:
        #In case when date is not provided take the given path as default
        dir_path_date = dir_path

    # Find the required files in the directory
    found_files = find_files(dir_path_date, file_format_to_find)
    print_files_from_dir(found_files)

    # Update names only if date is given as query
    if date:
        updatedName = update_file_name(found_files, date)
        # Update only if the query names already do not exist in file names, if so then operation is aborted. 
        if len(updatedName):
            print("\n Update can be initiated with following convention.  ")
            print_files_from_dir(updatedName)
        else:
            print("No updated names found, aborting renaming.")
            renaming_status = False
    else:
        print("No specific date given in arguments.")

    print(f"Renaming status : {renaming_status} ")
    if renaming_status == True:
        if len(updatedName):
            # Currently only supports if the length is equal.
            rename_files(found_files,updatedName)
            print("Renaming complete")
            print_files_from_dir(find_files(dir_path_date, file_format_to_find))

    else:
        print("Renaming option is disabled. ")
        


if __name__ == "__main__":
    main()
