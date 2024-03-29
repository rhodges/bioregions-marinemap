# Django settings for bmm project.
from lingcod.common.default_settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIME_ZONE = 'America/Vancouver'
ROOT_URLCONF = 'bmm.urls'

GEOMETRY_DB_SRID = 54009
DISPLAY_AREA_UNITS = 'sq_km'
#KML_SIMPLIFY_TOLERANCE = .0002 #overriding this setting to account for lat/lon db srid
KML_SIMPLIFY_TOLERANCE_DEGREES = .025 #overriding this setting to account for lat/lon db srid
KML_ALTITUDEMODE_DEFAULT = 'clampToGround'

TEMPLATE_DIRS = ( os.path.realpath(os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')), )

INSTALLED_APPS += ( 'mybioregions', 
                    'analysis',
                    'lingcod.analysistools', #necessary?
                    'django.contrib.humanize',
                    'lingcod.raster_stats'
                  )

COMPRESS_CSS['application']['source_filenames'] += (
    'bmm/css/analysis_report.css',
    'kmltree/dist/kmltree_mod.css',
)

COMPRESS_JS['application']['source_filenames'] += (
    'bmm/js/jquery.qtip-1.0.0-rc3.min.js',
)

# bioregions.labs.ecotrust.org 
GOOGLE_API_KEY = 'ABQIAAAAn9EXtJkKOlQBGEfk28CiahQkv7FNjWKr_TVFL7EgIFo2pXN1jRRz4grU7hzFNhpS8coxw1Dz219KfQ'
# bioregions.labs.ecotrust.org:8000
#GOOGLE_API_KEY = 'ABQIAAAAn9EXtJkKOlQBGEfk28CiahTSuF7m83X3uEERz7nj3jSiHAkiaxQeB-tWbTkStcVCW35ldeO0TwWa5g'

LOG_FILE =  os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'bmm.log'))
#LOG_FILE = '/usr/local/apps/bioregions/bmm.log'
LOGFILE =  os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'bmm.log'))

APP_NAME = "The Bioregion Discovery Tool"

GROUP_REGISTERED_BY_WEB = 'Community Members'

STATICMAP_AUTOZOOM = False

GRASS_LOCATION = 'world_moll3'
GRASS_GISBASE = '/usr/local/grass-6.4.1RC2'
GRASS_GISDBASE = '/home/grass'

STATIC_URL = ADMIN_MEDIA_PREFIX
HELP_EMAIL = 'bioregions@ecotrust.org'

TITLES = { 'self': 'Reports', }

REMOVE_MAPSET_AFTER_RUN = True

from settings_local import *
