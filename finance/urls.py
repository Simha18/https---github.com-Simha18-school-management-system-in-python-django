from django.urls import path


from finance.views import feeCollections
from finance.views import feeDuesReport
from finance.views import feeCollectionReport



urlpatterns = [

    path('feecoll/', feeCollections),
    path('duereport/', feeDuesReport),
    path('collectionreport/', feeCollectionReport),

]
