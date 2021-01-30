
from django.contrib.sites.shortcuts import get_current_site

def sassy_context(request):
    return {'saasy': 
                {'profile': request.user.saasy_profile.get(site=get_current_site(request)) }
            }
