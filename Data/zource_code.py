from distutils.command.clean import clean
from os import write
import re
import csv


def splitToSentences(src, des):
    """
    Parses text data inside of the 'src' file and writes it into the 'des' file.
    """
    f = open(des, "w", encoding="utf-8")

    # splits the texts inside src into paragraphs
    par = [line.strip() for line in src if line.strip() and len(
        line.strip().split()) > 1 and line.strip()[-1] in ".?!'\""]

    # split each paragraph into sentences
    # sentences = par    -> this is the working version
    sentences = []
    for p in par:
        sen = re.split("[.?!]", p.strip())
        for s in sen:
            temp_s = cleanSentence(s)
            if temp_s not in sentences and isSentenceValid(temp_s):
                # append to list if no duplicate and is more than one word
                sentences.append(temp_s)

    # convert sentence list into string
    sentences = "\n".join(sentences)

    # writes the data into the destination file
    f.write(sentences)

    # closes the file
    f.close()


def cleanSentence(s):
    s = s.strip()
    s = re.sub("[\w ]*<.*?>.*?</.*?>", "", s).strip()
    s = re.sub("^\S+:", "", s).strip()
    s = re.sub("^\(.*?\)", "", s, 1).strip()
    s = re.sub("<.*?>", "", s).strip()

    # remove non-alphabet chars and trailing spaces
    s = re.sub("[^a-zA-Z\sáéíóúñÁÉÍÓÚÑ]", "", s).strip()
    s = re.sub("\s+", " ", s)

    return s


def isSentenceValid(s):
    """
    sentence must be more than 1 word and must not only include proper nouns or capitalized words
    """
    words = s.split()
    if len(words) > 1:
        for i in range(1, len(words)):
            if words[i][0].islower():
                return True

    return False


def writeCSV():
    # header of the dataset
    header = ["Text", "Language"]

    # creates the dataset
    with open("phlanguages.csv", "w", encoding="utf-8", newline="") as f:
        # writer for the csv file
        writer = csv.writer(f)
        # writes the header row to the csv
        writer.writerow(header)

        # BIKOL texts
        with open("Bikol.txt", encoding="utf-8") as fbikol:
            bikol = fbikol.read().split("\n")
            # transfers FIRST 20 paragraphs (note: update this)
            for i in range(20):
                # splits the sentences but retains the ending punctuation/s
                sen = [s.strip() for s in re.split(
                    "(\..?|!.?|\?.?|\.\.\..?)", bikol[i]) if s.strip()]
                # adds each sentence and label to the dataset
                for j in range(0, len(sen), 2):
                    if(j+1 < len(sen)):
                        writer.writerow([sen[j]+sen[j+1], "Bikol"])

        # CEBUANO TEXTS
        with open("Cebuano.txt", encoding="utf-8", newline="") as fceb:
            ceb = fceb.read().split("\n")
            # transfer FIRST 350 paragraphs (note: update this)
            for i in range(350):
                # splits the sentences but retains the ending punctuation/s
                sen = [s.strip() for s in re.split(
                    "(\..?|!.?|\?.?|\.\.\..?)", ceb[i]) if s.strip()]
                # adds each sentence and label to the dataset
                for j in range(0, len(sen), 2):
                    if(j+1 < len(sen)):
                        writer.writerow([sen[j]+sen[j+1], "Cebuano"])

        # HILIGAYNON
        with open("Hiligaynon.txt", encoding="utf-8", newline="") as fhili:
            hili = fhili.read().split("\n")
            # transfer FIRST 100 paragraphs (note: update this)
            for i in range(100):
                # splits the sentences but retains the ending punctuation/s
                sen = [s.strip() for s in re.split(
                    "(\..?|!.?|\?.?|\.\.\..?)", hili[i]) if s.strip()]
                # adds each sentence and label to the dataset
                for j in range(0, len(sen), 2):
                    if(j+1 < len(sen)):
                        writer.writerow([sen[j]+sen[j+1], "Hiligaynon"])

        # ILOCANO
        with open("Ilocano.txt", encoding="utf-8", newline="") as filoc:
            iloc = filoc.read().split("\n")
            # transfer FIRST 460 paragraphs (note: update this)
            for i in range(460):
                # splits the sentences but retains the ending punctuation/s
                sen = [s.strip() for s in re.split(
                    "(\..?|!.?|\?.?|\.\.\..?)", iloc[i]) if s.strip()]
                # adds each sentence and label to the dataset
                for j in range(0, len(sen), 2):
                    if(j+1 < len(sen)):
                        writer.writerow([sen[j]+sen[j+1], "Ilocano"])

        # KAPAMPANGAN
        with open("Kapampangan.txt", encoding="utf-8", newline="") as fkap:
            kap = fkap.read().split("\n")
            # transfer FIRST 900 paragraphs (note: update this)
            for i in range(900):
                # splits the sentences but retains the ending punctuation/s
                sen = [s.strip() for s in re.split(
                    "(\..?|!.?|\?.?|\.\.\..?)", kap[i]) if s.strip()]
                # adds each sentence and label to the dataset
                for j in range(0, len(sen), 2):
                    if(j+1 < len(sen)):
                        writer.writerow([sen[j]+sen[j+1], "Kapampangan"])

        # TAGALOG
        with open("Tagalog.txt", encoding="utf-8", newline="") as ftag:
            tag = ftag.read().split("\n")
            # transfer FIRST 350 paragraphs (note: update this)
            for i in range(350):
                # splits the sentences but retains the ending punctuation/s
                sen = [s.strip() for s in re.split(
                    "(\..?|!.?|\?.?|\.\.\..?)", tag[i]) if s.strip()]
                # adds each sentence and label to the dataset
                for j in range(0, len(sen), 2):
                    if(j+1 < len(sen)):
                        writer.writerow([sen[j]+sen[j+1], "Tagalog"])


