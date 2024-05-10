FROM python:3.8-slim

# Устанавливаем Poetry
#RUN pip install poetry

# Копируем файлы poetry (pyproject.toml и poetry.lock) в контейнер
#COPY pyproject.toml poetry.lock ./
COPY requirements.txt .

# Устанавливаем зависимости с помощью Poetry
RUN pip3 install -r requirements.txt
#RUN apt-get update && apt-get install -y build-essential && apt-get install -y libjpeg-dev libpng-dev
#RUN pip3 install torch==2.3.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install torch==2.1.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install torchvision==0.16.2 -f https://download.pytorch.org/whl/torch_stable.html
#RUN poetry install --no-dev  # Устанавливаем только зависимости для запуска (без dev-зависимостей)
#RUN pip3 install torch --user

# Копируем все остальные файлы вашего проекта в контейнер
COPY /inference/ ./
ADD /models/clip ./clip/
ADD /sneakers/data/labelled_sample.csv ./
ADD /sneakers/data/golden_dataset ./golden_dataset/

EXPOSE 8000

# Устанавливаем команду по умолчанию (запуск FastAPI, Uvicorn, или другую)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]