from ultralytics import YOLO


class ObjectDetector:
    def __init__(self, model_path="yolo11n.pt"):
        self.model = YOLO(model_path)

    def detect(self, image):
        results = self.model(image)
        return results

    def detect_and_save(self, image, output_path):
        results = self.model(image)

        annotated = results[0].plot()

        import cv2
        cv2.imwrite(output_path, annotated)

        return annotated
     