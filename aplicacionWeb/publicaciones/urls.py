from django.urls import path
from publicaciones import views

app_name = 'publicaciones'

urlpatterns = [
    path('publicaciones/', views.VerPublicaciones.as_view(), name='publicaciones'),
    path('postear/', views.Postear.as_view(), name='postear'),
    path('editar-post/<int:pk>', views.EditarPost.as_view(), name='editar-posteo'),
    path('eliminar-post/<int:pk>', views.EliminarPost.as_view(), name='eliminar-posteo'),
    path('detalle-post/<int:pk>', views.PostDetalle.as_view(), name='detalle-posteo')
]