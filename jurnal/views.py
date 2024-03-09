from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

from jurnal.models import Transaksi

def index(request):
    template = 'jurnal/transaksi_list.html'
    transaksi_list = Transaksi.objects.all
    context = {'transaksi_list': transaksi_list}
    return render(request, template, context)
    
def tambah(request):
    template = 'jurnal/transaksi_form.html'
    now = datetime.now()
    context = {'now': now.strftime('%Y-%m-%d')}
    return render(request, template, context)

def simpan(request):
    post = request.POST
    debit = int(post['debit'])
    kredit = int(post['kredit'])

    last_saldo = 0
    last_transaksi = Transaksi.objects.last()
    if (last_transaksi is not None):
        last_saldo = last_transaksi.saldo

    transaksi = Transaksi()
    transaksi.tanggal = post['tanggal']
    transaksi.uraian = post['uraian']
    transaksi.debit = debit
    transaksi.kredit = kredit
    transaksi.saldo = last_saldo + debit - kredit
    transaksi.save()

    return redirect('jurnal:index')
    
def hapus(request, id):
    if request.method == 'POST':
        Transaksi.objects.filter(id=id).delete()
    return redirect('jurnal:index')
