from elyra.pipeline.processor import RuntimePipelineProcessor
from elyra.pipeline.runtime_type import RuntimeProcessorType


class UnicorePipelineProcessor(RuntimePipelineProcessor):
    _type = RuntimeProcessorType.UNICORE_PIPELINES
    _name = "unicore"
