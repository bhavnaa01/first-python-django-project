from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
   path('addstudent',views.addstudent),
   path('showstudents',views.showstudents),
   path('updatestudent',views.updatestudent),
   path('searchstudents',views.searchstudents),
   path('joinstudents',views.joinstudents),
   path('showjoinedstudent',views.showjoinedstudent),
   path('updatejoinedstudent',views.updatejoinedstudent),
   path('searchjoinedstudents',views.searchjoinedstudents),
   path('addbatch',views.addbatch),
   path('showbatches',views.showbatches),
   path('updatebatch',views.updatebatch),
   path('deletebatches',views.deletebatches),
   path('searchbatch',views.searchbatch),
   path('addtrainer',views.addtrainer),
   path('showtrainers',views.showtrainers),
   path('updatetrainer',views.updatetrainer),
   path('deletetrainer',views.deletetrainer)
]
