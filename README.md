
# League of legends champion classifier

League of leguends is one of the most popular MOBA games currently. It consist on 5vs5 online battles in which objective is to destroy the nexus. Currently, it counts with 157 champions. In this project only 5 of them (my favorite ones) were chosed. I discovered league of legends (lol) in first year of college, I was going through at that moment and this game helped me a lot. This little project is attribute to this amazing game. 😃

<p>
<img src="images/lol_gif_part_1_Trim.gif" width="45%"/>
  &nbsp; &nbsp; &nbsp; &nbsp;
<img src="images/lol_gif_part_1_Trim-_2_.gif" width="45%"/>
</p>



### Currently this   project is deployed in AWS EC2. and It can be accesed in this [ **link** ](http://ec2-18-191-142-227.us-east-2.compute.amazonaws.com/) :link:. 

The model classifies images (original base picture. skins and fanart) of 5 champions: Aatrox, Ahri, akali, Anivia and Cassipeia. It´s easy to use, just drop an image in the dropzone and press classify.  

---
## About the project 
This project has 4 main: **data collection**, **model**, **backend** and **frontend**

### [Data collection](https://github.com/jglobaton10/LeagueOfLegendsChampionClassifier/blob/main/model/model.ipynb) 🔗

The dataset was built using **simple_image_download**. It was used to downlaod 25 images per champion, which were divided in train 80% and test 20%. The code to buil the dataset is potrayed next. 

```python

n_images = 25
response = simp.simple_image_download

base_path = 'simple_images/'
os.mkdir('test1')
for champion in champions.name:
    response().download(champion + ' lol', 23)
   
    ## Creates a folder for each champion to save the testing images 
    os.mkdir('test1/'+champion+'_lol')
    
    for element in os.listdir(base_path+ champion + '_lol')[-5:-1]:
        shutil.move(base_path+ champion + '_lol/'+element, 'test1/'+champion+'_lol/'+element)
```





### [Model](https://github.com/jglobaton10/LeagueOfLegendsChampionClassifier/blob/main/model/model.ipynb) 🔗

It was built a **convolutional neural network**  model using tensorflow and keras. Parameter tuning was performed on the number of neurons and layers and It achieved a **precison 0.75**. 

### [Backend](https://github.com/jglobaton10/LeagueOfLegendsChampionClassifier/blob/main/Flaskserver/server.py) 🔗

The backend was built using flask and it is composed of two parts. First, a helper module that loades the wieghts in the model and make predictions taking a base64 image decoding it and applying the predict function from the model. Second, the flask server which receives the return requests. 

### [Frontend](https://github.com/jglobaton10/LeagueOfLegendsChampionClassifier/tree/main/Front_end) 🔗
It is basic html a .js app  that takes an image encode it in base64 and sends and receives requests. This part of the app was deployed in a **nginx server** inside the EC2 instance. 
