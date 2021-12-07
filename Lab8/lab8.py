import lightrdf
from nltk import pos_tag
import wget

def onthology_lexicalization_idk():
    parser = lightrdf.Parser()
    # word = input("Input your word:")
    word = 'natural_language_processing'
    file = open('CSO.3.3.owl', 'rb')
    parents_of_word = list()
    for s, p, o in parser.parse(file, format="owl", base_iri=None):
        if o.find(word) != -1 and p.find('superTopicOf') != -1:
            parents_of_word.append(s)
    file.close()

    file = open('CSO.3.3.owl', 'rb')
    for s, p, o in parser.parse(file, format="owl", base_iri=None):
        if (s in parents_of_word or o in parents_of_word) and p.find('superTopicOf') != -1:
            print(s.split('/')[-1] + " superTopicOf " +  o.split('/')[-1])
            
            
def POS_tagging():
    file = open('computer-science.txt', 'r', encoding='utf-8')
    result_file = open('result.txt', 'w')
    text = file.read()
    list_of_phrases = text.split('\n')
    
    
    list_of_phrases = [item for sublist in [x.split('.') for x in list_of_phrases] for item in sublist]
    
    for phrase in list_of_phrases:
        result = pos_tag(phrase.split())
        if len(result) < 3:
            continue
        first = False
        second = False
        third = False
        for _, pos in result:
            if pos.find('NN') != -1 and first == False:
                first = True
            elif pos.find('VB') != -1 and first == True:
                second = True
            elif pos.find('NN') != -1 and second == True:
                third = True
            if third == True:
                result_file.write(phrase + '.\n')
                break


def more_file_extraction(word):
    file = open('CSO.3.3.owl', 'rb')
    parser = lightrdf.Parser()
    for s, p, o in parser.parse(file, format="owl", base_iri=None):
        if o.find(word) != -1:
            return True
    return False


def ultimul_pumct_si_gata():
    file = open('result.txt', 'r')
    file_to_write = open('result2.txt', 'w')
    for line in file:
        for word in line.split():
            if more_file_extraction(word):
                file_to_write.write(line + '\n')
                break
    file.close()

ultimul_pumct_si_gata()