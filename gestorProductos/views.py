from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required

def inventarioAdmin(request):
    productos = Producto.objects.all()
    return render(request, 'gestorProductos/productosAdmin.html', {'productos': productos})


# Vista para listar productos
@login_required
def productos_admin(request):
    productos = Producto.objects.all()
    return render(request, 'productosAdmin.html', {'productos': productos})

@login_required
def productos_usuario(request):
    productos = Producto.objects.filter(creado_por=request.user)
    return render(request, 'gestorProductos/productosUsuario.html', {'productos': productos})

def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'categorias': categorias})

@login_required
def lista_productos_usuario(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()  # Superusuario ve todos los productos
    else:
        productos = Producto.objects.filter(creado_por=request.user)  # Usuarios ven solo sus productos
    return render(request, 'gestorProductos/productosUsuario.html', {'productos': productos})

# Vista para agregar productos
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creado_por = request.user #asignar el usuario actual
            form.save()  # Guardar el nuevo producto en la base de datos
            return redirect('productosAdmin')  # Redirigir a la lista de productos
    else:
        form = ProductoForm()  # Crear un formulario vacío

    return render(request, 'gestorProductos/agregar_producto.html', {'form': form})
# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    # Obtener el producto a eliminar
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Eliminar el producto
    producto.delete()
    
    # Redirigir al listado de productos
    return redirect('productosAdmin')
    
# Vista para editar un producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    form = ProductoForm(instance = producto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productosAdmin') 
    else:
        form = ProductoForm()
    
    return render(request, 'gestorProductos/agregar_producto.html', {'form': form})

@login_required
def editar_producto_usuario(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, creado_por=request.user)  # Filtrar por usuario
    form = ProductoForm(instance=producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productosUsuario')
    return render(request, 'gestorProductos/agregar_producto.html', {'form': form})

@login_required
def eliminar_producto_usuario(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, creado_por=request.user)  # Filtrar por usuario
    producto.delete()
    return redirect('productosUsuario')


#vista para mostrar los productos generados en la pagina principal
def index(request):
    productos = Producto.objects.all()  
    return render(request, 'index.html', {'productos': productos})

#redirgir vista segun usuario
def gestionar_productos(request):
    if request.user.is_superuser:
        return redirect('productosAdmin')  # Ruta definida en las URLs para superusuario
    elif request.user.is_authenticated:
        return redirect('productosUsuario')  # Ruta definida en las URLs para usuario normal
    else:
        return redirect('login')  # Si no está autenticado, redirigir al login


""" def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')

        # Validación y guardado
        if categoria_id:
            producto.categoria = get_object_or_404(Categoria, id=categoria_id)
            producto.save()
            return redirect('lista_productos')

    categorias = Categoria.objects.all()
    return render(request, 'editar_producto.html', {'producto': producto, 'categorias': categorias}) """



# Vista para agregar una categoría
""" def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        if nombre:
            Categoria.objects.create(nombre=nombre, descripcion=descripcion)
            return redirect('lista_productos')

    return render(request, 'agregar_categoria.html')

# Vista para eliminar una categoría
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_productos')
    return render(request, 'confirmar_eliminacion_categoria.html', {'categoria': categoria})
 """