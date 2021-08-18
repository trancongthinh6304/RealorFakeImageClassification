# RealorFakeImageClassification
 Project name: Real or Fake Image Classification
## Members:
* Trần Công Thịnh
* Vũ Thị Quỳnh Nga

### 1. Introduction
#### Target:
* Classify real images and images created by AI
* Real life application: in playing games, in movie theaters,...😎

#### Link preferences
* [Link weight (.hdf5)](https://drive.google.com/drive/folders/1BHIh8p08TQvfreLLZnWOaA_RL8nWNTVa?usp=sharing) 
* [Link dataset](https://drive.google.com/drive/folders/1zE4g0rGf27Sjzz3-RTwQ4K4O0khzglxe?usp=sharing)
* [Link Presentation](https://docs.google.com/presentation/d/12o2xQ4W0sg7fAQ4GHayeycuZOKQu6MArjVX_nGfaGbA/edit?usp=sharing)
* [Link papet](https://hackmd.io/@vuthiquynhnga/Hy7WrEZwu)

### Result
![image](https://user-images.githubusercontent.com/62460040/118517986-eb295f80-b761-11eb-9ed1-df489d1833c2.png)

### 2. Gradio app tutorial

1. Access link weight, add weight file to your drive
2. Run the following lines of code:
```
from keras.models import load_model

weights_path = '/content/drive/MyDrive/Models/ResNet152-21-0.0109.hdf5' #đường dẫn đến file weight

#Nhớ khởi tạo model trước
model = Resnet_based_model
#Load weight
model.load_weights(weights_path)
```
3. Use gradio
After the code run, this interface will emerge
![2021-05-17 (2)](https://user-images.githubusercontent.com/42512473/118430885-54c45200-b6ff-11eb-9578-0fc16a68b8ec.png)
* Drag image into the frame
* Hit submit
* Wait for the result in the right section 👍
