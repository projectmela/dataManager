# The code here is supposed to create empty directories 
# This is used during fieldwork to create folders for the required datasets
import argparse
import os

def argument_Parser():

    parser = argparse.ArgumentParser(description="The file creates empty folder structure to save session for the day.")
    parser.add_argument("--input", "-i", type=str, help="The path for data")
    parser.add_argument("--date", "-d", type=str, help="Set the date for which the data is to be produced.")
    # This option can be integrated in future if structure changes.
    parser.add_argument("--custom", "-c", type=bool, help="Customize directory names", default=False)

    return parser.parse_args()

def makeDir(dirPath):
    if os.path.exists(dirPath):
        print(f"Already exists : {dirPath}")
        return False
    else:
        os.mkdir(dirPath)
        print(f"Added : {dirPath}")
        return True
    
def make_directories(path, date, session_dir_name, drone_dir_name):
    path_date = os.path.join(path, date)
    dirList = []
    
    makeDir(path_date)

    for session in session_dir_name:   
        makeDir(os.path.join(path_date,session))
        for drone in drone_dir_name:
            makeDir(os.path.join(path_date,session,drone))
    
def main():

    args = argument_Parser()
    lekDir = []
    droneDir = []
    if args.custom:
       lekDir.append(input("Enter Name of Session with lek title e.g. SM_Lek1 or SE_Lek1"))
       droneDir.append(input("Enter combination of drone with position. e.g. PXDX, X is number etc."))
    else:
        lekDir = ["SM_Lek1", "SE_Lek1"]
        droneDir = ["P1D1","P1D2","P2D3","P2D4","P3D5","P3D6"]

    make_directories(args.input, args.date, lekDir, droneDir)

if __name__ == "__main__":
    main()


