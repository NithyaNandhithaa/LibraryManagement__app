from django.urls import path

from LibraryApp import views

urlpatterns = [
    path('',views.login_fun,name='log'),#it will redirect to login page
    path('areg',views.admin_reg,name='areg'),#it will redirect to admin registeration page
    path("readadmin",views.admin_read_fun),# it will check whether given value is already exist or not ,
                                            # if not it will create superuser and it in user predefined table
    path('sreg',views.stu_reg,name='sreg'),#it will redirect to student regiesteration page
    path("readstud",views.stu_read_fun),#it will read student data and save it in  student table
    path("logdata",views.log_data_fun),
    path('add',views.add_book,name='add'),# it will redirect to addbook.html
    path("bookdata",views.read_book_data),#it will add book to book table
    path('display',views.display_fun,name='dis'),#it will display the book table
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),

    path('assign',views.assign_fun,name='assign'),
    path("read_assign_data",views.read_assignbook),
    path("assign_data",views.read_assign_data),
    path('issue',views.issue_fun,name='issue'),

    path('upgrade/<int:id>',views.upgrade_fun,name='upgrade'),#to update issued table
    path('v/<int:id>',views.delete_issuetable_fun,name='v'),#it will delete the row from issued table
    path('sissue',views.sissue_display_fun,name='sissue'),#it will fetch data of student and get it from issue_book table and display in studentissuebook.html
    path('ahome',views.admin_home_fun,name='ahome'),#it will redirect ot admin home page
    path('shome',views.student_home_fun,name='shome'),#it will redirect to student home page
    path('pro',views.profile_fun,name='pro'),#it will redirect to student profile setting page
    path("go_to_up" ,views.go_to_up,name="proup"),#it will update the student data
    path("updatepro",views.profile_updation,name="go_to_up")
]