import os
import nipype.interfaces.base as nib
from tempfile import mkdtemp
from shutil import rmtree

from nipype.testing import assert_equal
import nipype.pipeline.engine as pe


class InputSpec(nib.TraitedSpec):
    input1 = nib.traits.Int(desc='a random int')
    input2 = nib.traits.Int(desc='a random int')


class OutputSpec(nib.TraitedSpec):
    output1 = nib.traits.List(nib.traits.Int, desc='outputs')


class TestInterface(nib.BaseInterface):
    input_spec = InputSpec
    output_spec = OutputSpec

    def _run_interface(self, runtime):
        runtime.returncode = 0
        return runtime

    def _list_outputs(self):
        outputs = self._outputs().get()
        outputs['output1'] = [1, self.inputs.input1]
        return outputs


def test_run_multiproc():
    cur_dir = os.getcwd()
    temp_dir = mkdtemp(prefix='test_engine_')
    os.chdir(temp_dir)

    pipe = pe.Workflow(name='pipe')
    mod1 = pe.Node(interface=TestInterface(), name='mod1')
    mod2 = pe.MapNode(interface=TestInterface(),
                      iterfield=['input1'],
                      name='mod2')
    pipe.connect([(mod1, mod2, [('output1', 'input1')])])
    pipe.base_dir = os.getcwd()
    mod1.inputs.input1 = 1
    pipe.config['execution']['poll_sleep_duration'] = 2
    execgraph = pipe.run(plugin="MultiProc")
    names = ['.'.join((node._hierarchy, node.name)) for node in execgraph.nodes()]
    node = execgraph.nodes()[names.index('pipe.mod1')]
    result = node.get_output('output1')
    yield assert_equal, result, [1, 1]
    os.chdir(cur_dir)
    rmtree(temp_dir)
