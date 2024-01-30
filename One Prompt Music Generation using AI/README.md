# MusicGen Using AI

## Overview:
This simple project utilizes the Hugging Face model, specifically the 'facebook/musicgen-small model', to generate music based on user input. The project takes advantage of the 'Hugging Face Inference API' and requires an API key for authorization.

## Tools and Technologies:

* **[Python](https://www.python.org/):** Utilized for data analysis, visualization, and modeling.

* **[Requests Library](https://docs.python-requests.org/en/master/):** Used for making HTTP requests to the Hugging Face Inference API.

* **[Pydub Library](https://pydub.com/):**Utilized for processing audio files, specifically for converting the received content into an AudioSegment object.

* **[Hugging Face Model](https://huggingface.co/facebook/musicgen-small):** The pre-trained model hosted on Hugging Face's model hub, providing music generation capabilities.

* **[IO Module (BytesIO)](https://docs.python.org/3/library/io.html#io.BytesIO):**  Used to handle the byte stream of the content received from the API response.

## Requirements:

**1. Python Installation:** 
Ensure that Python is installed on your machine. You can download and install Python from the official Python website.

**2. Required Packages:**
 Make sure you have the necessary Python packages installed. You can use the following command in your terminal or command prompt to install them:

  ```
    pip install requests pydub 
  ```

##  Usage

1. Obtain an API key from Hugging Face.

2. Replace the placeholder in the API_key variable with your API key.

```
    API_key = "Bearer YOUR_API_KEY_HERE"

```

3. Run the script and enter the type of music you want to listen to when prompted.

## Tips:

**1. Environment Considerations:** If you're using virtual environments, make sure to activate your environment before running the code.

**2. Check Dependencies:** Double-check that all dependencies and required libraries are installed and up-to-date.