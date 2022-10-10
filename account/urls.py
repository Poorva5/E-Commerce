from django.urls import path
from account.views import  registration_view, home, login_view, logout_view, profile_view, about_page
#             home,
#             login_view,
#             logout_view,
#             account_view,
#             # registration_view,
# )




urlpatterns = [ 
    path('register/' , registration_view, name="signup"),
    path('logout/', logout_view, name = "logout"),
    path('login/', login_view, name="login"),
    path('home/', home, name="home"),
    path('profile/<phone>/', profile_view, name="profile_page"),
    path('about_us/', about_page, name='about_page'),
#     path('profile/', account_view, name="account"),
    
]

