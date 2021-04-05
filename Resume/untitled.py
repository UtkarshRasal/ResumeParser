




import re
import nltk
import docx2txt
from pdfminer.high_level import extract_text
from nltk.tokenize import sent_tokenize, word_tokenize
from resume_parser import resumeparse
from datetime import datetime
from dateparser.search import search_dates
from dateutil import relativedelta

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_text_from_docx(docx_path):
	txt = docx2txt.process(docx_path)
	if txt:
		return txt.replace('\t', ' ')
	return None


def extract_experience(txt):

	heading_list = [
		'experience',
		'employment',
		'technical',
		'publications',
		'educational',
		'projects',
	]
	year_key = {}
	s = ""
	prev_heading = "first Heading"
	for i in nltk.word_tokenize(txt.lower()):
		if i in heading_list:
			year_key[prev_heading] = s
			s = " "
			prev_heading = i
		else:
			s = s + " " + i

	# import pdb;pdb.set_trace()
	experience_months = []
	for key in year_key:
		# import pdb;pdb.set_trace()
		if key in heading_list:
			i=key
			break
	print("iiiii",i)
	# 	experience_months.append(re.findall(r'[A-Z]\w+\s\d+',year_key[i]))

	import pdb;pdb.set_trace()
	date_data = search_dates(year_key[i])
	for edate in date_data:
		experience_months.append(re.findall(r'[a-z]\w+\s\d+',str(edate[0])))
	rvs_date=experience_months[::-1]
	rvs_date=list(filter(None,rvs_date))
	n=2
	n1=0
	n2=2
	monthss=[]
	yearss=[]
	start_date = " "
	end_date = " "
	time_difference = " "
	for k in range(0,len(rvs_date),n):
		val = rvs_date[n1:n2]
		
		try:
			start_date = datetime.strptime(val[0][0], "%B %Y")
			end_date = datetime.strptime(val[1][0], "%B %Y")
			time_difference = relativedelta.relativedelta(start_date,end_date)
		except:
			start_date = datetime.strptime(val[0][0], "%B %Y")
			end_date = datetime.now()
			time_difference = relativedelta.relativedelta(end_date,start_date)
		if time_difference.months:
			monthss.append(time_difference.months)
		if time_difference.years:
			yearss.append(time_difference.years)
		n1+=2
		n2+=2
	print("months",monthss,"years",yearss)
	get_year = ""
	get_month = ""
	# if monthss:
	# 	# import pdb;pdb.set_trace()
	# 	sum_of_month = sum(monthss)
	# 	get_year = sum_of_month//12

	# 	get_month = sum_of_month%12
	# 	print(get_year,"year",get_month,"get_month")
	# return ("{} year {} months".format(get_year,get_month))

	if list(filter(None,monthss)) and list(filter(None,yearss)):
		return ("{} year {} months".format(yearss[0],monthss[0]))
	else:
		sum_of_month = sum(monthss)
		get_year = sum_of_month//12

		get_month = sum_of_month%12
		print(get_year,"year",get_month,"get_month")
		return ("{} year {} months".format(get_year,get_month))


