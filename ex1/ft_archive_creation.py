import sys

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if (len(sys.argv) == 1):
        print("Usage: python3 ft_ancient_text.py <file_path>")
    else:
        file_path = sys.argv[1]
        print(f"Accessing file '{file_path}'")
        try:
            file = open(file_path, "r")
            print("---\n")
            content = file.read()
            print(content)
            print("\n---")
            file.close()
            print(f"File '{file_path}' closed.\n")
            new_content_list = [x + "#\n" for x in content.split("\n")]
            new_content = ""
            for line in new_content_list:
                new_content += line
            new_content = new_content[:-1]
            print("Transform data:")
            print("---\n")
            print(new_content)
            print("\n---")
            new_file_name = input("Enter new file name (or empty): ")
            if (new_file_name):
                print(f"Saving data to '{new_file_name}'")
                file = open(new_file_name, "x")
                file.write(new_content)
                file.close()
                print(f"Data saved in file '{new_file_name}'.")
            else:
                print("Not saving data.")
        except Exception as e:
            print(f"Error opening '{file_path}': {e}")
