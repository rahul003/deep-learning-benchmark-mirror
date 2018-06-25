import os

def getImagenetData(dataset):
    if not os.path.exists(os.path.expanduser('~/data/')):
        os.system('mkdir -p ~/data')
        os.system("aws s3 sync s3://aws-ml-platform-datasets/imagenet/pass-through/train-passthrough.rec ~/data/")