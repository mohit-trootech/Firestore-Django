from django.contrib import admin
from django.urls import path
from firestore.views import firestore_home, firestore_create, firestore_read, newsletter
from firestore.utils.constants import Urls

urlpatterns = [
    path("admin/", admin.site.urls, name=Urls.ADMIN.value),
    path("", firestore_home, name=Urls.INDEX.value),
    path("create/", firestore_create, name=Urls.CREATE.value),
    path("list/", firestore_read, name=Urls.LIST.value),
    path("newsletter/", newsletter, name=Urls.NEWLETTER_REVERSE.value),
]
