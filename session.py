from itsdangerous import URLSafeTimedSerializer
from fastapi import Request, Response



secret_key = "1234567890"

serializer = URLSafeTimedSerializer(secret_key)

def add_session(response: Response, session_data:dict, httponly=False):
    """Creer un session utilisateur cryptée"""
    try :
        encrypted_session = serializer.dumps(session_data)
        response.set_cookie(key='session', value=encrypted_session, httponly=httponly, secure=True)
    except : return False  
    return True  
            
    
def get_session(request):
    """Recuperer une session utilisateur"""
    try :
        encrypted_session = request.cookies.get('session')
        if encrypted_session is None : return None
        session_data = serializer.loads(encrypted_session)
    except : return None
    
    return session_data
 