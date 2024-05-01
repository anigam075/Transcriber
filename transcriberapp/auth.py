from .models import User_s

def authenticate(email=None, password=None):
    try:
        user = User_s.objects.get(email=email)
        if user.password == password:
            return user
    except User_s.DoesNotExist:
        return None

def login(request, user):
    request.session['user_id'] = user.id

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']

def get_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            return User_s.objects.get(id=user_id)
        except User_s.DoesNotExist:
            pass
    return None