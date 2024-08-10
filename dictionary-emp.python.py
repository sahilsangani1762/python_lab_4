emp = {
    "id": 10,
    "name": "sahil",
    "designation": "Software Engineer",
    "salary": 85000
}

print("Original dictionary:")
print(emp)

if "designation" in emp:
    del emp["designation"]

emp["name"] = "nevil"

print("\nUpdated dictionary:")
print(emp)
