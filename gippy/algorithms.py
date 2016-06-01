# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_algorithms', [dirname(__file__)])
        except ImportError:
            import _algorithms
            return _algorithms
        if fp is not None:
            try:
                _mod = imp.load_module('_algorithms', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _algorithms = swig_import_helper()
    del swig_import_helper
else:
    import _algorithms
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import gippy

def acca(*args, **kwargs):
  """
    acca(GeoImage arg1, std::string filename, float arg3, float arg4, int arg5=5, int arg6=10, 
        int arg7=4000) -> GeoImage

    Parameters:
        arg1: gip::GeoImage const &
        filename: std::string
        arg3: float
        arg4: float
        arg5: int
        arg6: int
        arg7: int

    """
  return _algorithms.acca(*args, **kwargs)

def fmask(*args, **kwargs):
  """
    fmask(GeoImage geoimg, std::string filename, int arg3=3, int arg4=5) -> GeoImage

    Parameters:
        geoimg: gip::GeoImage const &
        filename: std::string
        arg3: int
        arg4: int

    """
  return _algorithms.fmask(*args, **kwargs)

def cookie_cutter(*args, **kwargs):
  """
    cookie_cutter(vector_GeoImage geoimgs, std::string filename="", GeoFeature feature=gip::GeoFeature(), 
        bool crop=False, std::string proj="EPSG:4326", float xres=1.0, float yres=1.0, 
        int interpolation=0) -> GeoImage

    Parameters:
        geoimgs: std::vector< gip::GeoImage,std::allocator< gip::GeoImage > > const &
        filename: std::string
        feature: gip::GeoFeature
        crop: bool
        proj: std::string
        xres: float
        yres: float
        interpolation: int

    """
  return _algorithms.cookie_cutter(*args, **kwargs)

def indices(*args, **kwargs):
  """
    indices(GeoImage geoimg, svector products, std::string filename="") -> GeoImage

    Parameters:
        geoimg: gip::GeoImage const &
        products: std::vector< std::string,std::allocator< std::string > >
        filename: std::string

    """
  return _algorithms.indices(*args, **kwargs)

def linear_transform(*args, **kwargs):
  """
    linear_transform(GeoImage geoimg, CImg< float > coef, std::string filename) -> GeoImage

    Parameters:
        geoimg: gip::GeoImage const &
        coef: CImg< float >
        filename: std::string

    """
  return _algorithms.linear_transform(*args, **kwargs)

def pansharp_brovey(*args, **kwargs):
  """
    pansharp_brovey(GeoImage geoimg, GeoImage panimg, CImg< float > weights=CImg< float >(), std::string filename="") -> GeoImage

    Parameters:
        geoimg: gip::GeoImage const &
        panimg: gip::GeoImage const &
        weights: CImg< float >
        filename: std::string

    """
  return _algorithms.pansharp_brovey(*args, **kwargs)

def rxd(*args, **kwargs):
  """
    rxd(GeoImage geoimg, std::string filename="") -> GeoImage

    Parameters:
        geoimg: gip::GeoImage const &
        filename: std::string

    """
  return _algorithms.rxd(*args, **kwargs)
# This file is compatible with both classic and new-style classes.


