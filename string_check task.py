import re

person = {
    "name" : "Srija Saithya",
    "company" : "Hallmark",
    "city" : "Hyderabad",
    "favorite" : "Biryani",
}

story = "my name is srija, and i work in hallmark Global Pvt Ltd. Hyderabad is a city in Telangana. its famous for Biryani. Biryani is a very famous dish which available at any place. Biryani is sold near my place"
final_list = []
search_list = person.values()

for x in search_list:
  for m in re.finditer(x,story):
    list = [x,m.start(),(m.end()-1)]
    final_list.append(list)

print(final_list)

