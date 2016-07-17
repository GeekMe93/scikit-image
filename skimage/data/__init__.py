"""Standard test images.

For more images, see

 - http://sipi.usc.edu/database/database.php

"""

import os as _os
import warnings

from .. import data_dir
from ..io import imread, use_plugin
from .._shared.utils import deprecated
from ._binary_blobs import binary_blobs
from .. import img_as_bool

__all__ = ['load',
           'camera',
           'lena',
           'text',
           'checkerboard',
           'coins',
           'moon',
           'page',
           'horse',
           'clock',
           'immunohistochemistry',
           'chelsea',
           'coffee',
           'hubble_deep_field',
           'rocket',
           'astronaut']


def load(f, as_grey=False):
    """Load an image file located in the data directory.

    Parameters
    ----------
    f : string
        File name.
    as_grey : bool, optional
        Convert to greyscale.

    Returns
    -------
    img : ndarray
        Image loaded from ``skimage.data_dir``.
    """
    use_plugin('pil')
    return imread(_os.path.join(data_dir, f), as_grey=as_grey)


def camera():
    """Gray-level "camera" image.

    Often used for segmentation and denoising examples.

    """
    return load("camera.png")


@deprecated('skimage.data.astronaut')
def lena():
    """Colour "Lena" image.

    **This image has been removed from scikit-image due to copyright
    concerns.**

    The standard, yet sometimes controversial Lena test image was
    scanned from the November 1972 edition of Playboy magazine.  From
    an image processing perspective, this image is useful because it
    contains smooth, textured, shaded as well as detail areas.

    """
    raise RuntimeError("This image has been removed due to copyright concerns.")


def astronaut():
    """Colour image of the astronaut Eileen Collins.

    Photograph of Eileen Collins, an American astronaut. She was selected
    as an astronaut in 1992 and first piloted the space shuttle STS-63 in
    1995. She retired in 2006 after spending a total of 38 days, 8 hours
    and 10 minutes in outer space.

    This image was downloaded from the NASA Great Images database
    <http://grin.hq.nasa.gov/ABSTRACTS/GPN-2000-001177.html>`__.

    No known copyright restrictions, released into the public domain.

    """

    return load("astronaut.png")


def text():
    """Gray-level "text" image used for corner detection.

    Notes
    -----
    This image was downloaded from Wikipedia
    <http://en.wikipedia.org/wiki/File:Corner.png>`__.

    No known copyright restrictions, released into the public domain.

    """

    return load("text.png")


def checkerboard():
    """Checkerboard image.

    Checkerboards are often used in image calibration, since the
    corner-points are easy to locate.  Because of the many parallel
    edges, they also visualise distortions particularly well.

    """
    return load("chessboard_GRAY.png")


def coins():
    """Greek coins from Pompeii.

    This image shows several coins outlined against a gray background.
    It is especially useful in, e.g. segmentation tests, where
    individual objects need to be identified against a background.
    The background shares enough grey levels with the coins that a
    simple segmentation is not sufficient.

    Notes
    -----
    This image was downloaded from the
    `Brooklyn Museum Collection
    <http://www.brooklynmuseum.org/opencollection/archives/image/617/image>`__.

    No known copyright restrictions.

    """
    return load("coins.png")


def moon():
    """Surface of the moon.

    This low-contrast image of the surface of the moon is useful for
    illustrating histogram equalization and contrast stretching.

    """
    return load("moon.png")


def page():
    """Scanned page.

    This image of printed text is useful for demonstrations requiring uneven
    background illumination.

    """
    return load("page.png")


def horse():
    """Black and white silhouette of a horse.

    This image was downloaded from
    `openclipart <http://openclipart.org/detail/158377/horse-by-marauder>`

    Released into public domain and drawn and uploaded by Andreas Preuss
    (marauder).

    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return img_as_bool(load("horse.png", as_grey=True))


def clock():
    """Motion blurred clock.

    This photograph of a wall clock was taken while moving the camera in an
    aproximately horizontal direction.  It may be used to illustrate
    inverse filters and deconvolution.

    Released into the public domain by the photographer (Stefan van der Walt).

    """
    return load("clock_motion.png")


def immunohistochemistry():
    """Immunohistochemical (IHC) staining with hematoxylin counterstaining.

    This picture shows colonic glands where the IHC expression of FHL2 protein
    is revealed with DAB. Hematoxylin counterstaining is applied to enhance the
    negative parts of the tissue.

    This image was acquired at the Center for Microscopy And Molecular Imaging
    (CMMI).

    No known copyright restrictions.

    """
    return load("ihc.png")


def chelsea():
    """Chelsea the cat.

    An example with texture, prominent edges in horizontal and diagonal
    directions, as well as features of differing scales.

    Notes
    -----
    No copyright restrictions.  CC0 by the photographer (Stefan van der Walt).

    """
    return load("chelsea.png")


def coffee():
    """Coffee cup.

    This photograph is courtesy of Pikolo Espresso Bar.
    It contains several elliptical shapes as well as varying texture (smooth
    porcelain to course wood grain).

    Notes
    -----
    No copyright restrictions.  CC0 by the photographer (Rachel Michetti).

    """
    return load("coffee.png")


def hubble_deep_field():
    """Hubble eXtreme Deep Field.

    This photograph contains the Hubble Telescope's farthest ever view of
    the universe. It can be useful as an example for multi-scale
    detection.

    Notes
    -----
    This image was downloaded from
    `HubbleSite
    <http://hubblesite.org/newscenter/archive/releases/2012/37/image/a/>`__.

    The image was captured by NASA and `may be freely used in the
    public domain <http://www.nasa.gov/audience/formedia/features/MP_Photo_Guidelines.html>`_.

    """
    return load("hubble_deep_field.jpg")


def rocket():
    """Launch photo of DSCOVR on Falcon 9 by SpaceX.

    This is the launch photo of Falcon 9 carrying DSCOVR lifted off from
    SpaceX's Launch Complex 40 at Cape Canaveral Air Force Station, FL.

    Notes
    -----
    This image was downloaded from
    `SpaceX Photos
    <https://www.flickr.com/photos/spacexphotos/16511594820/in/photostream/>`__.

    The image was captured by SpaceX and `released in the public domain
    <http://arstechnica.com/tech-policy/2015/03/elon-musk-puts-spacex-photos-into-the-public-domain/>`_.

    """
    return load("rocket.jpg")
