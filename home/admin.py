from django.contrib import admin
from home.models import Contact

from home.models import Venue
from home.models import Event
from home.models import MyClubUser
from home.models import Demo
from home.models import Student
from home.models import Admission
from home.models import marks
from home.models import Feedback

# Register your models here.
admin.site.register(Contact)

admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)
admin.site.register(Demo)
admin.site.register(Student)
admin.site.register(marks)
admin.site.register(Admission)
admin.site.register(Feedback)
