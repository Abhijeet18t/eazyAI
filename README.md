# eazyAI
The internship project under the supervisory of Robotics and AI Engineering Program, Faculty of Engineering, King Mongkut's Institute of Technology Ladkrabang

# Brief

Topic: Object Detection
Task: Object detection through webapp

The task assigned for this intership involves creation of a webapp which can allow users to select the
pretrained object detection model. The users then will have the option to upload the image and get
the bounding box as on the image as the result.(It will be extended for video too if time permits)

We have provided you with the train and detect notebook file already. The task is now seperated in these
subgroups:
FRONT END (use React js)
- create a form to upload trained .pt file and give a name to it.
- homepage should have an option to select from the trained models that were uploaded
- user should then have a space to upload an image and click detect button.
- the resultant image after detection should be shown.
- use your creativity to make the page look beautiful :)

BACK END(use Django REST Framework)
- create an API to store the trained .pt file in filesystem and save the name and file path in database.
- create an API to accept the input image and selected model and pass it to detect function and return
the response to the FE.

Python
- The task here is to create the detect function which will be called from Django Backend
- the function should take the model and image as the parameter and return the result.
- Basically it should do the same task as detect.py command in the notebook file that you went through.

Note: Please use virtual environment for installation of required packages for object detectiona and django.

# Duration
Mar 18 - Apr 20, 2021

# Author
1. Rushikesh Patil 
2. Kartiki Borage 
3. Abhijeet Takale 
4. Vrushali Chaudhari 
5. Palak Jha 

# Advisor
1. Dr. Poom Konghuayrob
2. Niraj Pahari
3. Sarucha Yanyong

# Organization
Robotics and AI Engineering Program, Faculty of Engineering, King Mongkut's Institute of Technology Ladkrabang
