FROM python:3.9-slim

# Instala libGL e demais libs requeridas pelo OpenCV
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      libgl1-mesa-glx \
      libglib2.0-0 \
      libsm6 \
      libxrender1 \
      libxext6 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "app.py"]
