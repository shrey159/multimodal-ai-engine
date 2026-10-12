import os
import numpy as np
import onnxruntime as ort
from typing import Dict, Any

class ONNXInferenceEngine:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.session = None
        
        if os.path.exists(self.model_path):
            session_options = ort.SessionOptions()
            session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
            self.session = ort.InferenceSession(self.model_path, session_options, providers=['CPUExecutionProvider'])
            self.input_name = self.session.get_inputs()[0].name
            self.output_name = self.session.get_outputs()[0].name

    def predict(self, input_data: np.ndarray) -> Dict[str, Any]:
        if self.session is None:
            # Fallback mock engine if no ONNX model file is present yet
            return {
                "predictions": [[0.95, 0.05]],
                "shape": [1, 2],
                "status": "mock_execution"
            }
        
        if input_data.dtype != np.float32:
            input_data = input_data.astype(np.float32)

        outputs = self.session.run([self.output_name], {self.input_name: input_data})
        predictions = outputs[0]
        
        return {
            "predictions": predictions.tolist(),
            "shape": predictions.shape,
            "status": "onnx_execution"
        }