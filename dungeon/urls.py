from django.urls import path,include
from .views import LandingView,ZayavkaDetali,ZayavkaSpisok,\
    ZayavkaCreate,ZayavkaDelete,ZayavkaSpisokR,\
    ZayavkaSpisokC,ZayavkaDetaliC,ZayavkaUpdate,zayavka_create_c_def,\
    ZayavkaUpdateR #Asda ZayavkaCreateC

app_name='dungeon'

urlpatterns=[

    path('<int:pk>/',ZayavkaDetali.as_view(),name='zayavka-detali'),
    path('<int:pk>/obnovit',ZayavkaUpdate.as_view(),name='zayavka-update'),
    path('spisok',ZayavkaSpisok.as_view(),name='zayavka-spisok'),
    path('create',ZayavkaCreate.as_view(),name='zayavka-create'),
    path('<int:pk>/udalit',ZayavkaDelete.as_view(),name='zayavka-delete'),

    path('spisok_r',ZayavkaSpisokR.as_view(),name='zayavka-spisok-r'),
    path('<int:pk>/smenit_status',ZayavkaUpdateR.as_view(),name='zayavka-update-r'),

    path('spisok_c',ZayavkaSpisokC.as_view(),name='zayavka-spisok-c'),
    path('spisok_c/create',zayavka_create_c_def,name='zayavka-create-c'),
    path('<int:pk>/spisok_c/detali',ZayavkaDetaliC.as_view(),name='zayavka-detali-c'),


    #path('spisok_c/create',SS,name='zayavka-create-c'),

]