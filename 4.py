import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validations = {
        "cid": (lambda x : True),
        "byr": (lambda x : 1920 <= int(x) <= 2002),
        "iyr": (lambda x : 2010 <= int(x) <= 2020),
        "eyr": (lambda x : 2020 <= int(x) <= 2030),
        "hgt": (lambda x : (150 if "cm" in x else 59) <= int(re.search(r"\d+", x)[0]) <= (193 if "cm" in x else 76)),
        "hcl": (lambda x : re.match(r"#[0-9a-f]{6}$", x)),
        "ecl": (lambda x : x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
        "pid": (lambda x : re.match(r"[0-9]{9}$", x))
        }

valid1 = 0
valid2 = 0

#Part 1
for block in open("4.in").read().strip().split('\n\n'):
    if sum([1 if req in block else 0 for req in required]) == len(required):
        valid1 += 1

#Part 2
for block in open("4.in").read().strip().split('\n\n'):
    passport = "".join(block.replace('\n', ' '))
    if sum([1 if req in passport else 0 for req in required]) == len(required):
        pairs = [entry.split(":") for entry in passport.split(" ")]
        if all([validations[key](value) for key, value in pairs]):
            valid2 += 1



print(valid1)
print(valid2)
