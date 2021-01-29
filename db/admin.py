from django.contrib import admin

from .models import UserProfile
from .models import Collection
from .models import CollectionData
from .models import Tag
from .models import Number
from .models import Searchable
from .models import SearchTerm
from .models import SearchTermValue
#from .models import Number


admin.site.register(UserProfile)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
	#fields = ('title',)
	pass
	
admin.site.register(CollectionData)
admin.site.register(Tag)
admin.site.register(Number)
admin.site.register(Searchable)
admin.site.register(SearchTerm)
admin.site.register(SearchTermValue)


