import re
import nltk
import docx2txt
import os
from datetime import datetime
from dateutil import relativedelta
from dateparser.search import search_dates
# from pdfminer.high_level import extract_text
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
from pyresparser import ResumeParser


def extract_text_data(path):
	name, extension = os.path.splitext(path)
	if extension == '.pdf':
		txt = ''
		pdfFileObject = open(path, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
		number_of_pages = pdfReader.getNumPages()
		for page_number in range(number_of_pages):
			page = pdfReader.getPage(page_number)
			txt1= page.extractText()
			txt = txt + txt1
		return txt
	elif extension == '.docx':
		txt = docx2txt.process(path)
		if txt:
			print(txt)
			return txt.replace('\t', ' ')
		return None

def extract_experience_period(txt):
	try: 
		heading_list = [
			'Experience',
			'EXPERIENCE',
			'Employment',
			'Technical Skills',
			'Publications',
			'Educational',
			'EDUCATION',
			'Projects',
			'PROJECTS',
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

		import pdb;pdb.set_trace()
		experience_months = []
		for key in year_key:
			if key in heading_list:
				i=key
				break
		date_data = search_dates(year_key[i])
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
		for k in range(0,len(rvs_date),n):
			val = rvs_date[n1:n2]
			try:
				try:
					start_date = datetime.strptime(val[0][0], "%B %Y")
					end_date = datetime.strptime(val[1][0], "%B %Y")
					time_difference = relativedelta.relativedelta(start_date,end_date)
				except:
					start_date = datetime.strptime(val[0][0], "%b %Y")
					end_date = datetime.strptime(val[1][0], "%b %Y")
					time_difference = relativedelta.relativedelta(start_date,end_date)
			except:
				try:
					start_date = datetime.strptime(val[0][0], "%B %Y")
				except:
					start_date = datetime.strptime(val[0][0], "%b %Y")
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
		if list(filter(None,monthss)) and list(filter(None,yearss)):
			return ("{} Year {} Months".format(yearss[0],monthss[0]))
		else:
			sum_of_month = sum(monthss)
			get_year = sum_of_month//12
			get_month = sum_of_month%12
			# print(get_year,"year",get_month,"get_month")
			return ("{} Year {} Months".format(get_year,get_month))
	except:
		return None


def extract_experience(txt):

	try:
		experience_list = []
		heading_list = [
			'Projects',
			'PROJECTS',
			'PERSONAL',
			'Personal',
			'Experience',
			'EXPERIENCE',
			'Leadership',
			'LEADERSHIP',
			'Relevant',
			'Certifications',
			'CERTIFICATIONS',
			'Education',
			'EDUCATION',
			'Strengths',
			'STRENGTHS',
			'Certifications',
			'CERTIFICATIONS',
			'Publications',
			'PUBLICATIONS',
		]
		import pdb;pdb.set_trace()
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
		
		try:
			i = 'Experience'
			for sent in nltk.sent_tokenize(para.get(i)):
				experience_list.append(sent)
			return experience_list
		except:
			i='EXPERIENCE'
			for sent in nltk.sent_tokenize(para.get(i)):
				experience_list.append(sent)
			return experience_list
	except:
		return None
		
def extract_projects(txt):
	try:
		projects_list = []
		heading_list = [
			'Projects',
			'PROJECTS',
			'PERSONAL',
			'Personal',
			'Experience',
			'EXPERIENCE',
			'Leadership',
			'LEADERSHIP',
			'Relevant',
			'Certifications',
			'CERTIFICATIONS',
			'Education',
			'EDUCATION',
			'Strengths',
			'STRENGTHS',
			'Certifications',
			'CERTIFICATIONS',
			'Publications',
			'PUBLICATIONS',
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
		
		try:
			i = 'Projects'
			for sent in nltk.sent_tokenize(para.get(i)):
				projects_list.append(sent)
			return projects_list
		except:
			i='PROJECTS'
			for sent in nltk.sent_tokenize(para.get(i)):
				projects_list.append(sent)
			return projects_list
	except:
		return None

def extract_fields(txt, path):
	resume_fields = ResumeParser(path).get_extracted_data()
	return resume_fields



























