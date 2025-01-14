por temas de seguridad se apartó la configuración de la base de datos, crear la carpeta databasesettings.py dentro del archivo hacer lo siguiente: 
DBCONFIG = {
    'default': {
        'ENGINE': 'tipo_bd',
        'NAME': 'name',
        'USER':'user',
        'PASSWORD': 'pass',
        'HOST': 'HOST',
        'PORT': 'port',
    }
}
