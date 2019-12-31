# labeling images through slack

python version : 3.7.4  

./ngrok authtoken  
./ngrok http 80  

pip install -r requirements.txt  
python manage.py makemigrations classifier  
python manage.py migrate  
python manage.py loaddata images.json  
python manage.py runserver 80  ( *sudo if needed ) 
