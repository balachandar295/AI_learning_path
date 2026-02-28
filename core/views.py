def dashboard_view(request):
    # 1. URL parameters fetch pannuroam
    email = request.GET.get('email', '')
    # Default score 15, illana URL-la irundhu edukkum
    current_score = int(request.GET.get('score', 15)) 

    # 2. Database-la user info check pannuroam
    user_info = UserPreference.objects.filter(email=email).first()

    # Default values
    username = "GUEST USER"
    lang = "Python"
    goal = "Career Path"
    duration = "15 Days"

    if user_info:
        username = user_info.full_name
        lang = user_info.prog_language
        goal = user_info.learning_goal
        # Model-la 'duration' field irundha edukkum, illana default
        duration = getattr(user_info, 'duration', '15 Days')

    # 3. AI Roadmap Generation
    roadmap_list = []
    try:
        # Prompt-la score and language automatic-ah send aagum
        model = genai.GenerativeModel('gemini-pro')
        prompt = (f"Create a 5-step roadmap for learning {lang} "
                  f"with the goal {goal}. My current knowledge score is {current_score}/100. "
                  f"Return ONLY a JSON list of objects with 'title' and 'desc' keys.")
        
        response = model.generate_content(prompt)
        raw_text = response.text.replace('```json', '').replace('```', '').strip()
        roadmap_list = json.loads(raw_text)
    except Exception as e:
        # AI error vandha default roadmap
        roadmap_list = [
            {"title": f"Master {lang} Basics", "desc": "Start with syntax and variables."},
            {"title": "Logic & Projects", "desc": "Build small apps to test skills."}
        ]

    # 4. Score-ai vachu Level calculation (Automatic)
    # 0-30: Beginner, 31-70: Intermediate, 71+: Advanced
    if current_score < 30:
        level_label = "Beginner"
    elif current_score < 70:
        level_label = "Intermediate"
    else:
        level_label = "Advanced"

    context = {
        'username': username,
        'email': email,
        'language': lang,
        'goal': goal,
        'duration': duration,
        'roadmap_list': roadmap_list,
        'score': current_score,
        'accuracy': current_score,
        'streak': 1,
        'level': level_label,
    }
    return render(request, 'dashboard.html', context)
import json
import google.generativeai as genai
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserPreference, UserActivity

genai.configure(api_key="YOUR_ACTUAL_API_KEY")

# --- INDHA FUNCTION MISSING ---
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

# --- INDHA FUNCTION-UM IRUKKANUM ---
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        return redirect(f'/assessment/?email={email}')
    return render(request, 'login.html')

# Dashboard View (Update pannadhu)
def dashboard_view(request):
    email = request.GET.get('email', '')
    current_score = int(request.GET.get('score', 15)) 
    user_info = UserPreference.objects.filter(email=email).first()

    # Roadmap generation logic inga irukanum...
    # (Mela naan kudutha full dashboard_view code-ai inga podunga)
    
    context = {
        'username': user_info.full_name if user_info else "GUEST USER",
        'language': user_info.prog_language if user_info else "Python",
        'roadmap_list': [], # AI logic inga varum
        'score': current_score,
    }
    return render(request, 'dashboard.html', context)
import json
import google.generativeai as genai
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
        return redirect(f'/assessment/?email={email}')
    return render(request, 'login.html')

# 3. Assessment View
def assessment_view(request):
    email = request.GET.get('email', '')
    if request.method == 'POST':
        user_email = request.POST.get('email')
        final_score = 75 # Logic for score calculation can be added here
        return redirect(f'/dashboard/?email={user_email}&score={final_score}')
    return render(request, 'assessment.html', {'email': email})

# 4. Profile View (Indha function missing-nu dhaan error vandhuchi)
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
            return JsonResponse({'message': 'Updated Success! ✅'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'proinfo.html')

# 6. Dashboard View (Final Corrected Version)
def dashboard_view(request):
    email = request.GET.get('email', '')
    current_score = int(request.GET.get('score', 15)) 
    user_info = UserPreference.objects.filter(email=email).first()

    username = user_info.full_name if user_info else "GUEST USER"
    lang = user_info.prog_language if user_info else "Python"
    goal = user_info.learning_goal if user_info else "Career Path"

    # AI Roadmap Logic
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
# 7. Update Profile Logic
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
# Check that this function exists and is spelled exactly like this:
@csrf_exempt
def add_activity(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # We use the Model 'UserActivity' inside the function 'add_activity'
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
# Change this:
# import google.generativeai as genai 

# To this:
import google.genai as genai
return redirect('profile')
return redirect('assessment')
return redirect('dashboard')