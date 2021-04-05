import nltk
import os
import docx2txt
from pdfminer.high_level import extract_text

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

# def pdf_extract_text(pdf_path):
# 	return extract_text(pdf_path)

# def main():
# 	print(pdf_extract_text('/home/dell/Downloads/SrishtiJain 2021.pdf'))

# main()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_text_from_docx(docx_path):
	txt = docx2txt.process(docx_path)
	if txt:
		return txt.replace('\t', ' ')
	return None

def extract_names(txt):
	person_names = []
	for sent in nltk.sent_tokenize(txt):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			if hasattr(chunk, 'label') and (chunk.label() == 'PERSON' or chunk.label() == 'ORGANIZATION'):
				person_names.append(
					' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
				)
	return person_names 

def extract_projects(txt):

	projects_list = []
	projects_list1 = []
	projects_list2 = []
	projects_list3 = []
	heading_list = [
		# 'Education',
		# 'Experience',
		# 'Publications',
		# 'Leadership',
		# 'Extra-Curricular',
		# 'Skills',
		# 'Certifications',
		'Projects' or 'PROJECTS',
		'Leadership',
		'Certifications' or 'CERTIFICATIONS',
		'STRENGTHS',
		'Strengths',
		'SKILLS',
	]
	para = {}
	s=""
	prev_heading = "first Heading"
	for i in nltk.word_tokenize(txt):
		if i in heading_list:
			para[prev_heading] = s
			s = ""
			prev_heading = i
		else:
			s = s + " " + i

	# import pdb;pdb.set_trace()
	i='Projects'
	print("key",i)
	print("value",para[i])
	


	count = 1
	projects_dict = {}

	projects_title = ""
	project_sent = ""
	# for sent in para:
	for sent in nltk.sent_tokenize(para[i]):
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				# chunk = list(chunk)
				if hasattr(chunk, 'label') and (chunk.label() == 'ORGANIZATION' or 'PERSON'):
						chunk_leave = chunk.leaves()
						# import pdb;pdb.set_trace()
						for word,tag in chunk_leave:
							# projects_title = []
							# projects_title.append(word)
							projects_title = word
						print("projects_title",projects_title)
				project_sent = sent
				projects_dict[projects_title] = project_sent

					# while count<=3:
					# print(chunk.label())
					# pass
					# projects_list.append(sent)
						# count += 1
				# print("sent",sent," ")
	print("projects_dict",projects_dict)
	return projects_list			


def main():
	text = extract_text_from_docx('/home/ebabu/Downloads/Sanidhya_CV-converted.docx')
	names = extract_names(text)
	if names:
		print("names",names)
		# print(names[0])
	projects = extract_projects(text)
	print("projects",projects)

main()


