from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate


def product_list(request):
    products = Product.objects.all()  # ดึงข้อมูลผลิตภัณฑ์ทั้งหมด
    return render(request, 'products/product_list.html', {'products': products})  # เรนเดอร์ Template สำหรับแสดงรายการผลิตภัณฑ์

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)  # รับข้อมูลจากฟอร์ม
        if form.is_valid():
            form.save()  # บันทึกผลิตภัณฑ์ใหม่
            return redirect('product_list')  # เปลี่ยนเส้นทางไปยังรายการผลิตภัณฑ์
    else:
        form = ProductForm()  # สร้างฟอร์มใหม่เมื่อไม่ใช่ POST
    return render(request, 'products/product_form.html', {'form': form})  # เรนเดอร์ Template สำหรับฟอร์มผลิตภัณฑ์

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)  # ดึงผลิตภัณฑ์ตาม ID
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)  # รับข้อมูลจากฟอร์มและใช้กับผลิตภัณฑ์ที่มีอยู่
        if form.is_valid():
            form.save()  # บันทึกการเปลี่ยนแปลง
            return redirect('product_list')  # เปลี่ยนเส้นทางไปยังรายการผลิตภัณฑ์
    else:
        form = ProductForm(instance=product)  # แสดงฟอร์มพร้อมข้อมูลที่มีอยู่
    return render(request, 'products/product_form.html', {'form': form})  # เรนเดอร์ Template สำหรับฟอร์มผลิตภัณฑ์

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)  # ดึงผลิตภัณฑ์ตาม ID
    if request.method == "POST":
        product.delete()  # ลบผลิตภัณฑ์
        return redirect('product_list')  # เปลี่ยนเส้นทางไปยังรายการผลิตภัณฑ์
    return render(request, 'products/product_confirm_delete.html', {'product': product})  # เรนเดอร์ Template ยืนยันการลบ

def yadom1(request):
    return render(request, 'products/yadom1_detail.html')

def yadom2(request):
    return render(request, 'products/yadom2_detail.html')

def yadom3(request):
    return render(request, 'products/yadom3_detail.html')

def login(request):
    return render(request, 'products/login.html')

def logout(request):
    return render(request, 'products/logout.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # ล็อกอินผู้ใช้หลังจากสมัคร
            return redirect('login')  # เปลี่ยนเส้นทางไปยังหน้ารายการผลิตภัณฑ์
    else:
        form = CustomUserCreationForm()
    return render(request, 'products/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # ใช้ฟังก์ชันที่นำเข้ามา
            return redirect('product_list')
        else:
            # จัดการกรณีการเข้าสู่ระบบที่ล้มเหลว
            ...
    return render(request, 'products/login.html')

def logout_view(request):
    auth_logout(request)  # เรียกใช้ฟังก์ชัน logout ของ Django
    return redirect('product_list')  # เปลี่ยนให้กลับไปที่หน้าเข้าสู่ระบบ 


