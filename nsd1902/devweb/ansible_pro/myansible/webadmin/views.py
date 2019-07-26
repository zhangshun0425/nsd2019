from django.shortcuts import render
from .models import HostGroup, Module

# Create your views here.

def webadmin_index(request):
    return render(request, 'webadmin_index.html')

def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:
            # get_or_create返回元组：(组实例，0/1)
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:
                g.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def add_modules(request):
    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})