from pyresparser import ResumeParser
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Resume.utils import extract_experience_period,extract_experience, extract_projects, extract_text_data, extract_fields
from rest_framework.views import APIView
from .models import ResumeData
from .serializers import ResumeSerializer
from .path import file_path
from .forms import uploadForm
from django.contrib.sites.shortcuts import get_current_site
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os, requests, imgkit, uuid, img2pdf
from django.views import View
from subprocess import run
import subprocess

class UploadResume(APIView):
	def get(self, request):
		return render(request, 'Resume_Folder/uploadResume.html')

class ResumeView(APIView):
	serializer_class = ResumeSerializer

	def post(self, request):
		path = file_path(request)
		text = extract_text_data(path)
		resume_field = extract_fields(text, path)
		experience_period = extract_experience_period(text)
		exp = extract_experience(text)
		proj = extract_projects(text)
		experience = " "
		projects = " "

		resume_field_data = {}
		for i in resume_field:
			if i == 'name' or i == 'email' or i=='skills':
				resume_field_data[i] = resume_field[i]

		name = resume_field_data['name']		
	
		data = {'file_path': path,'name':name, 'experience':experience.join(exp) if exp else experience, 'projects':projects.join(proj) if proj else projects}
		serializer = self.serializer_class(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		_data = serializer.data
		_experience = _data['experience']
		_projects = _data['projects']
		_uid = _data['uid']
		print(_data['uid'])

		current_site = get_current_site(request).domain
		relativeLink = '/resume/download/'
		absurl = 'http://' + current_site + relativeLink + _uid 
		print(absurl)
		
		dict_data = {
			'experience_period':experience_period,
			'experience':_experience,
			'projects':_projects,
			'resume_field_data':resume_field_data,
			'absurl': absurl,
			'uid':_data['uid']
		}
		return render(request, 'Resume_Folder/resume_template.html', {'data':dict_data})
		# return Response({'data':dict_data})

class ResumeSaveView(APIView):
	serializer_class = ResumeSerializer
	model_class = ResumeData

	def post(self, request, pk):
		if request.is_ajax:
			instance = self.model_class.objects.get(uid=pk)
			_data = request.data
			data = {'experience': _data['experience'].replace('&nbsp;', '\n'), 'projects': _data['projects'].replace('&nbsp;', '\n') }
			serializer = self.serializer_class(data=data, instance=instance)
			serializer.is_valid(raise_exception=True)
			serializer.save()

			return Response(serializer.data)
		return Response("ERROR with ajax")



class ResumeUserView(APIView):			
	serializer_class = ResumeSerializer
	model_class = ResumeData

	def get(self, request, pk):
		instance = self.model_class.objects.get(uid=pk)
		serializer = self.serializer_class(instance=instance)
		_data = serializer.data 

		_experience = _data['experience'].replace('\n', '<br>')
		_projects = _data['projects'].replace('\n', '<br>')

		_experience = _experience.replace('<b>', "<b class='bold'>")
		_projects = _projects.replace('<b>', "<b class='bold'>")

		path = _data['file_path']
		text = extract_text_data(path)
		resume_field = extract_fields(text, path)
		experience_period = extract_experience_period(text)

		resume_field_data = {}
		for i in resume_field:
			if i == 'name' or i == 'email' or i=='skills':
				resume_field_data[i] = resume_field[i]

		dict_data = {
			'experience_period':experience_period,
			'experience':_experience,
			'projects':_projects,
			'resume_field_data':resume_field_data,
		}
		return render(request, 'Resume_Folder/resumeUserTemp.html', {'data':dict_data})

        
class DownloadView(APIView):
	model_class = ResumeData
	serializer_class = ResumeSerializer

	def get(self, request, pk):
		options = {
			'format': 'jpeg',
		}
		instance = self.model_class.objects.get(uid=pk)
		serializer = self.serializer_class(instance=instance)
		_data = serializer.data 

		name = _data['name']

		absurl = 'http://localhost:8000/resume-user/' + pk + '/'
		image_path = 'downloaded_Resume/Image_Files/' + name + '.jpeg'
		pdf_path = 'downloaded_Resume/PDf_files/' + name + '.pdf'
		
		#convert from url to image
		imgkit.from_url(absurl, image_path, options=options) 
		
		#convert from image to pdf
		subprocess.run(["img2pdf", image_path, "-o", pdf_path])

	
		return HttpResponse('File Downloaded Successfully')
