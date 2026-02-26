import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Steps:

# Parse the JSON string using json.loads()
# data becomes a python dictionary
data = json.loads(sampleJson)
print(f"Full dict: {data}")

# Access and print the employee's salary
salary = data['company']['employee']['payable']['salary']
print(f"Salary: {salary}")

# Add a "birth_date" key to the employee with value "1990-05-15"
data['company']['employee']['birth_date'] = "1990-05-15"
print(f"Full modified dict: {data}")

# Save the modified data to a file called employee.json using json.dump() with indent=2
# Read the file back and print it to verify
with open("employee.json", "w") as f:
    json.dump(data, f, indent=2)

# Expected output:
# Salary: 7000
# Modified data saved to employee.json
# Verified — birth_date: 1990-05-15

# Step 5 

