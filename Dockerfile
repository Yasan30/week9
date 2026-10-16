2.FROM python:3.10-slim
3.WORKDIR /app
4.COPY requirements.txt .
5.RUN pip install --no-cache-dir -r requirements.txt
6.COPY . .
7.EXPOSE 5000
CMD ["python", "app.py"] 