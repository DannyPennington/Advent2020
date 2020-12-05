import re

class Passport:
    def __init__(self, byr="0", iyr="0", eyr="0", hgt=" ", hcl=" ", ecl=" ", pid="0", cid="0", valid=False):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
    
    def verify(self):
        hexCodeRegEx = "^#([a-f0-9]{6})"
        successes = 0
        # Check the conditions for each field
        # Birth year
        if (1920 <= int(self.byr) <= 2002):
            successes += 1
            #print("Birth year valid")
        # Issue year
        if (2010 <= int(self.iyr) <= 2020):
            successes += 1
            #print("issue year valid")
        # Expiration year
        if (2010 <= int(self.eyr) <= 2030):
            successes += 1
            #print("expiry year valid")
        # Height 
        if (self.hgt.endswith("cm")):
            if (150 <= int(self.hgt[0:-2]) <=193):
                successes += 1
                #print("height valid cm")
        elif (self.hgt.endswith("in")):
            if (59 <= int(self.hgt[0:-2]) <= 76):
                successes += 1
                #print("height valid in")
        # Hair colour
        if (re.search(hexCodeRegEx, self.hcl)):
            successes += 1
            #print("hair valid")
        # Eye colour
        if (self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            successes += 1
            #print("eyes valid")
        # Passport ID
        if (len(self.pid) == 9):
            successes += 1
            #print("passport id valid")

        # Check all were successful and set as valid
        #print("Successes:", successes)
        if successes >= 7:
            return True
        else:
            return False
            
def parseList(inputList):
    # Go through each item in the list to determine with field it is then return our passport object
    byr_val = "0"
    iyr_val = "0"
    eyr_val = "0"
    hgt_val = " "
    hcl_val = " "
    ecl_val = " "
    pid_val = "0"
    cid_val = "0"
    for i in inputList:
        if i.startswith("byr"):
            byr_val = i[4:]
        elif i.startswith("iyr"):
            iyr_val = i[4:]
        elif i.startswith("eyr"):
            eyr_val = i[4:]
        elif i.startswith("hgt"):
            hgt_val = i[4:]
        elif i.startswith("hcl"):
            hcl_val = i[4:]
        elif i.startswith("ecl"):
            ecl_val = i[4:]
        elif i.startswith("pid"):
            pid_val = i[4:]
        elif i.startswith("cid"):
            cid_val = i[4:]
    
    return Passport(byr = byr_val, iyr = iyr_val, eyr = eyr_val, hgt = hgt_val, hcl = hcl_val, ecl = ecl_val, pid = pid_val, cid = cid_val)

# Read our file and parse it into the format we're expecting
with open("Day4/data.txt", "r") as data:
    lines = data.readlines()

stringInput = "".join(lines)
data = stringInput.split("\n\n")

validCount = 0

# Loop through every item in dataframe
for i in data:

    # Replace any "\n"s with whitespace so we can count the no. fields
    newInput = i.replace("\n", " ")
    fields = newInput.split(" ")
    fields.sort()

    # We only need to check if the passport has at least 7 fields as otherwise it is definitely invalid
    if not (len(fields) < 7):
        passport = parseList(fields)
        if (passport.verify()):
            validCount += 1

print("Number of valid passports:", validCount)
