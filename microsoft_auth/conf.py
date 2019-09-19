from django.contrib.sites.shortcuts import get_current_site

from .models import SiteConfiguration


LOGIN_TYPE_MA = SiteConfiguration.LOGIN_TYPE_MA
LOGIN_TYPE_XBL = SiteConfiguration.LOGIN_TYPE_XBL
CACHE_TIMEOUT = 86400
CACHE_KEY_OPENID = "microsoft_auth_openid_config"
CACHE_KEY_JWKS = "microsoft_auth_jwks"


def get_conf(request):
    site = get_current_site(request)
    return SiteConfiguration.objects.get(site=site)
