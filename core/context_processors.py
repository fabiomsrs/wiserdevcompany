from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'RUN_DATE': settings.RUN_DATE,        
    }