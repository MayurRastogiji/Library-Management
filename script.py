import os

def replace_spaces_with_underscores(directory):
    for filename in os.listdir(directory):
        if " " in filename:
            new_filename = filename.replace(" ", "_")
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: "{filename}" -> "{new_filename}"')

if __name__ == "__main__":
    target_dir = input("Enter the directory path: ").strip()
    if os.path.isdir(target_dir):
        replace_spaces_with_underscores(target_dir)
    else:
        print("Invalid directory path.")