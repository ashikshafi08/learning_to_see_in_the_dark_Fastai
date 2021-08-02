# ```Introduction```
Converting night time images to day time images.

# ```Run```
To run this app on a local streamlit app:

	 pip install -r requirements.txt
     streamlit run init.py

We've deployed the app on streamlit which is trained on learning to see in dark paper with resnet 34 as architecture.

     Currently this project is under development will take quite more time to get it to bring us good results 

# ```code``` 
The code for replicating this experiment can be found in [`notebooks`](https://github.com/KliKli2/litd/tree/main/notebooks) folder 

# ```Dataset used``` 
[Sony camera raw dataset](https://storage.googleapis.com/isl-datasets/SID/Sony.zip)
this dataset is converted to `jpg` images and then trained with the backbone of `resnet34` architecture 

```Original paper link```
## [arXiv:1805.01934](https://arxiv.org/abs/1805.01934) `[cs.CV]`

Special thanks to the authors of the paper. 
