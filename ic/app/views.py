import imp
from django.shortcuts import render
from django.views import View
from .models import Fort,Food, painting,PerfArts,freedomar,musicali,textile

def home(request):
    return render(request, 'app/index.html')

def fort(request):
    fort = Fort.objects.all()
    return render(request, 'app/fortdetail.html',{'fort':fort})

class fortdetailview(View):
    def get(self, request, pk):
     fort = Fort.objects.get(pk=pk)
     return render(request, 'app/fortde2.html',{'fort':fort})

def food(request):
    food = Food.objects.all()
    return render(request, 'app/food.html',{'foods':food})

class fooddetailview(View):
    def get(self, request, pk):
     food = Food.objects.get(pk=pk)
     return render(request, 'app/fooddetail.html',{'food':food})


class ProductView(View):
    def get(self,request):
        paint = painting.objects.filter(category='P')
        museum = painting.objects.filter(category='M')
        return render(request, 'app/painting.html',{'paint':paint, 'museum':museum})


class productdetailview(View):
    def get(self, request, pk):
     paint = painting.objects.get(pk=pk)
     return render(request, 'app/paintingdetail.html',{'paint':paint})


def pa(request):
    pa = PerfArts.objects.all()
    return render(request, 'app/perfomingarts.html',{'pa':pa})

class padetailview(View):
    def get(self, request, pk):
     pa = PerfArts.objects.get(pk=pk)
     return render(request, 'app/perfdetails.html',{'pa':pa})


class freedom(View):
    def get(self,request):
        rb = freedomar.objects.filter(category='R')
        images = freedomar.objects.filter(category='I')
        clip = freedomar.objects.filter(category='N')
       
        return render(request, 'app/freedomarchieve.html',{'rb':rb, 'images':images,'clip':clip})


class frdetailview(View):
    def get(self, request, pk):
     fr = freedomar.objects.get(pk=pk)
     return render(request, 'app/freedetails.html',{'fr':fr})




class music(View):
    def get(self,request):
        avan = musicali.objects.filter(category='A')
        tat = musicali.objects.filter(category='T')
        ghan = musicali.objects.filter(category='G')
        sush = musicali.objects.filter(category='S')

       
        return render(request, 'app/musicalsub.html',{'avan':avan, 'tat':tat,'ghan':ghan, 'sush':sush})


class mdetailview(View):
    def get(self, request, pk):
     mi = musicali.objects.get(pk=pk)
     return render(request, 'app/musicaldetail.html',{'mi':mi})



class textiles(View):
    def get(self,request):
        weav = textile.objects.filter(category='W')
        print = textile.objects.filter(category='P')
        embd = textile.objects.filter(category='E')
        return render(request, 'app/textiles.html',{'weav':weav, 'print':print,'embd':embd})


class textiledetailview(View):
    def get(self, request, pk):
     ti = textile.objects.get(pk=pk)
     return render(request, 'app/textilesdetail.html',{'ti':ti})