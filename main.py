import requests
import random
import os

# Create people directory if it doesn't exist
people_dir = ".\\people"
if not os.path.exists(people_dir):
    os.makedirs(people_dir)

# Load names
with open(r".\firstnames.txt", 'r') as first_names_file:
    first_names = [name.strip() for name in first_names_file.readlines()]
with open(r".\lastnames.txt", 'r') as last_names_file:
    last_names = [name.strip() for name in last_names_file.readlines()]

def get_fake_person_image(output_path):
    r = requests.get("https://thispersondoesnotexist.com/", headers={"User-Agent": "Mozilla/5.0"})
    if r.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(r.content)

def create_fake_person():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Clean up name and make dir
    person_dir = os.path.join(people_dir, f"{first_name}_{last_name}")
    os.makedirs(person_dir, exist_ok=True)

    image_path = os.path.join(person_dir, "image.jpeg")
    get_fake_person_image(image_path)
    return first_name, last_name

# Example run
amount = 0
while True:
    input_amount = input("Enter amount of fake people to generate: ")
    try: amount = int(input_amount)
    except Exception: pass

    if amount > 0: break
    else: print("Please enter a valid number")

# Seperator
print("\nGenerating people...\n")

# Create people and print out names
for i in range(amount):
    first_name, last_name = create_fake_person()
    print(f"[{i+1}] - {first_name} {last_name}")

# Generation done, wait for user to exit program.
print("\nFake people generated!")
input("Press ENTER to exit")
