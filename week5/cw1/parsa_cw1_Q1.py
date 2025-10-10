# name = input("enter some names?")
# name = name.replace(" ", ",")
# name.split(",")
# name.lower()
# a_names = [name for name in name if name == "a" if len(name) > 3]
# name.sort(name)
# def writing () :
#     with open(name.txt , 'w'  ) as f :
#         f.write(name)
#         print("file saved successfully with X names ")
#         f.close()

def writing():
    names = input("Enter some names: ")

    names = names.strip().split(",")
    names = [name.strip().lower() for name in names if name]


    filtered_names = [name for name in names if name.startswith('a') and len(name) > 3]

    filtered_names.sort()

    with open("names.txt", "w") as f:
        for name in filtered_names:
            f.write(name)
        f.write(f"Total names saved: {len(filtered_names)}")
    print(f"File saved successfully with {len(filtered_names)} names.")
writing()
