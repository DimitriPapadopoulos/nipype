# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..converters import BSplineToDeformationField


def test_BSplineToDeformationField_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        defImage=dict(
            argstr='--defImage %s',
            hash_files=False,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        refImage=dict(argstr='--refImage %s', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        tfm=dict(argstr='--tfm %s', ),
    )
    inputs = BSplineToDeformationField.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BSplineToDeformationField_outputs():
    output_map = dict(defImage=dict(), )
    outputs = BSplineToDeformationField.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
