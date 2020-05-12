from BuildInfo import BuildInfo
import pdb
import os

try:
    __BuildInfo_Path__ = os.environ['SECUREBUILD_BUILDINFO_FILEPATH']
except KeyError:
    __BuildInfo_Path__ = '../data/test.buildinfo'

if not __BuildInfo_Path__:
    __BuildInfo_Path__ = '/output/secure-build.buildinfo'

if __name__ == "__main__":
    f = open(__BuildInfo_Path__, "r")
    buf = f.readlines()

    info = BuildInfo.from_str(buf)
    if not info.verify(os.environ['PATH'], os.environ['LD_LIBRARY_PATH']):
        print("build not verified")
        pdb.set_trace()
    else:
        print("build is verified")
        return 0

