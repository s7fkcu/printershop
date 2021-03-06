# -*- coding: utf-8 -*-

import os
def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

TEST = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('codeman', 'shalyapinalexander@gmail.com'),
)

MANAGERS = ADMINS

if TEST:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3', 
			'NAME': 'datebase',
			'USER': '',
			'PASSWORD': '',
			'HOST': '',
			'PORT': '',
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'laserpat_laser40',
			'USER': 'laserpat_laser40',
			'PASSWORD': 'x3oPWjst',
			'HOST': 'localhost',
			'PORT': '5432',
		}
	}

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'da'

gettext = lambda s: s
LANGUAGES = (
	('da', gettext('Danish')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = '/home/hosting_laserpatrongenbrug/projects/laserpatrongenbrug/media/'
STATIC_ROOT = MEDIA_ROOT

MEDIA_URL = '/media/'
STATIC_URL = MEDIA_URL

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '#09vt1wob9o2g(z73n*q@25mxqi7$b9=j8ycuhsft3_ayh_iaf'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	#'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.gzip.GZipMiddleware',
	
	'my_flatpages.middleware.FlatpageFallbackMiddleware',
	'shop.middleware.ShopSessionMiddleware',
)

ROOT_URLCONF = 'www.urls'

TEMPLATE_DIRS = (
	rel('templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',

	# django 1.2 only
	'django.contrib.messages.context_processors.messages',

	# required by django-admin-tools
	'django.core.context_processors.request',

	'configuration.context_processors.config_proc',
	'project.context_processors.translate_interface_proc',
)

INSTALLED_APPS = (
	'tinymce',
	'filebrowser',
	
	'admin_tools',
	'admin_tools.theming',
	'admin_tools.menu',
	'admin_tools.dashboard',
	
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.sitemaps',

	'my_flatpages',
	'project',
	'shop',
	'questionanswer',
	'actions',
	'feedback',
	'configuration',
	'paginator',
	'parsers.exelparser',
	'pay',
	'sms',
	
	'sorl.thumbnail',
	'captcha',
	'mptt',
	'rosetta',
)

PAGINATE_BY = 10

SHOP_COUNT_NEW_POPULARITY = 30
SHOP_VAT = 0.25

PAY_MERCHANT_NUMBER = '8010472'

SMS_PARAMS = {
	'from':'LaserToner',
	'apikey':'MRQMWD41S67W0DW8FS100E87H6KWT3RZV7V0Z4526VNL68D2NZS2I4VS7MG472FW',
}
SMS_URL_SEND = 'http://smspilot.ru/api.php'

#CACHE_BACKEND = 'db://shop_cache?max_entries=100000'

MPTT_ADMIN_LEVEL_INDENT = 40

DEFAULT_FROM_EMAIL = 'info@laserpatrongenbrug.dk'
AUTH_USER_EMAIL_UNIQUE = True
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False

ADMIN_TOOLS_MENU = 'www.dashboard.CustomMenuDashboard'
ADMIN_TOOLS_INDEX_DASHBOARD = 'www.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'www.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_THEMING_CSS = 'admin_tools/css/theming_tomu.css'

TINYMCE_JS_URL = '/media/js/tiny_mce/tiny_mce_src.js'
TINYMCE_SPELLCHECKER=False
TINYMCE_PLUGINS = [
    'safari',
    'table',
    'advlink',
    'advimage',
    'iespell',
    'inlinepopups',
    'media',
    'searchreplace',
    'contextmenu',
    'paste',
    'wordcount'
]

TINYMCE_DEFAULT_CONFIG={
	'theme' : "advanced",
	'plugins' : ",".join(TINYMCE_PLUGINS),
	#'language' : 'ru',
	'theme_advanced_buttons1' : "undo,redo,|,bold,italic,underline,strikethrough,|,bullist,numlist,|,justifyleft,justifycenter,justifyright,justifyfull,fontselect,fontsizeselect,|,outdent,indent,blockquote,|,forecolor,backcolor",
	'theme_advanced_buttons2' : "table,|,delete_row,delete_table,|,row_after,row_before,|,cut,copy,paste,pastetext,pasteword,|,search,replace,|,link,unlink,|,link,unlink,anchor,image,media,|,cleanup,|,code",
	'theme_advanced_buttons3' : "",
	'theme_advanced_buttons4' : "",
	'theme_advanced_toolbar_location' : "top",
	'theme_advanced_toolbar_align' : "left",
	'theme_advanced_statusbar_location' : "bottom",
	'theme_advanced_resizing' : True,
	'table_default_cellpadding': 2,
	'table_default_cellspacing': 2,
	'cleanup_on_startup' : False,
	'cleanup' : False,
	'paste_auto_cleanup_on_paste' : False,
	'paste_block_drop' : False,
	'paste_remove_spans' : False,
	'paste_strip_class_attributes' : False,
	'paste_retain_style_properties' : "",
	'forced_root_block' : False,
	'force_br_newlines' : False,
	'force_p_newlines' : True,
	'remove_linebreaks' : False,
	'convert_newlines_to_brs' : False,
	'inline_styles' : False,
	'relative_urls' : False,
	'formats' : {
		'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
		'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
		'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
		'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
		'strikethrough' : {'inline' : 'del'},
		'italic' : {'inline' : 'em'},
		'bold' : {'inline' : 'strong'},
		'underline' : {'inline' : 'u'}
	},
	'pagebreak_separator' : "",
	'content_css' : MEDIA_URL + "css/text.css",
}

FILEBROWSER_DIRECTORY = 'upload/'
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_URL_TINYMCE = MEDIA_URL + 'js/tiny_mce/'
FILEBROWSER_PATH_TINYMCE = os.path.join(MEDIA_ROOT, 'js', 'tiny_mce')

FILEBROWSER_MAX_UPLOAD_SIZE = 1048576000

FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm','swf'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p'],
    'Code': ['.html','.py','.js','.css']
}

FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': ''},
    'small': {'verbose_name': 'Small (300px)', 'width': 300, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (460px)', 'width': 460, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (620px)', 'width': 620, 'height': '', 'opts': ''},
    'cropped': {'verbose_name': 'Cropped (60x60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'croppedthumbnail': {'verbose_name': 'Cropped Thumbnail (140x140px)', 'width': 140, 'height': 140, 'opts': 'crop'},
}
