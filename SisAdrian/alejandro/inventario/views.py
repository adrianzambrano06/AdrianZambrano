from django.shortcuts import render
from django.template.backends import django

from .models import *
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
# Create your views here.
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from django.http import HttpResponse

class grupolistar(ListView):
    model=grupo
    template_name='mantenimientos/grupolistar.html'
class grupoguardar(CreateView):
    model= grupo
    fields = ['gruponombre','grupoanulado']
    template_name = 'mantenimientos/grupoguardar.html'
    success_url = reverse_lazy('grupolistar')
class grupomodificar(UpdateView):
    model = grupo
    fields = ['gruponombre','grupoanulado']
    template_name = 'mantenimientos/grupomodificar.html'
    success_url = reverse_lazy('grupolistar')
def hello_pdf(request):
    # Cree el objeto HttpResponse con los encabezados de PDF adecuados.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
    p = canvas.Canvas(response)

    # Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
    # Consulte la documentación de ReportLab para obtener la lista completa de funciones.
    p.drawString(100, 100, "Hello world.")

    # Cierre el objeto PDF limpiamente y listo.
    p.showPage()
    p.save()
    return response
def grupos_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   grupos = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Registros", styles['Heading1'])
   grupos.append(header)
   headings = ('Id', 'Grupo', 'Activo')
   if not pk:
      todogrupos = [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.all().order_by('pk')]
   else:
      todogrupos = [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.filter(id=pk)]
   t = Table([headings] + todogrupos)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))
   grupos.append(t)
   doc.build(grupos)
   response.write(buff.getvalue())
   buff.close()
   return response
####################################################proveedor
class proveedorlistar(ListView):
    model=proveedor
    template_name='mantenimientos/proveedorlistar.html'
class proveedorguardar(CreateView):
    model= proveedor
    fields = ['proveedorcedula','proveedornombres','proveedortelefono','proveedoranulado']
    template_name = 'mantenimientos/proveedorguardar.html'
    success_url = reverse_lazy('proveedorlistar')
class proveedormodificar(UpdateView):
    model = proveedor
    fields = ['proveedorcedula', 'proveedornombres', 'proveedortelefono', 'proveedoranulado']
    template_name = 'mantenimientos/proveedormodificar.html'
    success_url = reverse_lazy('proveedorlistar')
def proveedor_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   lista = []
   styles = getSampleStyleSheet()
   header = Paragraph("LISTADO DE PROVEEDORES", styles['Heading1'])
   lista.append(header)
   headings = ('Id', 'Cedula', 'Nombre', 'Telefono', 'Activo')
   if not pk:
      todoproveedor = [(p.id, p.proveedorcedula, p.proveedornombres, p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.all().order_by('pk')]
   else:
      todoproveedor= [(p.id, p.proveedorcedula, p.proveedornombres, p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.filter(id=pk)]
   t = Table([headings] + todoproveedor)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (4, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))
   lista.append(t)
   doc.build(lista)
   response.write(buff.getvalue())
   buff.close()
   return response
###################################################cliente
class clientelistar(ListView):
    model=cliente
    template_name='mantenimientos/clientelistar.html'
class clienteguardar(CreateView):
    model= cliente
    fields = ['clientecedula','clientenombre','clientetelefono','clienteanulado']
    template_name = 'mantenimientos/clienteguardar.html'
    success_url = reverse_lazy('clientelistar')
class clientemodificar(UpdateView):
    model= cliente
    fields = ['clientecedula','clientenombre','clientetelefono','clienteanulado']
    template_name = 'mantenimientos/clientemodificar.html'
    success_url = reverse_lazy('clientelistar')
def cliente_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   lista = []
   styles = getSampleStyleSheet()
   header = Paragraph("LISTADO DE CLIENTES", styles['Heading1'])
   lista.append(header)
   headings = ('Id', 'Cedula', 'Nombre', 'Telefono', 'Activo')
   if not pk:
      todocliente = [(p.id, p.clientecedula, p.clientenombre, p.clientetelefono, p.clienteanulado)
                         for p in cliente.objects.all().order_by('pk')]
   else:
      todocliente= [(p.id, p.clientecedula, p.clientenombre, p.clientetelefono, p.clienteanulado)
                         for p in cliente.objects.filter(id=pk)]
   t = Table([headings] + todocliente)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (4, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))
   lista.append(t)
   doc.build(lista)
   response.write(buff.getvalue())
   buff.close()
   return response
########################## producto
class productolistar(ListView):
    model = producto
    template_name = 'mantenimientos/productolistar.html'


class productoguardar(CreateView):
    model = producto
    fields = ['productogrupo', 'productonombre', 'productopreciovta', 'productocodigo',
              'productoexistencia','productoanulado']
    template_name = 'mantenimientos/productoguardar.html'
    success_url = reverse_lazy('productolistar')


class productomodificar(UpdateView):
    model = producto
    fields =['productogrupo', 'productonombre', 'productopreciovta', 'productocodigo',
             'productoexistencia','productoanulado']
    template_name = 'mantenimientos/productomodificar.html'
    success_url = reverse_lazy('productolistar')


def producto_print(self, pk=None):
    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rigthMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=19,
                            )
    lista = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Productos", styles['Heading1'])
    lista.append(header)
    headings = ('Id', 'Grupo', 'Producto', 'Precio Vta', 'Código','Exitencia','Estado')
    if not pk:
        todoslista = [(p.id, p.productogrupo, p.productonombre, p.productopreciovta,
                       p.productocodigo, p.productoexistencia ,p.productoanulado)
                      for p in producto.objects.all().order_by('pk')]
    else:
        todoslista = [(p.id, p.productogrupo, p.productonombre, p.productopreciovta,
                       p.productocodigo,p.productoexistencia ,p.productoanulado)
                      for p in producto.objects.filter(id=pk)]
    t = Table([headings] + todoslista)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (8, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    lista.append(t)
    doc.build(lista)
    response.write(buff.getvalue())
    buff.close()
    return response

# LOGIN

