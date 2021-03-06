from django.contrib import admin

# Register your models here.
from .models import About
from .models import Slider
from .models import Donor
from .models import Donation

admin.site.register(About)
admin.site.register(Slider)
admin.site.register(Donor)


class AdminDonation(admin.ModelAdmin):
    model = Donation
    list_display = ('title', 'start_date', 'end_date','raised_amount', 'goal_amount')


admin.site.register(Donation, AdminDonation)