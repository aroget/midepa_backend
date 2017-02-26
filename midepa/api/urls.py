from django.conf.urls import url
from .views import (ProfileListAPIView,
                    InquilinosListAPIView,
                    RegistrationCreateAPIView,
                    ServicioListCreateAPIView,
                    PresupuestoListCreateAPIView,
                    ServicioRatingRetrieveUpdateAPIView,
                    ServicioLRetrieveUpdateDestroyAPIView,
                    PresupuestoRetrieveUpdateDestroyAPIView,)

urlpatterns = [
    # Signup
    url(r'^register$', RegistrationCreateAPIView.as_view()),

    # GET, POST presupuesto (list)
    url(r'^presupuestos$', PresupuestoListCreateAPIView.as_view()),

    # PUT, GET, DELETE, (single)
    url(r'^presupuesto/(?P<pk>[0-9]+)/$',
        PresupuestoRetrieveUpdateDestroyAPIView.as_view()),


    # GET, POST presupuesto (list)
    url(r'^servicios$', ServicioListCreateAPIView.as_view()),

    # PUT, GET, DELETE, (single)
    url(r'^servicio/(?P<pk>[0-9]+)/$', ServicioLRetrieveUpdateDestroyAPIView.as_view()),

    # PATCH (rate)
    url(r'^servicio/(?P<pk>[0-9]+)/rate$', ServicioRatingRetrieveUpdateAPIView.as_view()),


    # GET (list)
    url(r'^inquilinos$', InquilinosListAPIView.as_view()),

    # GET (single)
    url(r'^me$', ProfileListAPIView.as_view()),

]
