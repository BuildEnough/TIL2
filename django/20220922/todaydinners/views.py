from django.shortcuts import render
import random


# Create your views here.
def index(request):

    dinners = ['치킨', '피자', '마라탕', '꿔바로우', '족발', '김치찜', '순대국', '국밥', '된장국', '오믈렛']

    dinner = random.choice(dinners)

    context = {
        'dinner': dinner,
    }

    return render(request, 'dinner.html', context)



def lotto(request, number):
    print(number)
    
    return render(request, 'lotto.html')
