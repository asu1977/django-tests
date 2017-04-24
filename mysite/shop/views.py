from django.shortcuts import render, get_object_or_404
from .models import Product
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def home(request):
    products = Product.objects.all()
    return render(request, "products/home.html", {"products": products})


def products_list(request):
    products = Product.objects.all()
    return render(request, "products/products_list.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/product_detail.html", {"product": product})


class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    sender = forms.EmailField()
    message = forms.CharField()
    copy = forms.BooleanField(required = False)


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        #Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['ВАШ_EMAIL_ДЛЯ_ПОЛУЧЕНИЯ_СООБЩЕНИЯ']
            #Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            #Переходим на другую страницу, если сообщение отправлено
            return render(request, 'products/thanks.html')
    else:
        #Заполняем форму
        form = ContactForm()
    #Отправляем форму на страницу
    return render(request, 'products/contact.html', {'form': form})
