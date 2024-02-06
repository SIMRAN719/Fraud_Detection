# Password Generator

## Description
This Python script generates strong and random passwords of variable length based on user input. It utilizes the random module to create passwords containing a mix of lowercase letters, uppercase letters, digits, and special characters.


**1. Default Password Generation:** Generates a random password with a mix of uppercase letters, lowercase letters, digits, and special characters.

**2. Customized Password Generation:** Allows users to specify the length of the password and the number of uppercase letters, lowercase letters, digits, and special characters.


## Features

* Generates passwords with customizable length and character composition.

* Includes lowercase letters, uppercase letters, digits, and special characters in the generated passwords.

* Provides flexibility in choosing the number of each character type in the password.

* Simple command-line interface for ease of use.


## Prerequisites:

**1. Python Installation:** Ensure that Python is installed on your machine. You can download and install Python from the official Python website.

## Installation

1. Clone this repository to your local machine

```
    git clone https://github.com/SIMRAN719/Mini-Projects.git
```

2. Navigate to the project directory

```
    cd password-generator
```

3. Run the script

```
    python Password Generator.py
```

## Usage

* Upon running the script, you will be prompted to choose between default and customized password generation.

* For customized password generation, you will be asked to specify the desired length of the password and the number of uppercase letters, lowercase letters, digits, and special characters.

* After providing the necessary input, the script will generate and display the password accordingly.


## Sample

```
$ python password_generator.py
1. Default
2. Customize
Enter your choice: 1
Generated Password: n^5F7U&dR1@l

$ python password_generator.py
1. Default
2. Customize
Enter your choice: 2
Enter the total length of the password: 12
Enter the number of numbers you want in your password: 2
Enter the number of special characters you want in your password: 2
Enter the number of capital letters you want in your password: 3
Generated Password: R1%2H#9kL@o6
```