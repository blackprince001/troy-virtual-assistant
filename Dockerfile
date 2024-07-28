FROM python:3.9

WORKDIR /app

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

COPY requirements.txt /requirements.txt

RUN /root/.cargo/bin/uv pip install --system --no-cache -r /requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

