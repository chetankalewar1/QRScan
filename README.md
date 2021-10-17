1. Open the project folder and activate the venv using `source venv/bin/activate`.
2. Install the project requirements `pip install -r requirements.txt`.
3. To generate qr image for a record use function `get_qr_for_each_record` and pass in the filename.\
4. Use `python manage.py runserver` to start the django server.
5. You can now visit the links generated from qr and the data of client who opens the link and clicks on accept button will be saved in static/TestScane.xlsx .
