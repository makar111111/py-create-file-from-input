def create_file_from_input() -> None:
    file_name: str = input("Enter name of the file: ")
    lines: list[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(f"{file_name}.txt", "w") as file:
        for content_line in lines:
            file.write(content_line + "\n")


create_file_from_input()
