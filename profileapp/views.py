# Create your views here.
from django.shortcuts import render, redirect


def home (request):
    return render(request, 'home.html')

def personal(request):
    return render(request, 'personal.html')

def educational(request):
    return render(request, 'educational.html')

def interests(request):
    return render(request, 'interests.html')

def sale(request):
    return render(request, 'sale.html')

def rolemodel(request):
    return render(request, 'rolemodel.html')

def showMyData(request):
    showID = '65342310169-9'
    showName = "ธัญญลักษณ์ กลอยกระโทก"
    showAddress = "467 หมู่ 3 ตำบลแวง อำเภอโพนทอง จังหวัดร้อยเอ็ด รหัสไปรษณีย์ 45110"
    showtel = "0834738224"
    showgender = "หญิง"
    showBirthday = "07 เมษายน พ.ศ 2544"
    showWeight = 46
    showHeight = 166
    showstatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product =['Daniel Wellington',5150.00,'../../static/images/w011.jpg']
    products.append(product)
    product =['GUESS', 5900.00,'../../static/images/w022.jpg']
    products.append(product)
    product =['CASIO',4700.00,'../../static/images/w033.jpg']
    products.append(product)
    product =['MICHAEL KORS',8500.00,'../../static/images/w044.jpg']
    products.append(product)
    product =['COACH', 9400.00,'../../static/images/w055.jpg']
    products.append(product)
    product = ['TOMMY HILFIGER', 8900.00,'../../static/images/w066.jpg']
    products.append(product)
    product = ['Calvin Klein', 8600.00,'../../static/images/w077.jpg']
    products.append(product)
    product = ['Burberry', 12640.00,'../../static/images/w088.jpg']
    products.append(product)
    product = ['Gucci', 44000.00,'../../static/images/w099.jpg']
    products.append(product)
    product = ['BABY-G', 4700.00,'../../static/images/w010.jpg']
    products.append(product)

    context = {'showID':showID,'showName':showName,'showAddress':showAddress,'showtel':showtel,
               'showgender':showgender,'showBirthday':showBirthday,'showWeight':showWeight,'showHeight':showHeight,
               'showstatus':showstatus,'showSchool':showSchool, 'products':products}
    return render(request,'showMyData.html',context)


lstOurProduct = []
from profileapp.models import *
from profileapp.forms import *


def listProduct(request):
    context = {'products': lstOurProduct}
    return render(request, 'listProduct.html', context)


def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            brand = form.get('brand')
            type = form.get('type')
            model = form.get('model')
            color = form.get('color')
            price = form.get('price')

            if price <= 1000:
                warranty = 1
            elif price <= 2000:
                warranty = 2
            elif price <= 3000:
                warranty = 3
            else:
                warranty = 4

            vat = price * 0.07
            net = price + vat
            pd = Product(id, brand, type, model, color, price, warranty, vat, net)
            lstOurProduct.append(pd)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, 'inputProduct.html', context)