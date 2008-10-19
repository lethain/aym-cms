import os, datetime
ROOT_PATH = os.path.dirname(__file__)

# setting up directory paths
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH,'templates')
)
STATIC_DIR = os.path.join(ROOT_PATH,'static')
DEPLOY_DIR = os.path.join(ROOT_PATH,'deploy')
IMAGES_DIR = os.path.join(ROOT_PATH,'images')
TMP_DIR = os.path.join(ROOT_PATH, 'aym_tmp_files')

# path for YUICompressor, or None if you don't
# want to compress JS/CSS.
YUI_COMPRESSOR = "yuicompressor-2.3.6.jar"
#YUI_COMPRESSOR = None

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
#HSS_PATH = "./hss"
HSS_PATH = None # if you don't want to use HSS


# Set true if you want to use CleverCSS with all .css files.
# Must be installed via "sudo easy_install CleverCSS" before
# usage.
USE_CLEVER_CSS = True
#USE_CLEVER_CSS = False
CLEVER_CSS_EXT = ".ccss"

# setting up some helpful values
STATIC_URL_FORMAT = u"/static/%s"
STATIC_THUMBNAIL_FORMAT = STATIC_URL_FORMAT % u"thumbnail/%s"
STATIC_IMAGE_FORMAT = STATIC_URL_FORMAT % u"image/%s"
THUMBNAIL_SIZE = (128,128)
EMAIL = u"your_email_address@gmail.com"

# creating default rendering context
CONTEXT = {
    'email':EMAIL,
    'now':datetime.datetime.now(),
}

PAGES_TO_RENDER = (
    u"index.html",
)

INSTALLED_APPS = (
    'aym_tags',
)
