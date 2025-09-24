from django.shortcuts import render,redirect
# from .models import ContactMessage
def home(request):
    return render(request, "myapp/home.html")
# def contact_view(request):
#     success = False
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
        
#         ContactMessage.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )
#         success = True

#     return render(request, 'contact.html', {'success': success})