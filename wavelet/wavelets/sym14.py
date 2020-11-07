""" Symlet 14 wavelet """


class Symlet14:
    """
    Properties
    ----------
     near symmetric, orthogonal, biorthogonal

    All values are from http://wavelets.pybytes.com/wavelet/sym14/
    """
    __name__ = "Symlet Wavelet 14"
    __motherWaveletLength__ = 28  # length of the mother wavelet
    __transformWaveletLength__ = 2  # minimum wavelength of input signal

    # decomposition filter
    # low-pass
    decompositionLowFilter = [
        -2.5879090265397886e-05,
        1.1210865808890361e-05,
        0.00039843567297594335,
        -6.286542481477636e-05,
        -0.002579441725933078,
        0.0003664765736601183,
        0.01003769371767227,
        -0.002753774791224071,
        -0.029196217764038187,
        0.004280520499019378,
        0.03743308836285345,
        -0.057634498351326995,
        -0.03531811211497973,
        0.39320152196208885,
        0.7599762419610909,
        0.4753357626342066,
        -0.05811182331771783,
        -0.15999741114652205,
        0.02589858753104667,
        0.06982761636180755,
        -0.002365048836740385,
        -0.019439314263626713,
        0.0010131419871842082,
        0.004532677471945648,
        -7.321421356702399e-05,
        -0.0006057601824664335,
        1.9329016965523917e-05,
        4.4618977991475265e-05,
    ]

    # high-pass
    decompositionHighFilter = [
        -4.4618977991475265e-05,
        1.9329016965523917e-05,
        0.0006057601824664335,
        -7.321421356702399e-05,
        -0.004532677471945648,
        0.0010131419871842082,
        0.019439314263626713,
        -0.002365048836740385,
        -0.06982761636180755,
        0.02589858753104667,
        0.15999741114652205,
        -0.05811182331771783,
        -0.4753357626342066,
        0.7599762419610909,
        -0.39320152196208885,
        -0.03531811211497973,
        0.057634498351326995,
        0.03743308836285345,
        -0.004280520499019378,
        -0.029196217764038187,
        0.002753774791224071,
        0.01003769371767227,
        -0.0003664765736601183,
        -0.002579441725933078,
        6.286542481477636e-05,
        0.00039843567297594335,
        -1.1210865808890361e-05,
        -2.5879090265397886e-05,
    ]

    # reconstruction filters
    # low pass
    reconstructionLowFilter = [
        4.4618977991475265e-05,
        1.9329016965523917e-05,
        -0.0006057601824664335,
        -7.321421356702399e-05,
        0.004532677471945648,
        0.0010131419871842082,
        -0.019439314263626713,
        -0.002365048836740385,
        0.06982761636180755,
        0.02589858753104667,
        -0.15999741114652205,
        -0.05811182331771783,
        0.4753357626342066,
        0.7599762419610909,
        0.39320152196208885,
        -0.03531811211497973,
        -0.057634498351326995,
        0.03743308836285345,
        0.004280520499019378,
        -0.029196217764038187,
        -0.002753774791224071,
        0.01003769371767227,
        0.0003664765736601183,
        -0.002579441725933078,
        -6.286542481477636e-05,
        0.00039843567297594335,
        1.1210865808890361e-05,
        -2.5879090265397886e-05,
    ]

    # high-pass
    reconstructionHighFilter = [
        -2.5879090265397886e-05,
        -1.1210865808890361e-05,
        0.00039843567297594335,
        6.286542481477636e-05,
        -0.002579441725933078,
        -0.0003664765736601183,
        0.01003769371767227,
        0.002753774791224071,
        -0.029196217764038187,
        -0.004280520499019378,
        0.03743308836285345,
        0.057634498351326995,
        -0.03531811211497973,
        -0.39320152196208885,
        0.7599762419610909,
        -0.4753357626342066,
        -0.05811182331771783,
        0.15999741114652205,
        0.02589858753104667,
        -0.06982761636180755,
        -0.002365048836740385,
        0.019439314263626713,
        0.0010131419871842082,
        -0.004532677471945648,
        -7.321421356702399e-05,
        0.0006057601824664335,
        1.9329016965523917e-05,
        -4.4618977991475265e-05,
    ]
