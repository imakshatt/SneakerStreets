from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import SHOES_TABLE, LOGIN_TABLE, CONTACT_TABLE, CART_TABLE, BRAND_TABLE, CATEGORY_TABLE, ORDER_TABLE, FEEDBACK
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

# import paginator
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)


# Create your views here.
def index(request):
    # mydata = SHOES_TABLE.objects.all()
    # print(mydata)
    #
    # context = {
    #     'shoedata': mydata
    # }
    product = SHOES_TABLE.objects.all()
    productview = {
        'product': product
    }

    return render(request, 'index.html', productview)


def Men(request):
    menprodview = SHOES_TABLE.objects.filter(CATEGORY_ID=1)
    print(menprodview)

    default_page = 1
    page = request.GET.get('page', default_page)

    # Get queryset of items to paginate
    items = SHOES_TABLE.objects.filter(CATEGORY_ID=1)

    # Paginate items
    items_per_page = 4
    paginator = Paginator(items, items_per_page)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    # Provide filtered, paginated library items

    productview = {
        'menprodview': menprodview,
        'items_page': items_page
    }

    return render(request, 'men.html', productview)


def Women(request):
    womenprodview = SHOES_TABLE.objects.filter(CATEGORY_ID=2)
    print(womenprodview)

    default_page = 1
    page = request.GET.get('page', default_page)

    # Get queryset of items to paginate
    items = SHOES_TABLE.objects.filter(CATEGORY_ID=2)

    # Paginate items
    items_per_page = 4
    paginator = Paginator(items, items_per_page)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    productview = {
        'womenprodview': womenprodview,
        'items_page': items_page
    }

    return render(request, 'women.html', productview)


def Shopall(request):
    default_page = 1
    page = request.GET.get('page', default_page)

    # Get queryset of items to paginate
    items = SHOES_TABLE.objects.all()

    # Paginate items
    items_per_page = 8
    paginator = Paginator(items, items_per_page)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    productview = {
        'items_page': items_page,

    }
    return render(request, 'shopall.html', productview)


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Product(request):
    return render(request, 'product-detail.html')


def Cart(request):
    uid = request.session['log_id']
    # cartitems = CART_TABLE.objects.all()
    cartitems = CART_TABLE.objects.filter(L_ID=uid, ORDER_STATUS=0)

    # allitems = []
    #
    # for i in cartitems:
    #     price = SHOES_TABLE.object.get(id=i.SHOES_ID).PRICE
    #
    #     data = {
    #         'price': price
    #     }
    #     allitems += data
    # ais
    # print(allitems)
    carttotal = CART_TABLE.objects.filter(L_ID=uid, ORDER_STATUS=0).aggregate(Sum("FINAL_PRICE"))
    carttotal = carttotal.get("FINAL_PRICE__sum")

    print(carttotal)

    cartview = {
        'cartitems': cartitems,
        'carttotal': carttotal
    }

    return render(request, 'cart.html', cartview)


def Checkout(request):
    uid = request.session['log_id']
    carttotal = CART_TABLE.objects.filter(L_ID=uid, ORDER_STATUS=0).aggregate(Sum("FINAL_PRICE"))
    carttotal = carttotal.get("FINAL_PRICE__sum")
    uid = request.session['log_id']
    print(uid)
    UNAME = LOGIN_TABLE.objects.filter(id=uid)

    total = {
        'carttotal': carttotal,
        'UNAME': UNAME
    }
    return render(request, 'checkout.html', total)


