import csv
def createPreset(rarityLevels):
    rarities = {}
    with open("rarity.tsv", 'r', encoding="utf-8") as tsvfile:
        reader = csv.reader(tsvfile, delimiter="\t")
        for row in reader: 
            rarities[int(row[0])] = rarityLevels[int(row[1])]
    return rarities

def readFromCustom(filename="custom.tsv"):
    custom = {}
    with open(filename, 'r', encoding="utf-8") as tsvfile:
        reader = csv.reader(tsvfile, delimiter="\t")
        for row in reader: 
            custom[int(row[0])] = int(row[4])
    return custom
        