# Chair Haar Detector

使用 OpenCV Haar Cascade 進行椅子即時偵測的專題。

## 專題內容

本專題使用正樣本與負樣本訓練 Haar Cascade 分類器，並透過攝影機進行即時椅子偵測。

## 檔案說明

* `detect_camera.py`：開啟攝影機並即時偵測椅子。
* `label_tool.py`：建立正樣本標註資料。
* `create_negative_list.py`：建立負樣本清單。
* `cascade_output/cascade.xml`：訓練完成的 Haar Cascade 分類器。
* `annotations/positives.txt`：正樣本標註資料。
* `annotations/negatives.txt`：負樣本清單。
* `training_data/positives.vec`：正樣本訓練向量檔。

## 執行方式

先安裝需要的套件：

```bash
pip install opencv-python
```

接著執行：

```bash
python detect_camera.py
```

程式會開啟攝影機，並使用訓練完成的 Haar Cascade 模型偵測畫面中的椅子。

## 專題成果

成功訓練出椅子 Haar Cascade 分類器，並能透過攝影機進行即時偵測。
# chair-hair-detector
Haar Cascade chair detection project using OpenCV.
