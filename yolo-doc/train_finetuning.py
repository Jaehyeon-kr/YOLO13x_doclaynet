import typer
from ultralytics import YOLO
import numpy as np 

def main(
    base_model: str,
    datasets: str = "./datasets/data.yaml",
    epochs: int = 200,
    imgsz: int = 1024,
    batch: int = 1,
    seed: int = 42,
    mosaic: float=0.4,
    copy_paste: float=0.4,
    hsv_v: float = 0.4,                  # 명도 약간

):
    try:
        from clearml import Task

        Task.init(
            project_name="yolo13x",
            task_name=f"{base_model}-epochs-{epochs}-imgsz-{imgsz}-batch-{batch}",
        )
    except ImportError:
        print("clearml not installed")

    model = YOLO(base_model)
    model.train(
        data=datasets, epochs=epochs, imgsz=imgsz, batch=batch, seed=seed, patience=20, copy_paste=copy_paste, mosaic=mosaic,hsv_v=hsv_v,
    save_period=1 ,lr0=0.001 # 모든 에폭마다 weight 저장,
    )


if __name__ == "__main__":
    typer.run(main)
