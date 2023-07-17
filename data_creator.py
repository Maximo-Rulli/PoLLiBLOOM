import json


data = """
[ 
]
""".replace("“", '"').replace("”", '"').replace("\n", ' ')

data = json.loads(data)

# Specify the file path and name
file_path = "data.json"

# Open the file in write mode
with open(file_path, "a", encoding='utf-8') as file:
    for i in data:
        # Write JSON data to the file
        json.dump(i, file, ensure_ascii=False)
        file.write(',\n')