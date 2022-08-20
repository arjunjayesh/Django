D:\>pip install virtualenvwrapper-win
Collecting virtualenvwrapper-win
  Downloading virtualenvwrapper_win-1.2.7-py3-none-any.whl (18 kB)
Collecting virtualenv
  Downloading virtualenv-20.16.3-py2.py3-none-any.whl (8.8 MB)
     ---------------------------------------- 8.8/8.8 MB 7.1 MB/s eta 0:00:00
Collecting platformdirs<3,>=2.4
  Downloading platformdirs-2.5.2-py3-none-any.whl (14 kB)
Collecting filelock<4,>=3.4.1
  Downloading filelock-3.8.0-py3-none-any.whl (10 kB)
Collecting distlib<1,>=0.3.5
  Downloading distlib-0.3.5-py2.py3-none-any.whl (466 kB)
     ---------------------------------------- 467.0/467.0 kB 9.7 MB/s eta 0:00:00
Installing collected packages: distlib, platformdirs, filelock, virtualenv, virtualenvwrapper-win
Successfully installed distlib-0.3.5 filelock-3.8.0 platformdirs-2.5.2 virtualenv-20.16.3 virtualenvwrapper-win-1.2.7

D:\>cd ..

D:\>C:

C:\Users\arjun>cd Documents

C:\Users\arjun\Documents>cd C:\Users\arjun\PycharmProjects\Python_Basics\Django

C:\Users\arjun\PycharmProjects\Python_Basics\Django>pip install virtualenvwrapper-win
Requirement already satisfied: virtualenvwrapper-win in c:\users\arjun\appdata\local\programs\python\python310\lib\site-packages (1.2.7)
Requirement already satisfied: virtualenv in c:\users\arjun\appdata\local\programs\python\python310\lib\site-packages (from virtualenvwrapper-win) (20.16.3)
Requirement already satisfied: filelock<4,>=3.4.1 in c:\users\arjun\appdata\local\programs\python\python310\lib\site-packages (from virtualenv->virtualenvwrapper-win) (3.8.0)
Requirement already satisfied: platformdirs<3,>=2.4 in c:\users\arjun\appdata\local\programs\python\python310\lib\site-packages (from virtualenv->virtualenvwrapper-win) (2.5.2)
Requirement already satisfied: distlib<1,>=0.3.5 in c:\users\arjun\appdata\local\programs\python\python310\lib\site-packages (from virtualenv->virtualenvwrapper-win) (0.3.5)

C:\Users\arjun\PycharmProjects\Python_Basics\Django>mkvirtualenv

Usage: mkvirtualenv [mkvirtualenv-options] [virtualenv-options] DEST_DIR

  DEST_DIR              The name of the envirnment to create (must be last).

The new environment is automatically activated after being
initialized.

mkvirtualenv options:
  -a project_path       Associate existing path as project directory
  -i package            Install package in new environment. This option
                        can be repeated to install more than one package.
  -r requirements_file  requirements_file is passed to
                        pip install -r requirements_file

    NOTE: all mkvirtualenv-options must come before virtualenv-options!

Options not specified above are passed to virtualenv:

virtualenv -h
usage: virtualenv [--version] [--with-traceback] [-v | -q] [--read-only-app-data] [--app-data APP_DATA] [--reset-app-data] [--upgrade-embed-wheels] [--discovery {builtin}] [-p py] [--try-first-with py_exe]
                  [--creator {builtin,cpython3-win,venv}] [--seeder {app-data,pip}] [--no-seed] [--activators comma_sep_list] [--clear] [--no-vcs-ignore] [--system-site-packages] [--copies] [--no-download | --download]
                  [--extra-search-dir d [d ...]] [--pip version] [--setuptools version] [--wheel version] [--no-pip] [--no-setuptools] [--no-wheel] [--no-periodic-update] [--symlink-app-data] [--prompt prompt] [-h]
                  dest

options:
  --version                     display the version of the virtualenv package and its location, then exit
  --with-traceback              on failure also display the stacktrace internals of virtualenv (default: False)
  --read-only-app-data          use app data folder in read-only mode (write operations will fail with error) (default: False)
  --app-data APP_DATA           a data folder used as cache by the virtualenv (default: C:\Users\arjun\AppData\Local\pypa\virtualenv)
  --reset-app-data              start with empty app data folder (default: False)
  --upgrade-embed-wheels        trigger a manual update of the embedded wheels (default: False)
  -h, --help                    show this help message and exit

verbosity:
  verbosity = verbose - quiet, default INFO, mapping => CRITICAL=0, ERROR=1, WARNING=2, INFO=3, DEBUG=4, NOTSET=5

  -v, --verbose                 increase verbosity (default: 2)
  -q, --quiet                   decrease verbosity (default: 0)

discovery:
  discover and provide a target interpreter

  --discovery {builtin}         interpreter discovery method (default: builtin)
  -p py, --python py            interpreter based on what to create environment (path/identifier) - by default use the interpreter where the tool is installed - first found wins (default: [])
  --try-first-with py_exe       try first these interpreters before starting the discovery (default: [])

