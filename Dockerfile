FROM python:3.11-slim

# Install necessary system dependencies
RUN apt-get update 

# Set working directory
WORKDIR /app

# Download the model
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install diffusers transformers

COPY download_model.py .
RUN python download_model.py

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy requirements and install them


# Copy the application files
COPY . .


# Expose the port for Flask
ENV PORT 8080
EXPOSE $PORT

# Run the app
CMD ["python", "app.py"]
