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
            print("---")
            file.close()
            print(f"File '{file_path}' closed.")
        except Exception as e:
            print(f"Error opening '{file_path}': {e}")
