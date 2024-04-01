# chicken-disease-classification

## Project Overview
Chicken farming is a vital aspect of the agricultural industry, providing a significant portion of the world's meat consumption. However, poultry health is often threatened by various diseases, including coccidiosis, a common and economically significant parasitic disease caused by protozoa of the genus Eimeria. Timely and accurate diagnosis of such diseases is crucial for effective treatment and prevention strategies.

In this project, we aim to develop a classification system to distinguish between healthy chickens and those infected with coccidiosis using image analysis of fecal samples. By leveraging machine learning techniques, we intend to create a reliable tool that can assist poultry farmers and veterinarians in early disease detection and management.

## Dataset
The dataset is downloaded from Kaggle: [chicken-diseases-only-cocci-and-healthy](https://www.kaggle.com/datasets/akashrai1701/chicken-diseases-only-cocci-and-healthy). These images are categorized into two classes: healthy and infected with coccidiosis.

## Pipeline
1. Data Ingestion
2. Base Model Preparation (VGG16)
3. Model Training
4. Model Evaluation

## Methodology
To begin, a comprehensive MLOps folder structure template was established, encompassing key components such as setup procedures, and a requirements.txt file. Subsequently, a Conda environment was configured, and all necessary dependencies were installed. Following this, a custom logging system was implemented, and frequently utilized functions were incorporated into utils/common.py.
For each pipeline component, the workflow proceeded as follows:
* Configuration details were integrated into the config.yaml file.
* Custom entities were created to represent specific components within the pipeline.
* Configuration settings for each entity were added to ensure consistency.
* Pipeline components were developed to execute the specific task.
* The overall pipeline structure was constructed.
* main.py was updated to incorporate the newly developed pipeline components.

Lastly, the dvc.yaml file was revised to eliminate redundant execution of pipeline components, thereby optimizing the project's efficiency.

## How to run?
1. Clone the repository
   
``` git clone https://github.com/saraimdad/chicken-disease-classification.git ```

2. Create a conda environment after opening the repository

``` conda create -n cnncls python=3.11 -y ```

``` conda activate cnncls ```

3. Install the requirements

``` pip install -r requirements.txt ```

4. Run the following and open localhost

``` python app.py ```
