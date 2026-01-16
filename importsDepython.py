import os
import re

paquetes_comunes = {
    'django': 'django',
    'rest_framework': 'djangorestframework',
    'PIL': 'pillow',
    'psycopg2': 'psycopg2-binary',
    'mysql': 'mysqlclient',
    'corsheaders': 'django-cors-headers',
    'drf_yasg': 'drf-yasg',
    'whitenoise': 'whitenoise',
    'gunicorn': 'gunicorn',
    'environ': 'django-environ',
    'storages': 'django-storages',
    'ckeditor': 'django-ckeditor',
}

encontrados = set()

# Buscar en todos los archivos .py
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            ruta = os.path.join(root, file)
            with open(ruta, 'r', encoding='utf-8', errors='ignore') as f:
                contenido = f.read()
                
                # Buscar imports
                imports = re.findall(r'^\s*(?:import|from)\s+(\w+)', contenido, re.MULTILINE)
                for imp in imports:
                    if imp in paquetes_comunes:
                        encontrados.add(paquetes_comunes[imp])

# Agregar Django por defecto (si es proyecto Django)
encontrados.add('django')

# Guardar requirements.txt
with open('requirements_inferido.txt', 'w') as f:
    for pkg in sorted(encontrados):
        f.write(f'{pkg}\n')

print(f'Se encontraron {len(encontrados)} paquetes:')
for pkg in sorted(encontrados):
    print(f'  - {pkg}')