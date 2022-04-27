# from distutils.command.clean import clean
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


# for reference in case needed
def splitToSen():
    """
    Splits a paragraph into sentences and retains the ending punctuation/s
    """
    text = "<lbl>16</lbl> Mitubag si Jesus: May nag-andam og dakong hikay. Daghan siyag dinapit. <lbl>17</lbl> Gipaadto niya ang katabang aron pag-ingon: 'Dali na mo, andam na ang tanan.' <lbl>18</lbl> Apan morag nagsabot ang tanan sa pagpamalibad. Miingon ang usa: 'Mipalit kog uma nga kinahanglang adtoon ug susihon. Pasensya ka na.' <lbl>19</lbl> Miingon sab ang lain: 'Nakapalit kog lima ka parisang baka nga pang-uma ug pasulayon kog daro. Pasensya ka na.' <lbl>20</lbl> Miingon ang usa pa: 'Bag-o kong nakasal busa, dili makaadto?'"
    sen = [s.strip() for s in re.split(
        "(\..?|!.?|\?.?|\.\.\..?)", text) if s.strip()]

    sentences = []
    for i in range(0, len(sen), 2):
        if(i+1 < len(sen)):
            sentences.append(sen[i]+sen[i+1])

    return sentences


def writeCSV():
    """
    Creates the annotated dataset for LID
    """
    # header of the dataset
    header = ["Text", "Language"]

    # creates the dataset
    with open("phlanguages.csv", "w", encoding="utf-8", newline="") as f:
        # writer for the csv file
        writer = csv.writer(f)
        # writes the header row to the csv
        writer.writerow(header)

        # BIKOL texts: add each sentence/line with a label into the dataset
        with open("Bikol.txt", encoding="utf-8") as fbikol:
            bikol = fbikol.read().split("\n")
            for sentence in bikol:
                writer.writerow([sentence, "Bikol"])

        # CEBUANO texts: add each sentence/line with a label into the dataset
        with open("Cebuano.txt", encoding="utf-8") as fcebuano:
            cebuano = fcebuano.read().split("\n")
            for sentence in cebuano:
                writer.writerow([sentence, "Cebuano"])

        # HILIGAYNON texts: add each sentence/line with a label into the dataset
        with open("Hiligaynon.txt", encoding="utf-8") as fhiligaynon:
            hiligaynon = fhiligaynon.read().split("\n")
            for sentence in hiligaynon:
                writer.writerow([sentence, "Hiligaynon"])

        # ILOCANO texts: add each sentence/line with a label into the dataset
        with open("Ilocano.txt", encoding="utf-8") as filocano:
            ilocano = filocano.read().split("\n")
            for sentence in ilocano:
                writer.writerow([sentence, "Ilocano"])

        # KAPAMPANGAN texts: add each sentence/line with a label into the dataset
        with open("Kapampangan.txt", encoding="utf-8") as fkapampangan:
            kapampangan = fkapampangan.read().split("\n")
            for sentence in kapampangan:
                writer.writerow([sentence, "Kapampangan"])

        # PANGASINENSE texts: add each sentence/line with a label into the dataset
        with open("Pangasinense.txt", encoding="utf-8") as fpangasinense:
            pangasinense = fpangasinense.read().split("\n")
            for sentence in pangasinense:
                writer.writerow([sentence, "Pangasinense"])

        # TAGALOG texts: add each sentence/line with a label into the dataset
        with open("Tagalog.txt", encoding="utf-8") as ftagalog:
            tagalog = ftagalog.read().split("\n")
            for sentence in tagalog:
                writer.writerow([sentence, "Tagalog"])

        # WARAY texts: add each sentence/line with a label into the dataset
        with open("Waray.txt", encoding="utf-8") as fwaray:
            waray = fwaray.read().split("\n")
            for sentence in waray:
                writer.writerow([sentence, "Waray"])


def main():
    print("hello world")
    # writeCSV()

    # # bikol
    # file_bikol_lit = open("Bikol_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_bikol_lit, "Bikol-Lit.txt")
    # file_bikol_lit.close()

    # file_bikol_rel = open("Bikol_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_bikol_rel, "Bikol-Rel.txt")
    # file_bikol_rel.close()

    # # cebuano
    # file_ceb_lit = open("Cebuano_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_ceb_lit, "Cebuano-Lit.txt")
    # file_ceb_lit.close()

    # file_ceb_rel = open("Cebuano_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_ceb_rel, "Cebuano-Rel.txt")
    # file_ceb_rel.close()

    # # hiligaynon
    # file_hil_lit = open("Hiligaynon_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_hil_lit, "Hiligaynon-Lit.txt")
    # file_hil_lit.close()

    # file_hil_rel = open("Hiligaynon_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_hil_rel, "Hiligaynon-Rel.txt")
    # file_hil_rel.close()

    # # ilocano
    # file_ilo_lit = open("Ilocano_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_ilo_lit, "Ilocano-Lit.txt")
    # file_ilo_lit.close()

    # file_ilo_rel = open("Ilocano_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_ilo_rel, "Ilocano-Rel.txt")
    # file_ilo_rel.close()

    # # kapampangan
    # file_kap_lit = open("Kapampangan_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_kap_lit, "Kapampangan-Lit.txt")
    # file_kap_lit.close()

    # file_kap_rel = open("Kapampangan_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_kap_rel, "Kapampangan-Rel.txt")
    # file_kap_rel.close()

    # # pangasinense
    # file_pan_lit = open("Pangasinense_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_pan_lit, "Pangasinense-Lit.txt")
    # file_pan_lit.close()

    # file_pan_rel = open("Pangasinense_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_pan_rel, "Pangasinense-Rel.txt")
    # file_pan_rel.close()

    # # tagalog
    # file_tag_lit = open("Tagalog_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_tag_lit, "Tagalog-Lit.txt")
    # file_tag_lit.close()

    # file_tag_rel = open("Tagalog_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_tag_rel, "Tagalog-Rel.txt")
    # file_tag_rel.close()

    # # waray
    # file_war_lit = open("Waray_Literary_Text.txt", encoding='utf-8')
    # splitToSentences(file_war_lit, "Waray-Lit.txt")
    # file_war_lit.close()

    # file_war_rel = open("Waray_Religious_Text.txt", encoding='utf-8')
    # splitToSentences(file_war_rel, "Waray-Rel.txt")
    # file_war_rel.close()


if __name__ == "__main__":
    main()
