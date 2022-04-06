from django.urls import path

from computer.views import(
    DeleteComputer,
    IndexView,
    ComputerDetailsView,
    FormView,
    UpdateViewForm,
    IndividualDetailView,
    LogoDetailView,
    DeleteView
)

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('details/',ComputerDetailsView.as_view(),name='details'),
    path('form/',FormView.as_view(),name='form'),
    path('update/<int:pk>',UpdateViewForm.as_view(),name='update'),
    path('individualdetail/<int:pk>',IndividualDetailView.as_view(),name='individualdetail'),
    path('logodetail/<str:brandname>',LogoDetailView.as_view(),name='logodetail'),
    path('delete/<int:pk>',DeleteComputer.as_view(),name='delete'),
    
]

