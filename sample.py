import imgkit

options = {
    'format': 'png',
}

absurl = 'http://localhost:8000/resume-user/' + 'ee8540f4-16e4-4a88-93d0-ace0a121404d' + '/'

imgkit.from_url(absurl, 'test.png', options=options)