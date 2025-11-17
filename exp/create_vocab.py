# read phone_map
with open("phone_map", "r") as f:
    phone_map = f.readlines()

print(len(set([phone.strip().split(" ")[0] for phone in phone_map])))

org_phone_map = [phone.strip().split(" ")[-1] for phone in phone_map]
# remove sil
# org_phone_map = [phone for phone in org_phone_map if phone != "sil"]
new_phone_map = ['_'] + list(set(org_phone_map))

# create vocab_39.txt
with open("vocab_39.txt", "w") as f:
    for phone in new_phone_map:
        f.write(phone + "\n")