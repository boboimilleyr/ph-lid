import csv
import random


def writeCSV():
    """
    Creates the annotated dataset for LID
    """
    # header of the dataset
    header = ["Text", "Language"]

    # creates the dataset
    with open("phlanguages_samples.csv", "w", encoding="utf-8", newline="") as f:
        # writer for the csv file
        writer = csv.writer(f)
        # writes the header row to the csv
        writer.writerow(header)

        # BIKOL texts: add each sentence/line with a label into the dataset
        with open("Bikol.txt", encoding="utf-8") as fbikol:
            bikol = fbikol.read().split("\n")
            # shuffle the data
            random.shuffle(bikol)
            # get only the first 8000 sentences
            bikol = bikol[:8000]
            for sentence in bikol:
                writer.writerow([sentence, "Bikol"])

        # CEBUANO texts: add each sentence/line with a label into the dataset
        with open("Cebuano.txt", encoding="utf-8") as fcebuano:
            cebuano = fcebuano.read().split("\n")
            # shuffle the data
            random.shuffle(cebuano)
            # get only the first 8000 sentences
            cebuano = cebuano[:8000]
            for sentence in cebuano:
                writer.writerow([sentence, "Cebuano"])

        # HILIGAYNON texts: add each sentence/line with a label into the dataset
        with open("Hiligaynon.txt", encoding="utf-8") as fhiligaynon:
            hiligaynon = fhiligaynon.read().split("\n")
            # shuffle the data
            random.shuffle(hiligaynon)
            # get only the first 8000 sentences
            hiligaynon = hiligaynon[:8000]
            for sentence in hiligaynon:
                writer.writerow([sentence, "Hiligaynon"])

        # ILOCANO texts: add each sentence/line with a label into the dataset
        with open("Ilocano.txt", encoding="utf-8") as filocano:
            ilocano = filocano.read().split("\n")
            # shuffle the data
            random.shuffle(ilocano)
            # get only the first 8000 sentences
            ilocano = ilocano[:8000]
            for sentence in ilocano:
                writer.writerow([sentence, "Ilocano"])

        # KAPAMPANGAN texts: add each sentence/line with a label into the dataset
        with open("Kapampangan.txt", encoding="utf-8") as fkapampangan:
            kapampangan = fkapampangan.read().split("\n")
            # shuffle the data
            random.shuffle(kapampangan)
            # get only the first 8000 sentences
            kapampangan = kapampangan[:8000]
            for sentence in kapampangan:
                writer.writerow([sentence, "Kapampangan"])

        # PANGASINENSE texts: add each sentence/line with a label into the dataset
        with open("Pangasinense.txt", encoding="utf-8") as fpangasinense:
            pangasinense = fpangasinense.read().split("\n")
            # shuffle the data
            random.shuffle(pangasinense)
            # get only the first 8000 sentences
            pangasinense = pangasinense[:8000]
            for sentence in pangasinense:
                writer.writerow([sentence, "Pangasinense"])

        # TAGALOG texts: add each sentence/line with a label into the dataset
        with open("Tagalog.txt", encoding="utf-8") as ftagalog:
            tagalog = ftagalog.read().split("\n")
            # shuffle the data
            random.shuffle(tagalog)
            # get only the first 8000 sentences
            tagalog = tagalog[:8000]
            for sentence in tagalog:
                writer.writerow([sentence, "Tagalog"])

        # WARAY texts: add each sentence/line with a label into the dataset
        with open("Waray.txt", encoding="utf-8") as fwaray:
            waray = fwaray.read().split("\n")
            # shuffle the data
            random.shuffle(waray)
            # get only the first 8000 sentences
            waray = waray[:8000]
            for sentence in waray:
                writer.writerow([sentence, "Waray"])


print("hellowwww")
writeCSV()
