# Sistema de Gestión de Almacén

Este es un sistema de gestión de almacén desarrollado con Django, que permite administrar productos, clientes y pedidos.

## Características

- **Gestión de Productos:** Permite agregar, editar y eliminar productos. Cada producto puede tener una imagen asociada, descripción, precio y estado de oferta.

- **Gestión de Clientes:** Permite agregar y buscar clientes.

- **Gestión de Pedidos:** Crear y visualizar pedidos realizados por los clientes. #falta completar

- **Gestión de Pedidos:** Registro, inicio de sesión y cierre de sesión de usuarios.

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/matigarelik/Almacen.git

2. Crea un entorno virtual: `python -m venv myenv`.

3. Instala las dependencias del proyecto:
pip install -r requirements.txt

4. Realiza las migraciones de la base de datos:
python manage.py migrate

5. Inicia el servidor de desarrollo:
python manage.py runserver

Para utilizar las funcionalidades de usuario, como agregar productos al carrito de compras, Crea ina cuenta e inicia sesión con una cuenta de usuario regular.

## Uso

### Modificación de Productos

- La aplicación permite a los usuarios agregar, editar y eliminar productos.
- Al editar un producto, se puede cargar una imagen para ese producto. Si ya existe una imagen para el producto, la nueva imagen reemplazará a la anterior.
- Los campos de nombre, descripción, precio y oferta son obligatorios al agregar o editar un producto.

### Gestión de Ofertas

- Cada producto puede tener un estado de oferta, que se muestra en la lista de productos y en la página de detalles del producto.
- Al agregar o editar un producto, se puede especificar si el producto está en oferta. Si está en oferta, se mostrará un indicador de oferta junto al producto.

### Búsqueda de Productos

- Los usuarios pueden buscar productos utilizando el formulario de búsqueda en la página principal.
- La búsqueda se realiza en función del nombre y la descripción del producto.
- Los productos encontrados se muestran en una lista con sus detalles, incluyendo imagen, nombre, precio y estado de oferta.

## Contribución

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor abre un nuevo *issue* para discutir los cambios que te gustaría realizar o envía una solicitud de extracción (*pull request*).

