# ```Learning to see in the dark with Fastai```
This was a project by me and my teammates where we decided to use Fastai and implemented the paper learning to see in the dark. Rather using the `RAW` image format we converted it to `jpg`because of two things: 
- We didnt had much computing power (only Google Colab)
- And we didn't have the storage to store the dataset. 

The model we built with `jpg` didn't produce the paper's actual results, but we are still working on fixing the pixel issues related to the predicted image. Special thanks to the authors of the paper, team of fastai and Zach Mueller for walk with fastai. 

## ```Run```
To run this app on a local streamlit app:

	 pip install -r requirements.txt
     streamlit run init.py

We've deployed the app on streamlit which is trained on learning to see in dark paper with resnet 34 as architecture.

     Currently this project is under development will take quite more time to get it to bring us good results 

## ```Code``` 
The code for replicating this experiment can be found in [`notebooks`](https://github.com/KliKli2/litd/tree/main/notebooks) folder 

## ```Dataset used``` 
[Sony camera raw dataset](https://storage.googleapis.com/isl-datasets/SID/Sony.zip)
this dataset is converted to `jpg` images and then trained with the backbone of `resnet34` architecture 

## ```Original paper link```
 [arXiv:1805.01934](https://arxiv.org/abs/1805.01934) `[cs.CV]`

### ```Team Mates```
- [Som](https://www.linkedin.com/in/somesh-9188/)
- [Tanvi](https://www.linkedin.com/in/tanvi-punjani-49493490/)
- [Max](https://www.linkedin.com/in/maximilian-von-hohenb%C3%BChel-40057119b/)
- [Myself](https://www.linkedin.com/in/ashik-shaffi-7b3917171/)
