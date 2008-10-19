import os, datetime
ROOT_PATH = os.path.dirname(__file__)

# setting up directory paths
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH,'templates')
)
STATIC_DIR = os.path.join(ROOT_PATH,'static')
DEPLOY_DIR = os.path.join(ROOT_PATH,'deploy')
IMAGES_DIR = os.path.join(ROOT_PATH,'images')

# path for YUICompressor, or None if you don't
# want to compress JS/CSS.
#YUI_COMPRESSOR = "yuicompressor-2.3.6.jar"
YUI_COMPRESSOR = None

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
