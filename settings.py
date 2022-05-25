# <proj>/settings.py

INSTALLED_APPS = [
    # other installed apps
    'pwa',
]

# <proj>/settings.py

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    # or any other location of your choice
]

# <proj>/urls.py

from django.urls import path, include

urlpatterns = [
    # other path settings
    path('', include('pwa.urls')),
]