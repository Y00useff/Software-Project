from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_user, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    # path("viewHotel/", views.viewHotel, name="viewHotel"),
    path("viewRoom/<int:hid>", views.viewRoom, name="viewRoom"),
    path("search/", views.search, name="search"),
    path("priceOrder/<int:hid>", views.priceOrder, name="priceOrder"),
    path("descpriceOrder/<int:hid>", views.descpriceOrder, name="descpriceOrder"),
    path("aclist/<int:hid>", views.aclist, name="aclist"),
    path("nonaclist/<int:hid>", views.nonaclist, name="nonaclist"),
    path("kingroomlist/<int:hid>", views.kingroomlist, name="kingroomlist"),
    path("queenroomlist/<int:hid>", views.queenroomlist, name="queenroomlist"),
    path("twinroomlist/<int:hid>", views.twinroomlist, name="twinroomlist"),
    path("singleroomlist/<int:hid>", views.singleroomlist, name="singleroomlist"),
    path("doubleroomlist/<int:hid>", views.doubleroomlist, name="doubleroomlist"),
    path(
        "doubledoubleroomlist/<int:hid>",
        views.doubledoubleroomlist,
        name="doubledoubleroomlist",
    ),
    path("range", views.range, name="range"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("createprofile/", views.createProfile, name="createprofile"),
    path("editprofile/<str:user>/", views.editProfile, name="editprofile"),
    path("myBooking", views.myBooking, name="myBooking"),
    # path("viewCart/", views.viewCart, name="viewCart"),
    # path("addCart/<int:rid>", views.addCart, name="addCart"),
    # path("removeCart/<int:rid>", views.removeCart, name="removeCart"),
    path("payment/", views.makePayment, name="payment"),
    path(
        "check_room_availability/<int:rid>",
        views.check_room_availability,
        name="check_room_availability",
    ),
    path("book-room", views.book_room_page, name="bookroompage"),
    path("book-room/book", views.book_room, name="bookroom"),
    path("payment/", views.makePayment, name="payment"),
]

from django.urls import path
from . import views

urlpatterns += [
    path('payment/', views.payment_page, name='payment_page'),
    path('process_payment/', views.process_payment, name='process_payment'),
]
