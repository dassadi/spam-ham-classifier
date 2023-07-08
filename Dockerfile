# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/dassadi/spam-ham-classifier.git .

# Download the NLTK resource
RUN python -m nltk.downloader punkt


# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Streamlit app will run
EXPOSE 8501

# Set the entry point to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
