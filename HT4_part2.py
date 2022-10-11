import re

initial_text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


def count_whitespaces(txt):
    whitespace_cnt = re.findall('\s', txt)
    return len(whitespace_cnt)

def correct_misspelling(incorrect_word, correct_word):
    text_replace_iz = initial_text.lower().replace(' ' + incorrect_word + ' ', ' ' + correct_word + ' ')
    return text_replace_iz

def collect_last_words(txt):
    last_word_list = re.findall('(\w+)[:.|!?…]', txt)
    return last_word_list

def capitalize_and_append_sent(txt_list, paragraph_num):
    paragraph_list = []                                             # create an empty list for last sentence
    for paragraph in txt_list:
        sentences = paragraph.split('. ')
        paragraph_list.append(sentences)
    corrected_list = []                                        # create new final list
    paragraph_cnt = 0
    for paragraph in paragraph_list:
        list_cap = []                                          # create list to add sentences with capital letter for every paragraph
        for sent in paragraph:
            sent = sent.strip().capitalize()                   # correct first letter
            list_cap.append(sent)                              # add to the list
        corrected_list.append('. '.join(list_cap))             # add every paragraph to the final list
        if paragraph_cnt == paragraph_num:                     # add last sentence to the final list (cnt started from 0, counted empty paragraphs)
            corrected_list.append(' '.join(last_words_list).capitalize()+'.')
        paragraph_cnt = paragraph_cnt + 1
    final_text = '\n\t'.join(corrected_list)                    # convert list to the text
    return final_text

print('Number of whitespace characters is', count_whitespaces(initial_text))
print('----------------')
text_replace_iz = correct_misspelling('iz', 'is')
last_words_list = collect_last_words(text_replace_iz)
split_by_enter = text_replace_iz.split('\n')                    # split every paragraph

print(capitalize_and_append_sent(split_by_enter, 3))
