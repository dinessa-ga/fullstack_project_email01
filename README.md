Django Simple Rest Api
Configuración
Crear un entorno virtual para aislar las dependencias de nuestros paquetes localmente
crear venv python -m venv env

Activar venv

En uso de Linux: source env/bin/activate

En uso de Windows: env\Scripts\activate

Instale Django y Django REST framework en el entorno virtual
pip install django
pip install djangorestframwork
Migrar base de datos
cd myapp
python manage.py migrate

