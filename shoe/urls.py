from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShoeHome"),
    path("men", views.Men, name="ShoeMen"),
    path("basic", views.Basic, name="ShoeBasic"),
    path("signup", views.Signup, name="SignUp"),
    path("login", views.Login, name="Login"),
    path("logout", views.logout, name="Logout"),
    path('viewdata', views.viewdata, name='viewdata'),
    path('checkuser', views.checklogin, name='checkuser'),
    path('contactdetails', views.ContactDetails, name='ContactDetails'),
    path("women", views.Women, name="ShoeWomen"),
    path("about", views.About, name="ShoeAbout"),
    path("shopall", views.Shopall, name="Shopall"),
    path("contact", views.Contact, name="ShoeContact"),
    path("product", views.Product, name="ProductDetail"),
    path("product/<int:myid>", views.productView, name="ProductDetail"),
    path("cart", views.Cart, name="ShoeCart"),
    path("checkout", views.Checkout, name="ShoeCheckout"),
    # path("handlerequest", views.handlerequest, name="handlerequest"),
    path("order-complete", views.OrderComplete, name="OrderComplete"),
    path("submitreview", views.SubmitReview, name="SubmitReview"),
    path("add-to-wishlist", views.AddToWishlist, name="AddToWishlist"),
    path("addtocart", views.AddToCart, name="AddToCart"),
    path("removeitem/<int:did>", views.RemoveFromCart, name="RemoveFromCart"),
    path("yourorders", views.YourOrders, name="YourOrders"),
]
