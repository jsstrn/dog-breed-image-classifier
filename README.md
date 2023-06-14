# dog-breed-image-classifier

- Project: Use a Pre-trained Image Classifier to Identify Dog Breeds
- Nanodegree
  program: [AI Programming with Python](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089)
- Course provider: Udacity

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

### Install Ananconda

First, install [Anaconda](https://www.anaconda.com/download/). This should also install the latest version of Python 3
for you.

Check the version on Anaconda:

```shell
conda --version
```

Update Anaconda and its dependencies:

```shell
conda update conda
```

### Create virtual environment

Create a new virtual environment:

```shell
conda create --name my-new-env
```

Activate your new environment:

```shell
conda activate my-new-env
```

Check which environment you are currently on. The current environment is indicated by an asterisk `*`:

```shell
conda info --env
base          /some/dir/to/your/env
my-new-env *  /some/dir/to/your/env
```

### Install dependencies

Now install the following packages:

```shell
conda install pillow
conda install torchvision
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
