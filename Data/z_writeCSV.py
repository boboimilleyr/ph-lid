from asyncore import write
import csv
import random


def writeCSV():
    # header of the dataset
    header = ["Text", "Language"]
    languages = ["Bikol", "Cebuano", "Hiligaynon", "Ilocano",
                 "Kapampangan", "Pangasinense", "Tagalog", "Waray"]

    # creates the dataset
    with open("phlanguages_samples.csv", "w", encoding="utf-8", newline="") as f:
        # writer for the csv file
        writer = csv.writer(f)
        # writes the header row to the csv
        writer.writerow(header)

        for lang in languages:
            fname_lit = lang + "-Lit.txt"
            fname_rel = lang + "-Rel.txt"

            lit_sen = getSentences(fname_lit, 2500)
            for sen in lit_sen:
                writer.writerow([sen, lang])

            rel_sen = getSentences(fname_rel, 2500)
            for sen in rel_sen:
                writer.writerow([sen, lang])


def getSentences(fname, size):
    """
    Creates the annotated dataset for LID
    """
    # add each sentence/line of text file with a label into the dataset
    with open(fname, encoding="utf-8") as f:
        sentences = f.read().split("\n")
        # shuffle the data
        random.shuffle(sentences)
        # get only the first 8000 sentences
        sentences = sentences[:size]
        return sentences


print("hellowwww")
writeCSV()
