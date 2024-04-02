# FullStack Real Estate Predictive Analytics 
Real Estate Predictive Analytics aims to develop a Predictive Analytics tool to predict Real Estate housing prices in Bengaluru. This tool utilizes techniques like Data cleaning, Feature Engineering, EDA and Regression Model development to predict prices against user inputs. Further the tool leverages FastAPI for Backend Infrastructure and serving ML Model as an API. Also, Streamlit was utilized to develop basic frontend for our application.  

## Application Structure
The project has been divided into 3 major phases: 
- Data Analytics & Machine Learning: Bengaluru hosuing prices dataset is utilized for the application. This phase involves Data cleaning, Data transformations, Feature Engineering & Exploratory Data Analysis. Furthermore Linear Regression model is built to predict Real Estate prices. 
- Backend Infrastructure: FastAPI is leveraged for Server side setup and the logic for using the model as an API in the frontend application is implemented here. Utility functions are created and then FastAPI is utilized to serve routes to those functions.
- Frontend: Streamlit is utilized to develop a simple user friendly and interative web interface for the users to interact with the application

## Usage
To run the application, you will need to run the FastAPI server using uvicorn and then in a seperate terminal run the Streamlit application. Furthermore you can enter the details in the frontend application and predict Real Estate prices of your preferred location.

