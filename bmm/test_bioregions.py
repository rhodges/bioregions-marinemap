from django.core.management import setup_environ
import os
import sys
sys.path.append(os.path.dirname(__file__))

import settings
setup_environ(settings)

#==================================#
from mybioregions.models import *
from django.contrib.gis.geos import GEOSGeometry 
from django.contrib.auth.models import User, Group

def main():
    user = User.objects.get(username='demo')

    for model in [MyBioregion, Folder]:
        a = model.objects.all()
        for i in a:
            i.delete()

    g = GEOSGeometry('SRID=4326;POINT(-122.5 45.5)')

    bio1 = MyBioregion(user=user, name="bio1", 
            input_temp_weight = 0,
            input_language_weight = 0,
            input_precip_weight = 0,
            input_biomass_weight = 0,
            input_starting_point = g
            ) 
    bio1.save()

    bio2 = MyBioregion(user=user, name="bio2", 
            input_temp_weight = 50,
            input_language_weight = 0,
            input_precip_weight = 0,
            input_biomass_weight = 0,
            input_starting_point = g
            ) 
    bio2.save()

    area1 = (bio1.output_geom.area) / 10000.
    area2 = (bio2.output_geom.area) / 10000.
    print "\n"*4
    print area1/1000000., 'M Ha'
    print area2/1000000., 'M Ha'

if __name__ == '__main__':
    main()