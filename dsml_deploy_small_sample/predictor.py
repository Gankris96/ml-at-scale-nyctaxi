import onnxruntime
import numpy as np
import json
import traceback

model = "green_model_small_new.onnx"


class PythonPredictor:
    def __init__(self, config):
        self.session = onnxruntime.InferenceSession(model, None)
        self.input_name = self.session.get_inputs()
        self.output_name = self.session.get_outputs()[0].name

    def predict(self, payload):
        try:
            d = {}
            print("MYLOG = ", "reached here")
            input_data = payload["features"]
            list_typles = []
            for k in input_data:
                x = np.array([input_data[k]], dtype=np.float32).reshape((1, 1))
                list_typles.append((k, x))
                d[k] = x
            # np.array([1]).reshape((1, 1))
            # return input_data["Abs_Distance"]
            # d = {"Abs_Distance": np.asarray([1.])}
            # results = "HELLO"

            results = str(self.session.run([self.output_name], d)[0][0][0])
        except Exception as e:
            var = traceback.format_exc()
            results = "something_went_wrong.. " + var
        finally:
            return {
                "estimated_duration": results
            }


if __name__ == '__main__':
    print("Running ")
    predServer = PythonPredictor()
    d = {"Abs_Distance": np.asarray([1.])}
    predServer.predict(d)