def main():
    print("hello world")
    # writeCSV()

    # bikol
    file_bikol_lit = open("Bikol_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_bikol_lit, "Bikol-Lit.txt")
    file_bikol_lit.close()

    file_bikol_rel = open("Bikol_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_bikol_rel, "Bikol-Rel.txt")
    file_bikol_rel.close()

    # cebuano
    file_ceb_lit = open("Cebuano_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_ceb_lit, "Cebuano-Lit.txt")
    file_ceb_lit.close()

    file_ceb_rel = open("Cebuano_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_ceb_rel, "Cebuano-Rel.txt")
    file_ceb_rel.close()

    # hiligaynon
    file_hil_lit = open("Hiligaynon_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_hil_lit, "Hiligaynon-Lit.txt")
    file_hil_lit.close()

    file_hil_rel = open("Hiligaynon_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_hil_rel, "Hiligaynon-Rel.txt")
    file_hil_rel.close()

    # ilocano
    file_ilo_lit = open("Ilocano_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_ilo_lit, "Ilocano-Lit.txt")
    file_ilo_lit.close()

    file_ilo_rel = open("Ilocano_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_ilo_rel, "Ilocano-Rel.txt")
    file_ilo_rel.close()

    # kapampangan
    file_kap_lit = open("Kapampangan_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_kap_lit, "Kapampangan-Lit.txt")
    file_kap_lit.close()

    file_kap_rel = open("Kapampangan_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_kap_rel, "Kapampangan-Rel.txt")
    file_kap_rel.close()

    # pangasinense
    file_pan_lit = open("Pangasinense_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_pan_lit, "Pangasinense-Lit.txt")
    file_pan_lit.close()

    file_pan_rel = open("Pangasinense_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_pan_rel, "Pangasinense-Rel.txt")
    file_pan_rel.close()

    # tagalog
    file_tag_lit = open("Tagalog_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_tag_lit, "Tagalog-Lit.txt")
    file_tag_lit.close()

    file_tag_rel = open("Tagalog_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_tag_rel, "Tagalog-Rel.txt")
    file_tag_rel.close()

    # waray
    file_war_lit = open("Waray_Literary_Text.txt", encoding='utf-8')
    splitToSentences(file_war_lit, "Waray-Lit.txt")
    file_war_lit.close()

    file_war_rel = open("Waray_Religious_Text.txt", encoding='utf-8')
    splitToSentences(file_war_rel, "Waray-Rel.txt")
    file_war_rel.close()


if __name__ == "__main__":
    main()
