from core.models import Setting
def setting_logo(request):
    setting_data=Setting.objects.first()
    return {
        'setting_data':setting_data
    }