# Three datasets for unit 3.5.2 data collection

These datasets were too large to fit into 1GB of GitHub's Large File Storage (LFS) system, so I am including links to the data here. All these datasets were downloaded from sites as zip files, so I didn't use any APIs. As I'm trying to focus on a model-focused project, I don't want to spend too much time managing my data.

### ImageNet object localization

Link: https://www.kaggle.com/c/imagenet-object-localization-challenge/data?select=imagenet_object_localization_patched2019.tar.gz
This dataset comes from a Kaggle challenge for identifying objects in images. It contains about 1.2 million labelled images, each falling into one of 1000 classes. This would suit a capstone project that does simple object classification, although an advanced model would be needed to accurately classify into 1000 different classes.

### Caption generation
Link: https://www.kaggle.com/hsankesara/flickr-image-dataset
This dataset comes from a Kaggle challenge for adding a caption to an image that describes what is happening in the image. It contains approximately 31,000 images, labelled with a caption. This would suit a capstone project that extends an object classification algorithm, as a captioning algorithm would need to recognize multiple objects in a picture and describe the relationships between these objects. For example, it might recognize a man, a truck, and a tree, and need to recognize that the man is driving his truck past a tree.

### Recognizing intracranial hemorrhage
Link: https://www.kaggle.com/c/rsna-intracranial-hemorrhage-detection/overview
This dataset comes from a Kaggle competition for recognizing hemorrhaging in the brain from medical scans, and was built off of a research paper of the same topic. As a simple "yes/no" classification is required, it's best to have a large convolutional neural network or some combination with other ML methods to extract the best features from this dataset. The best algorithm would be one that categorizes with better accuracy than a human expert.
