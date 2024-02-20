import pandas as p


def saveData():
    print("Saving data")
    myData = [
        {
            "name": "Alice Johnson",
            "address": "123 Main Street, Cityville, State, ZIP",
            "phone": "(555) 123-4567",
        },
        {
            "name": "Bob Smith",
            "address": "456 Elm Street, Townsville, State, ZIP",
            "phone": "(555) 234-5678",
        },
        {
            "name": "Charlie Brown",
            "address": "789 Oak Avenue, Villagetown, State, ZIP",
            "phone": "(555) 345-6789",
        },
        {
            "name": "Diana Martinez",
            "address": "321 Maple Lane, Hamletsville, State, ZIP",
            "phone": "(555) 456-7890",
        },
        {
            "name": "Ethan Taylor",
            "address": "654 Pine Road, Suburbia, State, ZIP",
            "phone": "(555) 567-8901",
        },
        {
            "name": "Fiona Lee",
            "address": "987 Cedar Street, Ruralville, State, ZIP",
            "phone": "(555) 678-9012",
        },
        {
            "name": "George Wilson",
            "address": "210 Elm Avenue, Metropolis, State, ZIP",
            "phone": "(555) 789-0123",
        },
        {
            "name": "Hannah Adams",
            "address": "543 Birch Drive, Townburg, State, ZIP",
            "phone": "(555) 890-1234",
        },
        {
            "name": "Ian Thompson",
            "address": "876 Oak Lane, Cityburg, State, ZIP",
            "phone": "(555) 901-2345",
        },
        {
            "name": "Jessica Rodriguez",
            "address": "109 Pine Street, Villagetown, State, ZIP",
            "phone": "(555) 012-3456",
        },
    ]

    try:
        p.DataFrame(myData).to_excel("record.xlsx")
        print("working")
    except Exception as e:
        print(e)


def readData():
    try:
        df = p.read_excel("record.xlsx")
        records = df.to_dict("records")
        # Convert DataFrame to list of dictionaries
        return records
    except Exception as e:
        print(e)
        return []


if __name__ == "__main__":
    # saveData()
    x = readData()
    print("Name\t\t\tAddress\t\t\tContact\n")
    for y in x:
        print(y["name"] + "\t\t" + y["address"] + "\t\t" + y["phone"] + "\n")
