from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def home(request):
    """Render the homepage with a contact form."""
    return render(request, 'home/index.html')

@require_http_methods(["POST"])
def submit_form(request):
    """Handle form submission."""
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')
    
    if not all([name, email, message]):
        return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)
    
    return JsonResponse({
        'status': 'success',
        'message': f'Hello {name}! Your message has been received.',
        'data': {'name': name, 'email': email}
    })