def OrderComplete(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        paymentopt = request.POST.get("payment")
        print(paymentopt)
        uid = request.session['log_id']
        carttotal = CART_TABLE.objects.aggregate(Sum("FINAL_PRICE"))
        carttotal = carttotal.get("FINAL_PRICE__sum")
        orderdata = ORDER_TABLE(L_ID=LOGIN_TABLE(id=uid), ADDRESS=address, TOTAL_AMOUNT=carttotal,
                                PAYMENT_STATUS=paymentopt, ORDER_STATUS=0)
        orderdata.save()

        lasstid = ORDER_TABLE.objects.latest('id')

        print(lasstid)

        objid = lasstid.id
        print(objid)

        obj = CART_TABLE.objects.filter(L_ID=LOGIN_TABLE(id=uid))
        for object in obj:
            object.ORDER_ID = objid
            object.ORDER_STATUS = 1
            object.save()

        # param_dict = {
        #
        #     'MID': 'WorldP64425807474247',
        #     'ORDER_ID': 'ORDER_TABLE.id',
        #     'TXN_AMOUNT': '1',
        #     'CUST_ID': 'email',
        #     'INDUSTRY_TYPE_ID': 'Retail',
        #     'WEBSITE': 'WEBSTAGING',
        #     'CHANNEL_ID': 'WEB',
        #     'CALLBACK_URL': 'http://127.0.0.1:8000/handlepayment/',
        #
        # }

    return render(request, 'order-complete.html')


def AddToWishlist(request):
    return render(request, 'add-to-wishlist.html')


def Basic(request):
    uid = request.session['log_id']
    carttotal = CART_TABLE.objects.filter(L_ID=uid).count()
    print(carttotal)
    context = {
        'cartccount': carttotal
    }
    return render(request, 'basic.html', context)


def Signup(request):
    return render(request, 'signup.html')


def Login(request):
    return render(request, 'login.html')


def viewdata(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        name = request.POST.get("name")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        file = request.FILES['dp']

        logindata = LOGIN_TABLE(EMAIL_ID=email, NAME=name, PHONE_NO=phone, DOB=dob, ADDRESS=address, PASSWORD=password,
                                DP=file, ROLE=2, STATUS=1)
        logindata.save()
        messages.success(request, 'Data Inserted Successfully. you can login now')
    else:
        messages.error(request, 'error occured')

    return render(request, 'index.html')


def checklogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = LOGIN_TABLE.objects.get(EMAIL_ID=username, PASSWORD=password)
            request.session['log_user'] = user.EMAIL_ID
            request.session['log_id'] = user.id
            request.session.save()
            # print(user.dp)
            # context = {
            #     'dp' : user.dp
            # }
        except LOGIN_TABLE.DoesNotExist:
            user = None

        if user is not None:
            return redirect(index)  # ,context

        else:
            messages.error(request, 'Invalid USER ID')
    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_id']
    except:
        pass
    return redirect(index)


def ContactDetails(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        name = request.POST.get("name")
        message = request.POST.get("message")
        contactdata = CONTACT_TABLE(EMAIL_ID=email, FULL_NAME=name, PHONE_NO=phone, MESSAGE=message)
        contactdata.save()
        messages.success(request, 'Thank you for reaching out to us.')

    return render(request, 'contact.html')


def productView(request, myid):
    # Fetch the product using the id
    product = SHOES_TABLE.objects.filter(id=myid)
    return render(request, 'product-detail.html', {'product': product[0]})


def AddToCart(request):
    try:
        if request.session.is_empty():
            return render(request, 'login.html')
        else:
            try:
                if request.method == 'POST':
                    cartname = request.POST.get("currentname")
                    cartprice = request.POST.get("currentprice")
                    cartquantity = request.POST.get("quantity")
                    shoesid = request.POST.get("currentid")
                    finalprice = int(cartprice) * int(cartquantity)


                    # fetch foreign key values
                    fetchbrandid = SHOES_TABLE.objects.get(id=shoesid)
                    print(fetchbrandid.BRAND_ID)

                    fetchbid = BRAND_TABLE.objects.get(BRAND_NAME=fetchbrandid.BRAND_ID)
                    print(fetchbid.id)

                    uid = request.session['log_id']
                    print(uid)

                    fetchcatname = SHOES_TABLE.objects.get(id=shoesid)
                    print(fetchcatname.CATEGORY_ID)

                    fetchcatid = CATEGORY_TABLE.objects.get(CATEGORY_NAME=fetchcatname.CATEGORY_ID)
                    print(fetchcatid.id)

                    cartdata = CART_TABLE(SHOES_NAME=cartname, QUANTITY=cartquantity, SHOES_ID=SHOES_TABLE(id=shoesid),
                                          BRAND_ID=BRAND_TABLE(id=fetchbid.id),
                                          CATEGORY_ID=CATEGORY_TABLE(id=fetchcatid.id), L_ID=LOGIN_TABLE(id=uid),
                                          PRICE=cartprice, FINAL_PRICE=finalprice)
                    cartdata.save()

                    product = SHOES_TABLE.objects.all()
                    productview = {
                        'product': product,

                    }
                return redirect(Cart)
            except:
                pass
            return render(request, 'login.html')
    except:
        pass
    return render(request, 'login.html')


def RemoveFromCart(request, did):
    CART_TABLE.objects.filter(id=did).delete()

    cartitems = CART_TABLE.objects.all()
    carttotal = CART_TABLE.objects.aggregate(Sum("FINAL_PRICE"))
    carttotal = carttotal.get("FINAL_PRICE__sum")

    print(carttotal)

    context = {
        'cartitems': cartitems,
        'carttotal': carttotal
    }

    return render(request, 'cart.html', context)


def YourOrders(request):
    uid = request.session['log_id']
    yourorder = ORDER_TABLE.objects.filter(L_ID=uid)

    preview = {
        'yourorder': yourorder
    }

    return render(request, 'yourorders.html', preview)


# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     pass

def SubmitReview(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        ratings = request.POST.get("input-1")
        feedback = request.POST.get("feedback")
        print(ratings)
        print(feedback)
        subreview = FEEDBACK(L_ID=LOGIN_TABLE(id=uid), RATINGS=ratings, COMMENT=feedback)
        subreview.save()

    return redirect(index)
