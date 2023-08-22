from django.utils import timezone
import pytz

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        utc_now = timezone.now()
        ist = pytz.timezone('Asia/Kolkata')
        ist_now = utc_now.astimezone(ist)
        ist_now = ist_now.replace(tzinfo=None)
        ist_now = ist_now.replace(microsecond=0)
        request.ist_now = ist_now
        
        response = self.get_response(request)
        return response
