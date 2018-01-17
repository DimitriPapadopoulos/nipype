# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..modelgen import SpecifySPMModel


def test_SpecifySPMModel_inputs():
    input_map = dict(
        concatenate_runs=dict(usedefault=True, ),
        event_files=dict(
            mandatory=True,
            xor=['subject_info', 'event_files'],
        ),
        functional_runs=dict(
            copyfile=False,
            mandatory=True,
        ),
        high_pass_filter_cutoff=dict(mandatory=True, ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        input_units=dict(mandatory=True, ),
        outlier_files=dict(copyfile=False, ),
        output_units=dict(usedefault=True, ),
        parameter_source=dict(usedefault=True, ),
        realignment_parameters=dict(copyfile=False, ),
        subject_info=dict(
            mandatory=True,
            xor=['subject_info', 'event_files'],
        ),
        time_repetition=dict(mandatory=True, ),
    )
    inputs = SpecifySPMModel.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SpecifySPMModel_outputs():
    output_map = dict(session_info=dict(), )
    outputs = SpecifySPMModel.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
