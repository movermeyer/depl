from . import AptPackageRepository, Package

APT_REPO = \
    "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen"


def load(settings):
    def setup():
        s

    repos = [AptPackageRepository(APT_REPO)]
    return set([Package('mongodb-10gen', repos)]), [setup]