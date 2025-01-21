from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact_view(request):
    error_messages = []
    success_message = None

    if request.method == "POST":
        # Extract data from the form
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('msg', '').strip()

        # Validate data
        if not name:
            error_messages.append("Name is required.")
        if not email:
            error_messages.append("Email is required.")
        elif '@' not in email:  # Basic email validation
            error_messages.append("Invalid email format.")
        if not phone:
            error_messages.append("Phone number is required.")
        elif not phone.isdigit() or len(phone) != 10:
            error_messages.append("Phone number must be exactly 10 digits.")
        if not message:
            error_messages.append("Message is required.")

        # Save to the database if no errors
        if not error_messages:
            try:
                # Save validated data to the database
                
                success_message = "Your message has been submitted successfully!"
            except Exception as e:
                error_messages.append(f"An error occurred: {str(e)}")

    return render(request, 'contact.html', {
        'error_messages': error_messages,
        'success_message': success_message
    })


def projects (request):
    projects_show=[
        {
            'title': 'Rasoi Connect',
            'path': 'images/rasoi_connect.PNG',
        },
        {
            'title': 'Ecommerce',
            'path': 'images/ecommerce.PNG',
        },

        {
            'title': 'Timetable Scheduler',
            'path': 'images/timtable.PNG',
        },
        {
            'title': 'CRUD',
            'path': 'images/CRUD.PNG',
        },

         {
            'title': 'Photo Uploader',
            'path': 'images/photo_uploader.PNG',
        },
          {
            'title': 'To do list',
            'path': 'images/todolist.PNG',
        },
         {
            'title': 'Portfolio',
            'path': 'images/portfolio.PNG',
        },
                  {
            'title': 'Labour Hiring',
            'path': 'images\labour_hiring.PNG',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})
def resume(request):
    resume_path='myresume/sanjay_resume.pdf'
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,'rb') as resume_file:
            response=HttpResponse(resume_file.read(),content_type='application/pdf')
            response['Content-Disposition']='attachment';filename='sanjay_resume.pdf'
            return response
    else:
        return HttpResponse('file not found ',status=404)