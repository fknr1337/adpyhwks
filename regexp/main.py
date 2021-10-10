import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_list = []

def add_firs_last_sur(list):
    for i in contacts_list:
        if i[1] != '' and i[2] != '':
            names = f'{i[0], i[1], i[2]}'
            reg = "".join(a for a in names if a.isalpha())
            data_name = re.sub(r"([А-Я])", r" \1", reg).split()
            list.append(data_name)
        elif i[2] == '':
            names = f'{i[0], i[1]}'
            reg = "".join(a for a in names if a.isalpha())
            data_name = re.sub(r"([А-Я])", r" \1", reg).split()
            if len(data_name) != 3:
                data_name.append("")
            list.append(data_name)

def add_organization(list):
    i = 0
    for a in contacts_list:
        org = a[3]
        pos = a[4]
        list[i].append(org)
        list[i].append(pos)
        i += 1

def add_phones(list):
    i = 0
    for a in contacts_list:
        phone_num_old = a[5]
        phone_mask = \
            '(\+7|8)(\s*)(\(?)(\d{3})(\)?)(\s*)(\-*)(\d{3})(-*)(\d{2})(-*)(\d{2})(\s*)(\(?)(\s?(доб)?)(\.?)(\s*)(\d*)(\)?)'
        new_phone_num = re.sub(phone_mask, r'+7(\4)\8-\10-\12\13\15\17\19', phone_num_old)
        list[i].append(new_phone_num)
        i += 1

def add_emails(list):
    i = 0
    for a in contacts_list:
        email = a[6]
        list[i].append(email)
        i += 1

def make_final_data(list):
    result = []

    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][0] == list[j][0]:
                list[i] = [x or y for x, y in zip(list[i], list[j])]
        if list[i] not in result:
            result.append(list[i])
    return result

def write_new_book(result):
    with open("phonebook.csv", "w") as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(result)

if __name__ == '__main__':
    add_firs_last_sur(new_list)
    add_organization(new_list)
    add_phones(new_list)
    add_emails(new_list)
    write_new_book(make_final_data(new_list))
    print(new_list)