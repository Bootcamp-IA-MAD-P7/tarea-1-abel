from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),  # type: ignore[arg-type]
    path('<int:libro_id>/', views.detalle_libro, name='detalle_libro'),  # type: ignore[arg-type]
    path('crear/', views.crear_libro, name='crear_libro'),  # type: ignore[arg-type]
    path('<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),  # type: ignore[arg-type]
    path('<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),  # type: ignore[arg-type]
]