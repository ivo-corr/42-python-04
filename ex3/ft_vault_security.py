def secure_archive(
        filepath: str, action: int = 0, content: str = ""
                  ) -> tuple[True | False, str]:
    try:
        if (action == 0):
            with open(filepath, "r") as file:
                content = file.read()
                return (True, content)
        elif (action == 1):
            with open(filepath, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("not/existing/file"), end="\n\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/root/x.txt"), end="\n\n")
    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("test.txt")
    print(content, end="\n\n")
    if (content[0]):
        print("Using 'secure_archive' to write previous content to a new file:")
        print(secure_archive("new.txt", 1, content[1]))
