import time

name=input("Your Name:\n").strip()
age=int(input("Your Age:\n"))
city=input("City You Live in:\n").strip()
food=input("Your Favorite Food:\n").strip()
colour=input("Your Favorite Colour:\n").strip()
animal=input("Your Spirite Animal:\n").strip()
act=input("one thing You Love Doing:\n").strip()
str_age= str(age)
total_month = age*12

#age_tag
if age<30:
    age_tag="🧩You belong to the 'Adventurer' tribe."
   
elif age<=20:
    age_tag="🧩You belong to the 'Young Explorer' tribe."
else:
    age_tag="🧩You belong to the 'WISE OWL' tribe."
    
#security_code
pcode =name[:2].upper() + str_age[0:1] + animal[0].upper() + colour[0].lower() 

print("🧠 Know Your Personality")

time.sleep(3)

print("✨ Let's discover who you really are with some fun data magic!")

time.sleep(3)
print("🔍 Scanning colors, foods, and animal energies...")

time.sleep(2)

print("💫 Calculating your personality type using complex non-scientific logic...")

print(f"🎉 Hey {name.upper()}, here's your fun personality report!")

print("="*60)
print(f"🌆You're from {city.title()}, a place of dreams!")
print(f"🍿You love {food} and enjoy doing {act}.")
print(f"🎨You vibe with the color {colour.upper()} and your spirit animal is the {animal}.")
print(f"📅You've lived approximately {total_month} months already.")
print(f"{age_tag}")

print(f"🔐Your Secret Personality Code is:{pcode} ")

print("="*60)

print("💡 Time to explore more hobbies? You’ve got hidden sparks waiting!")

print("🌈 You are officially certified as: FUNKY AND FABULOUS! 😎")
