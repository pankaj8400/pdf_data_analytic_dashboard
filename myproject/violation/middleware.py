# middleware.py

import time
from django.conf import settings
from django.contrib.sessions.models import Session
from django.utils.deprecation import MiddlewareMixin

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        session_age = request.session.get('last_activity')

        # Check if last activity exists and if it's older than the allowed session duration
        if session_age and time.time() - session_age > settings.SESSION_COOKIE_AGE:
            # Expire the session if the user was inactive
            request.session.flush()  # Clear session data
        
        # Update last activity timestamp for every new request
        request.session['last_activity'] = time.time()

#