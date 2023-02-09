from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# print(contacts_list)



def name_normalization(contacts_list):
  name_normal_list = []
  search_phone = r'(8|\+7)\s*\(*(\d{1,3})\)*(\s|\-)*(\d{1,3})(\s|\-)*(\d{1,2})(\s|\-)*(\d{1,2})'
  pattern_phone = r'+7(\2)\4-\6-\8'
  search_phone_ext = r'(\(*)(доб.)(\s*)(\d+)(\)*)'
  pattern_phone_ext = r'\2\4'
  search_1 = r'\,{1,}'
  search_2 = r'\s|,'
  search_3 = r'\,$'

  for i in contacts_list:
    c_l = ",".join(i)
    resault_1 = re.sub(search_1, ",", c_l)
    resault_2 = re.sub(search_2, ",", resault_1, count=2)
    resault_3 = re.sub(search_3, "", resault_2)
    resault_phone = re.sub(search_phone, pattern_phone, resault_3)
    resault_phone_ext = re.sub(search_phone_ext, pattern_phone_ext, resault_phone).split(",")
    name_normal_list.append(resault_phone_ext)

  return name_normal_list

def delete_duplicates_contact(new_contacts_list):
  resault = []
  index = []
  for list_1 in new_contacts_list:
    ind = new_contacts_list.index(list_1)
    for list_2 in new_contacts_list:
      if list_1[:2] == list_2[:2] and list_1[2:] != list_2[2:]:
        cum = list_1 + list_2
        temp = []
        for count in cum:
          if count not in temp:
            temp.append(count)
        resault.append(temp)
        index.append(ind)

  index.reverse()
  for c in index:
    del (new_contacts_list[c])
  new_contacts_list.append(resault[1])
  new_contacts_list.append(resault[2])
  return new_contacts_list

name_normal_list = name_normalization(contacts_list)
new_contacts_list = delete_duplicates_contact(name_normal_list)
# print(new_contacts_list)
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)
