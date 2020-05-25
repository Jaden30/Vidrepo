from django.urls import path
 
from . import views 
# set to a list 
app_name = "movies"
urlpatterns = [
    path('', views.index, name = 'index'),# the empty string used to represnt the root of this app
    path('<int:movie_id>', views.detail, name = 'detail')

]