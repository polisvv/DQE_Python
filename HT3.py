initial_text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
import re
# count whitespaces
whitespace_cnt = re.findall(' ', initial_text) + re.findall('\t', initial_text) + re.findall('\n', initial_text)
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
# split by dots (before this delete spaces after dots), delete tabs
for i in split_by_enter:
    i = i.replace('\t','').replace('. ','.').split('.')
    paragraph_list.append(i)
    # collect last words for last sentences
    for j in i:
        last_sent.append(j.split()[-1:])
# delete empty elements (due to line between paragraphs)
last_sent = [x for x in last_sent if x]

# collect lists of last words to one list
ls = []
i = 0
while i < len(last_sent):
    for j in last_sent[i]:
        ls.append(j)
    i = i + 1

# create new final list
corrected_list = []
for i in paragraph_list:
    # create list to add sentences with capital letter for every paragraph
    list_cap = []
    for j in i:
        # correct first letter
        j = j.capitalize()
        # add to the list
        list_cap.append(j)
    # add every paragraph to the final list
    corrected_list.append('. '.join(list_cap))
# add last sentence to the final list
corrected_list.append(' '.join(ls).capitalize()+'.')
# convert list to the text
final_text = '\n\t'.join(corrected_list)
print(final_text)
