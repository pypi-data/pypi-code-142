from pipeline import (
    PipelineFile,
    pipeline_function,
    pipeline_model,
)
import onnxruntime


@pipeline_model
class OnnxModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = onnxruntime.InferenceSession(
                model_file.path,
                providers=["CUDAExecutionProvider", "CPUExecutionProvider"],
            )
            self.output_names = [output.name for output in self.model.get_outputs()]
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, onnx_input: dict) -> list:
        res = self.model.run(self.output_names, onnx_input)
        return res[0].tolist()
