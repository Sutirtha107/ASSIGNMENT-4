with open("output.txt","w+") as f:
    text1 = input("Enter text to write to the file: ")
    f.write(f"{text1}\n")
    print("Data successfully written to output.txt.\n")
    text2 = input("Enter additional text to append: ")
    f.write(f"{text2}\n")
    print("Data successfully appended.\n")
    f.seek(0)
    print(f"Final content of output.txt:\n{f.read()}")