# image_classifier

Using Streamlit and Pytorch I have developed a simple web app that classifies jpg images using the pretrained resnet101 neural network.



To deploy the app using Docker follow these steps in the CLI:
    
    docker build -t streamlit .

    docker run -p 8501:8501 streamlit

