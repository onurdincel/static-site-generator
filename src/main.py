import os
import shutil

def copy_directory_contents(source, destination):
    if os.path.exists(destination):
        print(f"Deleting: {destination}")
        shutil.rmtree(destination)
    os.mkdir(destination)
    print(f"Creating: {destination}")

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copy file: {dest_path}")
        elif os.path.isdir(src_path):
            copy_directory_contents(src_path, dest_path)



def main():
    copy_directory_contents("static", "public")

if __name__ == "__main__":
    main()