def extract_projects(txt):

	projects_list = []
	
	heading_list = [
		# 'Education',
		# 'Experience',
		# 'Publications',
		# 'Leadership',
		# 'Extra-Curricular',
		# 'Skills',
		# 'Certifications',
		'Projects',
		'PROJECTS',
		'Leadership',
		'Certifications',
		'Strengths',
		'SKILLS',
		'PERSONAL PROJECTS',
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
	


	try:
		i='Projects'
		print("key",i)
		print("value",para[i])
		
		count = 1
		projects_dict = {}

		projects_title = ""
		project_sent = ""
		# for sent in para:
		for sent in nltk.sent_tokenize(para[i]):
			projects_list.append(sent)
				
		print("projects_list",projects_list)
		return projects_list
	except:
		import pdb;pdb.set_trace()
		i='PROJECTS'
		print("key",i)
		print("value",para[i])
		
		count = 1
		projects_dict = {}

		projects_title = ""
		project_sent = ""
		# for sent in para:
		for sent in nltk.sent_tokenize(para[i]):
			projects_list.append(sent)
				
		print("projects_list",projects_list)
		return projects_list









# def extract_fields(txt):
# 	# import pdb;pdb.set_trace()
# 	resume_fields = resumeparse.read_file('/home/ebabu/Downloads/SrishtiJain2021-converted.docx')
# 	return resume_fields
	# pass



# def main():
# 	text = extract_text_from_docx('/home/dell/Downloads/Sanidhya_CV-converted.docx')
# 	experience = extract_experience(text)
# main()





















from django.shortcuts import render
from django.http import HttpResponse
from resume_parser import resumeparse
from Resume.utils import extract_text_from_docx,extract_experience,extract_projects
# extract_fields,

# Create your views here.



def resumeparse_fun(request):
	text = extract_text_from_docx('/home/ebabu/Downloads/SrishtiJain2021-converted.docx')
	# resume_field = extract_fields(text)
	experience = extract_experience(text)
	projects = extract_projects(text)
	resume_field_data = {}
	for i in resume_field:
		if i == 'name' or i== 'email' or i == 'skills':
			resume_field_data[i]=resume_field[i]
	# import pdb;pdb.set_trace()
	dict_data = {
		'experience':experience,
		'resume_field':resume_field,
		'projects':projects,
		'resume_field_data':resume_field_data,
	}
	return render(request,'Resume_Folder/resume_tem.html',{'data':dict_data})























import re
import nltk
import docx2txt
from pdfminer.high_level import extract_text
from nltk.tokenize import sent_tokenize, word_tokenize
# from resume_parser import resumeparse
# from pyresparser import ResumeParser
from datetime import datetime
from dateutil import relativedelta

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_text_from_docx(docx_path):
	txt = docx2txt.process(docx_path)
	if txt:
		return txt.replace('\t', ' ')
	return None


def extract_experience(txt):

	heading_list = [
		'Experience',
		'Publications',
	]


	year_key = {}
	s = ""
	prev_heading = "first Heading"
	for i in nltk.word_tokenize(txt):
		if i in heading_list:
			year_key[prev_heading] = s
			s = " "
			prev_heading = i
		else:
			s = s + " " + i


	i = 'Experience'
	date_data = re.findall(r'[A-Z]\w+\s\d+', year_key[i])
	rvs_date=date_data[::-1]
	n=2
	n1=0
	n2=2
	month_list=[]
	year_list=[]
	start_date = " "
	end_date = " "
	time_difference = " "
	for i in range(0,len(rvs_date),n):
		val = rvs_date[n1:n2]
		try:
			start_date = datetime.strptime(val[0], "%B %Y")
			end_date = datetime.strptime(val[1], "%B %Y")
			time_difference = relativedelta.relativedelta(start_date,end_date)
		except:
			start_date = datetime.strptime(val[0], "%B %Y")
			end_date = datetime.now()
			time_difference = relativedelta.relativedelta(end_date,start_date)
		if time_difference.months:
			month_list.append(time_difference.months)
		if time_difference.years:
			year_list.append(time_difference.year_list)
		n1+=2
		n2+=2
	if month_list:
		sum_of_month = sum(month_list)
		get_year = sum_of_month//12
		get_month = sum_of_month%1
	return ("{} year {} months".format(get_year,get_month))



# def extract_fields(txt):
# 	import pdb;pdb.set_trace()
# 	resume_fields = ResumeParser('/home/ebabu/Downloads/Sanidhya_CV-converted.docx').get_extracted_data()
# 	return resume_fields




# def main():
# 	text = extract_text_from_docx('/home/ebabu/Downloads/Sanidhya_CV-converted.docx')
# 	experience = extract_experience(text)
# 	print(experience)

# main()




import re
import nltk
import docx2txt
from pdfminer.high_level import extract_text
from nltk.tokenize import sent_tokenize, word_tokenize
from resume_parser import resumeparse
from datetime import datetime
from dateparser.search import search_dates
from dateutil import relativedelta

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_text_from_docx(docx_path):
	txt = docx2txt.process(docx_path)
	if txt:
		return txt.replace('\t', ' ')
	return None


def extract_experience(txt):

	heading_list = [
		'Experience',
		'Employment',
		'Technical Skills',
		# 'Professional',
		'Publications',
		'Educational',
	]

	year_key = {}
	s = ""
	prev_heading = "first Heading"
	for i in nltk.word_tokenize(txt):
		if i in heading_list:
			year_key[prev_heading] = s
			s = " "
			prev_heading = i
		else:
			s = s + " " + i

	# import pdb;pdb.set_trace()
	experience_months = []
	for key in year_key:
		if key in heading_list:
			i=key
	print("iiiii",i)
	# 	experience_months.append(re.findall(r'[A-Z]\w+\s\d+',year_key[i]))

	date_data = search_dates(year_key[i])
	import pdb;pdb.set_trace()
	for edate in date_data:
		experience_months.append(re.findall(r'[A-Z]\w+\s\d+',str(edate[0])))
	rvs_date=experience_months[::-1]
	rvs_date=list(filter(None,rvs_date))
	n=2
	n1=0
	n2=2
	monthss=[]
	yearss=[]
	start_date = " "
	end_date = " "
	time_difference = " "
	for i in range(0,len(rvs_date),n):
		val = rvs_date[n1:n2]
		# import pdb;pdb.set_trace()
		try:
			start_date = datetime.strptime(val[0][0], "%B %Y")
			end_date = datetime.strptime(val[1][0], "%B %Y")
			time_difference = relativedelta.relativedelta(start_date,end_date)
		except:
			start_date = datetime.strptime(val[0][0], "%B %Y")
			end_date = datetime.now()
			time_difference = relativedelta.relativedelta(end_date,start_date)
		if time_difference.months:
			monthss.append(time_difference.months)
		if time_difference.years:
			yearss.append(time_difference.years)
		n1+=2
		n2+=2
	print("months",monthss,"years",yearss)
	if monthss:
		# import pdb;pdb.set_trace()
		sum_of_month = sum(monthss)
		get_year = sum_of_month//12
		get_month = sum_of_month%12
		print(get_year,"year",get_month,"get_month") 
	return ("{} year {} months".format(get_year,get_month))


def extract_projects(txt):

	projects_list = []
	
	heading_list = [
		# 'Education',
		# 'Experience',
		# 'Publications',
		# 'Leadership',
		# 'Extra-Curricular',
		# 'Skills',
		# 'Certifications',
		'Projects',
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

	i='Projects'
	print("key",i)
	print("value",para[i])
	
	count = 1
	projects_dict = {}

	projects_title = ""
	project_sent = ""
	# for sent in para:
	for sent in nltk.sent_tokenize(para[i]):
		projects_list.append(sent)
			# import pdb;pdb.set_trace()
			# for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			# 	# chunk = list(chunk)
			# 	if hasattr(chunk, 'label') and (chunk.label() == 'ORGANIZATION' or 'PERSON'):
			# 	# 		projects_list.append(sent)
			# 	# 		chunk_leave = chunk.leaves()
			# 	# 		# import pdb;pdb.set_trace()
			# 	# 		for word,tag in chunk_leave:
			# 	# 			# projects_title = []
			# 	# 			# projects_title.append(word)
			# 	# 			projects_title = word
			# 	# 		print("projects_title",projects_title)
			# 	# project_sent = sent
			# 	# projects_dict[projects_title] = project_sent

			# 		# while count<=3:
			# 			# print(chunk.label())
			# 			# pass
			# 			# count += 1
			# 	# print("sent",sent," ")
	# import pdb;pdb.set_trace()
	print("projects_list",projects_list)
	return projects_list








def extract_fields(txt):
	# import pdb;pdb.set_trace()
	resume_fields = resumeparse.read_file('/home/ebabu/Downloads/Sanidhya_CV-converted.docx')
	return resume_fields



# def main():
# 	text = extract_text_from_docx('/home/dell/Downloads/Sanidhya_CV-converted.docx')
# 	experience = extract_experience(text)
# main()




# import pdb;pdb.set_trace()
			# for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			# 	# chunk = list(chunk)
			# 	if hasattr(chunk, 'label') and (chunk.label() == 'ORGANIZATION' or 'PERSON'):
			# 	# 		projects_list.append(sent)
			# 	# 		chunk_leave = chunk.leaves()
			# 	# 		# import pdb;pdb.set_trace()
			# 	# 		for word,tag in chunk_leave:
			# 	# 			# projects_title = []
			# 	# 			# projects_title.append(word)
			# 	# 			projects_title = word
			# 	# 		print("projects_title",projects_title)
			# 	# project_sent = sent
			# 	# projects_dict[projects_title] = project_sent

			# 		# while count<=3:
			# 			# print(chunk.label())
			# 			# pass
			# 			# count += 1
			# 	# print("sent",sent," ")
	# import pdb;pdb.set_trace()