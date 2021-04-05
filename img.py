import imgkit


css = 'templates/Resume_Folder/index.css'
with open("Resume-user.html", "r") as fp:
    data = fp.read()


# imgkit.from_url("http://localhost:8000/resume-user/5f269af7-946f-4875-99fb-1f3bdd58191b/", "test.jpeg")

imgkit.from_string(data, "test.jpeg")
