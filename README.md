

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
 
  <h3 align="center">Employee Turnover Estimation AI</h3>
 
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
Deployment of a logistical regression model that was trained on structured data. <br /> 
Such data contains a couple of values that relate to the work experience of the employee 
and the model predicts the estimation of them staying in the company in the first year of employment.  <br />
The deployment consists of a full stack application: 
1) Flask api written in Python, recieves value inputs from the frontend, runs the model and responds back to the frontend.
2) React.js frontend that contains a form page for the user to fill the input values and display the model's result.
<br />
Model was written and trained by Dor Getter github.com/DorGetter
<br />
<br />

![Untitled](https://user-images.githubusercontent.com/44925899/212956574-faff2711-82e5-4a90-9881-da69971c38e6.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Flask][Flask]][Flask-url]
* [![React][React.js]][React-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started 

### Installation


1. Clone the repo.
   ```
   git clone https://github.com/alexchagan/employee-churn-ai-app.git
   ```
2. Build docker-compose with file in the root directory.
   ```
   docker compose build
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Run docker-compose:
  ```
   docker compose up
  ```
2. Fill the input values in the form page and press submit.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Alex Chagan  - alexchagan95@gmail.com

Project Link: [https://github.com/alexchagan/sports-images-classifier](https://github.com/alexchagan/sports-images-classifier)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alex-chagan-a243221b6/
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Flask]: https://img.shields.io/badge/-Flask-black
[React-url]: https://reactjs.org/
[React.js]: https://img.shields.io/badge/-React.js-blue


