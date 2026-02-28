import json
import google.generativeai as genai  # Use the working library
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserPreference, UserActivity

# Replace with your actual API Key
genai.configure(api_key="AIzaSyB-xxxxxxxxxxxxxxxxxxxxxxxx")

# 1. Register User
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            UserPreference.objects.create(
                full_name=data.get('full_name'),
                email=data.get('email'),
                password=data.get('password')
            )
            return JsonResponse({'message': 'Success'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'signup.html')

# 2. Login User
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Login aana udane assessment-ku redirect pannuroam
        return redirect(f'/assessment/?email={email}')
    return render(request, 'login.html')

# 3. Assessment View
def assessment_view(request):
    email = request.GET.get('email', '')
    if request.method == 'POST':
        user_email = request.POST.get('email')
        final_score = 75 
        # Test mudinja udane dashboard-ku redirect
        return redirect(f'/dashboard/?email={user_email}&score={final_score}')
    return render(request, 'assessment.html', {'email': email})

# 4. Profile View 
def profile_view(request):
    email = request.GET.get('email', '')
    user_info = UserPreference.objects.filter(email=email).first()
    return render(request, 'proinfo.html', {'user': user_info})

# 5. Update Profile
@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            UserPreference.objects.filter(email=data.get('email')).update(
                skill_level=data.get('skill'),
                learning_goal=data.get('goal'),
                prog_language=data.get('language'),
                study_time=data.get('study_time'),
                duration=data.get('duration')
            )
            return JsonResponse({'message': 'Profile Updated Successfully! ✅'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'proinfo.html')

# 6. Dashboard View
def dashboard_view(request):
    email = request.GET.get('email', '')
    current_score = int(request.GET.get('score', 15)) 
    user_info = UserPreference.objects.filter(email=email).first()

    username = user_info.full_name if user_info else "GUEST USER"
    lang = user_info.prog_language if user_info else "Python"
    goal = user_info.learning_goal if user_info else "Career Path"

    roadmap_list = []
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Create a 5-step roadmap for {lang} for goal {goal}. Return ONLY a JSON list."
        response = model.generate_content(prompt)
        raw_text = response.text.replace('```json', '').replace('```', '').strip()
        roadmap_list = json.loads(raw_text)
    except:
        roadmap_list = [{"title": "Step 1", "desc": f"Master {lang} basics"}]

    context = {
        'username': username,
        'email': email,
        'language': lang,
        'roadmap_list': roadmap_list,
        'score': current_score,
        'accuracy': current_score,
        'level': "Beginner" if current_score < 50 else "Advanced",
    }
    return render(request, 'dashboard.html', context)

# 7. Add Activity
@csrf_exempt
def add_activity(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = UserPreference.objects.get(email=data.get('email'))
            UserActivity.objects.create(
                user=user,
                activity_type=data.get('type'),
                description=data.get('description')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)
    def register_user(request):
    if request.method == 'POST':
        # ... your logic ...
        return redirect('profile') # This MUST be indented inside the function
    return render(request, 'signup.html')