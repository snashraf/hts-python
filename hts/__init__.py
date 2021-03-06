from .fai import Fai
from .tbx import Tbx
from .bam import Bam
from .vcf import VCF
from .fisher import fisher_exact_test

__version__ = "0.0.3"


def doctests():
    import doctest
    import hts.htsffi
    for name, mod in (("htsffi", hts.htsffi),
                      ("fai", hts.fai),
                      ("fisher", hts.fisher),
                      ("vcf", hts.vcf),
                      ("bam", hts.bam)):

        mod = getattr(hts, name)
        print("%s: %r" % (name, doctest.testmod(m=mod,
                          optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)))
