# Basic instructions
## To run the app:
* in the root folder of the project run:
   ```
    docker build -t flask-library-app .
    docker run -p 5000:5000 flask-library-app
    ```

OR
* in the root folder of the project run:
   ```
    rm -rf venv
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements --no-cache
    python run.py
    ```
   
## run tests (I haven't completed the tests)
python -m unittest discover -s tests

## Notes and Assumptions in the project
1. I have used in memory simple non-persistent dictionary for simplicity.
2. The filter by author is O(n) since I haven't implemented indexing.
3. I didn't validate date format.
4. The tests were not completed
5. I didn't finish th documentation. 
   I have added documentation in book_controller.add_book as an example.
6. I am not familiar with python specific practices and structures so the code may not meet the conventions.

## Utilities
I have made a file under /utilities dir, with curl commands to test the app.
(simple replacement to Postman)