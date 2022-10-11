import re

initial_text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# count whitespaces
whitespace_cnt = re.findall('\s', initial_text)
print('Number of whitespace characters is', len(whitespace_cnt))
print('----------------')

# correct misspelling
text_replace_iz = initial_text.lower().replace(' iz ', ' is ')

# split every paragraph
split_by_enter = text_replace_iz.split('\n')
# create an empty list for paragraphs
paragraph_list = []
# create an empty list for last sentence
last_sent = []
# split by dots
for sentence in split_by_enter:
    sentence = sentence.split('. ')
    paragraph_list.append(sentence)
    # collect last words for last sentences
    for word in sentence:
        # skip empty entities
        if len(word.split()[-1:]) > 0:
            last_sent.append(word.split()[-1:])

# collect lists of last words to one list
last_sent_list = []
i = 0
while i < len(last_sent):
    # delete symbols
    for word in last_sent[i]:
        last_sent_list.append(''.join(symb for symb in word if symb not in '.?:!/;'))
    i = i + 1

# create new final list
corrected_list = []
paragraph_cnt = 0
for paragraph in paragraph_list:
    # create list to add sentences with capital letter for every paragraph
    list_cap = []
    for sent in paragraph:
        # correct first letter
        sent = sent.strip().capitalize()
        # add to the list
        list_cap.append(sent)
    # add every paragraph to the final list
    corrected_list.append('. '.join(list_cap))
    # add last sentence to the final list (cnt started from 0, counted empty paragraphs)
    if paragraph_cnt == 3:
        corrected_list.append(' '.join(last_sent_list).capitalize()+'.')
    paragraph_cnt = paragraph_cnt + 1
# convert list to the text
final_text = '\n\t'.join(corrected_list)
print(final_text)
