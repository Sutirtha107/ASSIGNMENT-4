try:
    with open("sample.txt","r") as f:
        print("Reading file content:")
        for i,line in enumerate(f.read().splitlines()):
            print(f"Line {i+1}: {line}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")