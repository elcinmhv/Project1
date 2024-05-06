from core.models import Setting
from core.forms import SubscriberForm
def setting_logo(request):
    setting_data=Setting.objects.first()
    subscriber_form = SubscriberForm()  # Create a form instance
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            # Clear the form after successful submission
            subscriber_form = SubscriberForm()
    return {
        'setting_data':setting_data,
        'subscriber_form': subscriber_form
    }