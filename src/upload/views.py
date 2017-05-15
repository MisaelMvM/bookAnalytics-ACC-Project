from django.shortcuts import render
from django.conf import settings
from forms import DocumentForm
from django.contrib.auth.decorators import login_required
import re
import string

# Create your views here.
@login_required()
def upload(request):
    title = 'Upload Your Book'
    confirm_message = None
    myList = []
    form = DocumentForm(request.POST, request.FILES or None)
    context = {'title':title, 'form':form, 'confirm_message':confirm_message}       
    if request.method == 'POST': 
        if form.is_valid():
            description = form.cleaned_data['description']
            form.save()
            frequency = { }
            url = path = 'C:/sandbox/12_Python/bookProjectEnv/static/media/documents/' + str(request.FILES['document'])
            document_text = open(url, 'r')
            text_string = document_text.read().lower()
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)            
            for word in match_pattern:
                count = frequency.get(word,0)
                frequency[word] = count + 1                
            frequency_list = frequency.keys()            
            for words in frequency_list:
            	myList.append({'word':words, 'frequency':frequency[words]})
            confirm_message = 'Upload successfull!'
            form = None
            context = {'title':title, 'form':form, 'list':myList, 'description':description, 'confirm_message':confirm_message}
            
            

    else:
        form = DocumentForm()

    template = 'upload.html'

    return render(request, template, context)


