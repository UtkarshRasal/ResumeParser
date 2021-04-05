from resume_parser import resumeparse

# nltk.download('popular')
data = resumeparse.read_file('/home/ebabu/Downloads/SrishtiJain 2021-converted.docx')
print(data)


# from pyresparser import ResumeParser
# data = ResumeParser('/path/to/resume/file').get_extracted_data()

# resume_fields = ResumeParser('/home/ebabu/Downloads/Sanidhya_CV-converted.docx').get_extracted_data()
# print(resume_fields)