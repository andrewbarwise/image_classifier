# image_classifier

Using Streamlit and Pytorch I have developed a simple web app that classifies jpg images using the pretrained resnet101 neural network.

To clone the app to your local machine follow these steps:
    
    > git clone https://github.com/andrewbarwise/image_classifier.git
    > cd image_classifier
    > py -3 -m venv .venv
    > .venv\scripts\activate
    > python -m pip install -r requirements.txt

To deploy the app via Streamlit follow this step:

    > streamlit run app.py

To deploy the app using Docker follow these steps:
    
    > docker build -t streamlit .
    > docker run -p 8501:8501 streamlit

