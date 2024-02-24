# AI Image Generation with Hugging Face Model

## Overview:
This project employs the Hugging Face model, specifically the 'stable-diffusion-xl-base-1.0' model, to generate images based on user prompts. The script utilizes the Hugging Face Inference API, requiring an API key for authentication.

## Tools and Technologies:

* **[Python](https://www.python.org/):** Utilized for scripting and interacting with APIs.

* **[Requests Library](https://docs.python-requests.org/en/master/):** Used for sending HTTP requests to the Hugging Face Inference API.

* **[Pillow (PIL)](https://pillow.readthedocs.io/en/stable/):** Employed for processing and displaying images.

* **[Random Module](https://docs.python.org/3/library/random.html):** Used for generating random numbers to enhance diversity in image generation.

## Requirements:

**1. Python Installation:** 
Ensure that Python is installed on your machine. You can download and install Python from the official Python website.

**2. Required Packages:**
Make sure you have the necessary Python packages installed. You can use the following command in your terminal or command prompt to install them:

```
    pip install requests, pillow
```
## Usage

1.  Obtain an API key from Hugging Face.

2. Replace the placeholder in the `API_Key` variable with your API key.

## Installation

1. Clone this repository to your local machine

```
    git clone https://github.com/SIMRAN719/Mini-Projects.git
```

2. Navigate to the project directory

3. Run the script

## Tips:

1. Environment Considerations: If you're using virtual environments, ensure to activate your environment before running the code.

2. Check Dependencies: Double-check that all dependencies and required libraries are installed and up-to-date.

## Note:

1. Ensure that your prompt is appropriate for generating meaningful images.

2. The generated image will be displayed and saved as pic.png in the directory where the script is executed.