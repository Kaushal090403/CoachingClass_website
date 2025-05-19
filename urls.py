
from django.contrib import admin
from django.urls import path
from auapp.views import login_view, signup, logout_view, changepw, rnp, home
from cmsapp.views import showcourses, addcourses,deletecourse,showstudent,addstudent,deletestudent,updatecourse,updatestudent
from loapp.views import locate

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_view, name="login_view"),
    path("signup/", signup, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("changepw/",changepw,name="changepw"),
    path("rnp/",rnp,name="rnp"),
    path("home/", home, name="home"),
    path("showcourses/", showcourses, name="showcourses"),
    path("addcourses/", addcourses, name="addcourses"),
    path("deletecourse/<int:id>", deletecourse, name="deletecourse"),
    path("showstudent/",showstudent,name="showstudent"),
    path("addstudent/",addstudent,name="addstudent"),
    path("deletestudent/<int:id>",deletestudent,name="deletestudent"),
    path("locate/",locate,name="locate"),
    path("updatecourse/<int:id>",updatecourse,name="updatecourse"),
    path("updatestudent/<int:id>",updatestudent,name="updatestudent"),
]
