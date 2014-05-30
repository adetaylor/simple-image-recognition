__author__ = 'adrian'

def find_blob(image, colour):
    """
    Find the most substantial area of the given colour within the image.

    The function searches for the largest area of the given colour, or a near colour,
    within the image, and returns the location of the centre of that area of colour.

    Should there be multiple areas of the colour within the given image, the algorithm will
    return details of the largest.

    When analysing the image the algorithm may have to choose between a large area of a vaguely
    similar colour, or a small area of a more perfectly similar colour. In this situation
    there are no guarantees about which blob it will specify. Such situations are best avoided
    in the input image.
    :param image: A 2D 'numpy' array of pixels
    :param colour: The colour being searched for
    :return: A tuple of (x, y, certainty) where x any are co-ordinates into the 2D array passed in,
    and certainty is a value from 0.0 (colour not found at all) to 1.0 (perfect colour match found
    at given location)
    """
    # Claire - please implement!
    return (0,0,0)