import argparse
import importlib
import logging
import os
from pathlib import Path

import CIMgen

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger(__name__)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Generate some CIM classes.')
    parser.add_argument('outdir', type=Path, help='The output directory')
    parser.add_argument('schemadir', type=str, help='The schema directory')
    parser.add_argument('langdir', type=str, help='The langpack directory')
    args = parser.parse_args()

    # validate inputs
    langPack = importlib.import_module(args.langdir + ".langPack")
    schema_path = Path(os.path.join(os.getcwd(), args.schemadir))
    assert schema_path.is_dir(), args.outdir.is_dir()


    # main
    CIMgen.cim_generate(schema_path, args.outdir, "cgmes_v2_4_15", langPack)

    langPack.resolve_headers(args.outdir)
