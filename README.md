# swen549-foodmap


__Made by:__ Calvin Wu, Edward Wong, Kevin Bastian, Nikolas Tilley


__About__

Cloud Application that maps the occurrences of Food and Events on RIT Campus. Deployed using Google App Engine.


__Configuration__

Before running or deploying this application, install the dependencies using pip:

	pip install -t lib -r requirements.txt
	
	
__Deployment__

1. Download and install Google App Engine Python SDK for your system.
2. Install extra libraries using dependencies listed in _requierments.txt_:

		pip install -t lib -r requirements.txt

3. Use _gcloud_ to deploy using your Project ID and a version number:
		
		 gcloud app deploy --project your-app-id -v your-version
		 
4. View the application at _https://your-app-id.appost.com_