from django.contrib import admin


from .models import EventPage , RaiseHand , RequestInsitute , InstituteDetails , EditProfile
admin.site.register(EventPage)
admin.site.register(RequestInsitute)
admin.site.register(InstituteDetails)
admin.site.register(EditProfile)

