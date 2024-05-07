#!/usr/bin/env python3

# script wrapping the invocation of auditwheel to vendor in shared libraries on linux
# output dir: wheelhouse (auditwheel default)

import argparse
import subprocess
import sysconfig
import os


def main(args):
    if "TOPOLOGIC_PLAT_NAME" in os.environ:
        platform_str = os.environ['TOPOLOGIC_PLAT_NAME']
    else:
        platform_str = sysconfig.get_platform().replace('-', '_')

    subprocess.run(["auditwheel", "repair",
                    f"--plat", f"{platform_str}",
                    "--strip",
                    "--exclude", "libdl.so.2", # these are in manylinux2014
                    "--exclude", "librt.so.1",
                    "--exclude", "libc.so.6",
                    "--exclude", "libm.so.6",
                    "--exclude", "libpthread.so.0",
                    args.wheel
                    ],
                   check=True
    )

def script():
    p = argparse.ArgumentParser(description="Vendor in .so dependencies of a wheel using auditwheel.")
    p.add_argument("--wheel", required=True, metavar="<path>")
    args = p.parse_args()
    main(args)


if __name__ == '__main__':
    script()
