# Copyright 2023 Lawrence Livermore National Security, LLC
# See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: MIT

import surfactant.plugin
from surfactant.sbomtypes import SBOM


@surfactant.plugin.hookimpl
def write_sbom(sbom: SBOM, outfile) -> None:
    # outfile is a file pointer, not a file name
    outfile.write(sbom.to_json(indent=2))
