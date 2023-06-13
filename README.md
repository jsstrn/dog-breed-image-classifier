# dog-breed-image-classifier

- Project: Use a Pre-trained Image Classifier to Identify Dog Breeds
- Nanodegree
  program: [AI Programming with Python](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089)
- Course provider: Udacity

## Requirements

First, install [Anaconda](https://www.anaconda.com/download/). Then install the following packages:

```shell
conda install pillow
conda install torchvision
```

## Getting started

Clone this repository with the tag `project-starter-files` to get the project starter files without any of the
solutions.

Using SSH

```shell
git clone --depth 1 --branch project-starter-files git@github.com:jsstrn/dog-breed-image-classifier.git 
```

Using HTTPS

```shell
git clone --depth 1 --branch project-starter-files https://github.com/jsstrn/dog-breed-image-classifier.git
```

## Run the program

To run the program:

```shell
python check_images.py
```

To run image classifier with all three models

```shell
sh run_models_batch.sh
```

To run image classifer against images in the `uploaded_images` directory:

```shell
sh run_models_batch_uploaded.sh
```

## Project feedback

> “Programs are meant to be read by humans and only incidentally for computers to execute.”
>
> -- Donald Knuth, The Art of Computer Programming.

![img.png](img.png)