creator:
  options for creator builtin

  --creator {builtin,cpython3-win,venv}
                                create environment via (builtin = cpython3-win) (default: builtin)
  dest                          directory to create virtualenv at
  --clear                       remove the destination directory if exist before starting (will overwrite files otherwise) (default: False)
  --no-vcs-ignore               don't create VCS ignore directive in the destination directory (default: False)
  --system-site-packages        give the virtual environment access to the system site-packages dir (default: False)
  --copies, --always-copy       try to use copies rather than symlinks, even when symlinks are the default for the platform (default: True)

seeder:
  options for seeder app-data

  --seeder {app-data,pip}       seed packages install method (default: app-data)
  --no-seed, --without-pip      do not install seed packages (default: False)
  --no-download, --never-download
                                pass to disable download of the latest pip/setuptools/wheel from PyPI (default: True)
  --download                    pass to enable download of the latest pip/setuptools/wheel from PyPI (default: False)
  --extra-search-dir d [d ...]  a path containing wheels to extend the internal wheel list (can be set 1+ times) (default: [])
  --pip version                 version of pip to install as seed: embed, bundle or exact version (default: bundle)
  --setuptools version          version of setuptools to install as seed: embed, bundle or exact version (default: bundle)
  --wheel version               version of wheel to install as seed: embed, bundle or exact version (default: bundle)
  --no-pip                      do not install pip (default: False)
  --no-setuptools               do not install setuptools (default: False)
  --no-wheel                    do not install wheel (default: False)
  --no-periodic-update          disable the periodic (once every 14 days) update of the embedded wheels (default: False)
  --symlink-app-data            not supported - symlink the python packages from the app-data folder (requires seed pip>=19.3) (default: False)

activators:
  options for activation scripts

  --activators comma_sep_list   activators to generate - default is all supported (default: bash,batch,fish,nushell,powershell,python)
  --prompt prompt               provides an alternative prompt prefix for this environment (value of . means name of the current working directory) (default: None)

config file C:\Users\arjun\AppData\Local\pypa\virtualenv\virtualenv.ini missing (change via env var VIRTUALENV_CONFIG_FILE)

1 was unexpected at this time.
C:\Users\arjun\PycharmProjects\Python_Basics\Django>mkvirtualenv inmakes
 C:\Users\arjun\Envs is not a directory, creating
created virtual environment CPython3.10.6.final.0-64 in 6715ms
  creator CPython3Windows(dest=C:\Users\arjun\Envs\inmakes, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\arjun\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.2.2, setuptools==63.4.1, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django>pip install Django
Collecting Django
  Downloading Django-4.1-py3-none-any.whl (8.1 MB)
     ---------------------------------------- 8.1/8.1 MB 6.9 MB/s eta 0:00:00
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     ---------------------------------------- 42.3/42.3 kB ? eta 0:00:00
Collecting asgiref<4,>=3.5.2
  Downloading asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting tzdata
  Downloading tzdata-2022.2-py2.py3-none-any.whl (336 kB)
     ---------------------------------------- 336.4/336.4 kB 6.9 MB/s eta 0:00:00
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-4.1 asgiref-3.5.2 sqlparse-0.4.2 tzdata-2022.2

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django>mkdir travelproject

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django>cd travelproject

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django\travelproject>django-admin start project travelproject
No Django settings specified.
Unknown command: 'start'. Did you mean startapp?
Type 'django-admin help' for usage.

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django\travelproject>django-admin startproject travelproject

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django\travelproject>cd travelproject

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django\travelproject\travelproject>python manage.py startapp travelapp

(inmakes) C:\Users\arjun\PycharmProjects\Python_Basics\Django\travelproject\travelproject>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 16, 2022 - 12:22:44
Django version 4.1, using settings 'travelproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[16/Aug/2022 12:23:14] "GET / HTTP/1.1" 200 10681
[16/Aug/2022 12:23:15] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[16/Aug/2022 12:23:15] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[16/Aug/2022 12:23:15] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[16/Aug/2022 12:23:15] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[16/Aug/2022 12:23:15] "GET /favicon.ico HTTP/1.1" 404 2117


MVT Architecture - Model View Template
Model - Table
View - To display
Template - HTML code


Create Project & App

C:\Users\arjun\PycharmProjects\Django\Project_1>django-admin startproject travelproject

C:\Users\arjun\PycharmProjects\Django\Project_1>cd travelproject

C:\Users\arjun\PycharmProjects\Django\Project_1\travelproject>python manage.py startapp travelapp

C:\Users\arjun\PycharmProjects\Django\Project_1\travelproject>python manage.py runserver


python manage.py startapp travelapp

Settings.py --> 
Installed Apps
Templates-> DIR -> os.path.join(BASE_DIR,'templates')

urls.py-->

Create View
urls.py-->path('',include('travelapp.urls)


STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

{% static '
'%}








