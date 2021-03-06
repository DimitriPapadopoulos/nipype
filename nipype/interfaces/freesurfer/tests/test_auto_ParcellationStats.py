# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..utils import ParcellationStats


def test_ParcellationStats_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    aseg=dict(mandatory=True,
    ),
    brainmask=dict(mandatory=True,
    ),
    copy_inputs=dict(mandatory=False,
    ),
    cortex_label=dict(),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    hemisphere=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_annotation=dict(argstr='-a %s',
    mandatory=False,
    xor=['in_label'],
    ),
    in_cortex=dict(argstr='-cortex %s',
    mandatory=False,
    ),
    in_label=dict(argstr='-l %s',
    mandatory=False,
    xor=['in_annotatoin', 'out_color'],
    ),
    lh_pial=dict(mandatory=True,
    ),
    lh_white=dict(mandatory=True,
    ),
    mgz=dict(argstr='-mgz',
    mandatory=False,
    ),
    out_color=dict(argstr='-c %s',
    genfile=True,
    mandatory=False,
    xor=['in_label'],
    ),
    out_table=dict(argstr='-f %s',
    genfile=True,
    mandatory=False,
    requires=['tabular_output'],
    ),
    rh_pial=dict(mandatory=True,
    ),
    rh_white=dict(mandatory=True,
    ),
    ribbon=dict(mandatory=True,
    ),
    subject_id=dict(argstr='%s',
    mandatory=True,
    position=-3,
    usedefault=True,
    ),
    subjects_dir=dict(),
    surface=dict(argstr='%s',
    mandatory=False,
    position=-1,
    ),
    tabular_output=dict(argstr='-b',
    mandatory=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    th3=dict(argstr='-th3',
    requires=['cortex_label'],
    ),
    thickness=dict(mandatory=True,
    ),
    transform=dict(mandatory=True,
    ),
    wm=dict(mandatory=True,
    ),
    )
    inputs = ParcellationStats.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_ParcellationStats_outputs():
    output_map = dict(out_color=dict(),
    out_table=dict(),
    )
    outputs = ParcellationStats.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
