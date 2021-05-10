import requests
import json
import sqlite3

# მოაქვს მარსზე გადაღებული ფოტოები კონკრეტული თარიღის მითითებისას. მონაცემები იწერება json ფაილსა და მონაცემთა ბაზაში.
key = '6A7O2ghhDhKe1fBnNVDuVglIz04poXa3c1VJDlm7'
date = input("Enter the date in YYYY-M-D format: ")
payload = {'earth_date': date, 'api_key': key}
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
r = requests.get(url, params=payload)
print(r.headers)
print(r.status_code)
json_file = r.text
dict = json.loads(json_file)
str_dict = json.dumps(dict, indent=3)

# json ფაილში ვინახავ წამოღებულ ინფორმაციას
with open("mars_data.json", 'w') as file:
    json.dump(dict, file, indent=3)

# ვუკავშირდები მონაცემთა ბაზას
db = sqlite3.connect("mars.sqlite")
c = db.cursor()

# ვქმნი table-ს სახელად mars. მასში არის სამი სვეტი: თარიღების, როვერების და ლინკების
c.execute("""CREATE TABLE if not exists mars
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        date VARCHAR(50),
        rover VARCHAR(25),
        pic_link VARCHAR(150))
""")


amount_of_pics = len(dict["photos"])
# ციკლი გადის ფოტოების რაოდენობაში და აგროვებს ლინკებს, თარიღებსა და rover-ების სახელებს.
# ეკრანზე გამოდის მხოლოდ თარიღი და ლინკი. ამავდროულად, სამივე მონაცემი გადადის მონაცემთა ბაზაში.
for i in range(amount_of_pics):
    earth_date = dict["photos"][i]["earth_date"]
    pic_link = dict["photos"][i]["img_src"]
    rover = dict["photos"][i]["camera"]["name"]
    print("{} - {}".format(earth_date, pic_link))
    c.execute('INSERT INTO mars (date, rover, pic_link) VALUES (?,?,?)', (earth_date, rover, pic_link))


db.commit()
db.close()

