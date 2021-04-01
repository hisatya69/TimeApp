from django.shortcuts import render

# Create your views here.
def home_view(request):
    if request.method=='POST':
        secs=request.POST['t']
        sec=int(secs)
        print((secs))
        if sec < 60:
            context1={'sec':sec}
            return render(request,'index.html',context1)
        else:
            min=int(sec/60)
            secs=sec%60
            context2={'minutes':min,'seconds':secs}
            print(context2)
            return render(request,'index.html',context2)
    return render(request,'index.html')


# def time(request):
#     return render(request,'time.html')