# RealorFakeImageClassification:
 Tên dự án: Real or Fake Image Classification
## Thành viên:
* Trần Công Thịnh
* Vũ Thị Quỳnh Nga

### 1. Introduction:
#### Mục đích:
* Phân biệt hình người thật và hình do AI tạo ra
* Ứng dụng: trong chơi game, rạp chiếu phim,...😎

#### Link các thành phần liên quan
* [Link weight (.hdf5)](https://drive.google.com/drive/folders/1BHIh8p08TQvfreLLZnWOaA_RL8nWNTVa?usp=sharing) 
* [Link dataset](https://drive.google.com/drive/folders/1zE4g0rGf27Sjzz3-RTwQ4K4O0khzglxe?usp=sharing)
* [Link Presentation](https://docs.google.com/presentation/d/12o2xQ4W0sg7fAQ4GHayeycuZOKQu6MArjVX_nGfaGbA/edit?usp=sharing)
* [Link file Báo Cáo](https://hackmd.io/@vuthiquynhnga/Hy7WrEZwu)

### 2. Hướng dẫn dùng app gradio ứng dụng

1. Vào link weight, thêm file weight vào drive của mình
2. Chạy đoạn code sau:
```
from keras.models import load_model

weights_path = '/content/drive/MyDrive/Models/ResNet152-21-0.0109.hdf5' #đường dẫn đến file weight

#Nhớ khởi tạo model trước
model = Resnet_based_model
#Load weight
model.load_weights(weights_path)
```
3. Sử dụng Gradio
Sau khi code chạy thì sẽ có giao diện như sau
![2021-05-17 (2)](https://user-images.githubusercontent.com/42512473/118430885-54c45200-b6ff-11eb-9578-0fc16a68b8ec.png)
* Kéo hình bỏ vào khung
* Bấm submit
* Chờ ra kết quả ở bên tay phải 👍
