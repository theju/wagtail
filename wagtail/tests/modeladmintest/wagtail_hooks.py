from __future__ import absolute_import, unicode_literals

from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail.contrib.modeladmin.views import CreateView
from wagtail.tests.testapp.models import BusinessChild, EventPage, SingleEventPage

from .models import Author, Book, Token, Publisher
from .forms import PublisherModelAdminForm


class AuthorModelAdmin(ModelAdmin):
    model = Author
    menu_order = 200
    list_display = ('name', 'date_of_birth')
    list_filter = ('date_of_birth', )
    search_fields = ('name', )
    inspect_view_enabled = True
    inspect_view_fields = ('name', )


class BookModelAdmin(ModelAdmin):
    model = Book
    menu_order = 300
    list_display = ('title', 'author')
    list_filter = ('author', )
    search_fields = ('title', )
    inspect_view_enabled = True
    inspect_view_fields_exclude = ('title', )


class TokenModelAdmin(ModelAdmin):
    model = Token
    list_display = ('key',)


class PublisherCreateView(CreateView):
    def get_form_class(self):
        return PublisherModelAdminForm


class PublisherModelAdmin(ModelAdmin):
    model = Publisher
    create_view_class = PublisherCreateView


class EventPageAdmin(ModelAdmin):
    model = EventPage
    list_display = ('title', 'date_from', 'audience')
    list_filter = ('audience', )
    search_fields = ('title', )
    inspect_view_enabled = True
    inspect_view_fields_exclude = ('feed_image', )


class SingleEventPageAdmin(EventPageAdmin):
    model = SingleEventPage


class EventsAdminGroup(ModelAdminGroup):
    menu_label = "Events"
    items = (EventPageAdmin, SingleEventPageAdmin)
    menu_order = 500


class BusinessChildAdmin(ModelAdmin):
    model = BusinessChild
    # having "Business Child" permanently in the menu confuses tests for the 'add page' view
    menu_label = "BusinessSprog"


modeladmin_register(AuthorModelAdmin)
modeladmin_register(BookModelAdmin)
modeladmin_register(TokenModelAdmin)
modeladmin_register(PublisherModelAdmin)
modeladmin_register(EventsAdminGroup)
modeladmin_register(BusinessChildAdmin)
