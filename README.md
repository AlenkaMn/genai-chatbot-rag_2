

# genai-chatbot-rag
 ```markdown


## Overview
This project provides a comprehensive solution for building a chatbot using Retrieval-Augmented Generation (RAG) techniques. It leverages powerful language models to retrieve relevant information and generate human-like responses, designed to enhance customer interactions and automate query handling.

## Table of Contents
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Technologies
- Python 3.10+
- Jupyter Notebook
- LangChain
- Ollama Server
- Chroma

## Getting Started

### Requirements
Before you begin, ensure you have met the following requirements:
- Python 3.10 or higher
- Jupyter Notebook
- Ollama Server installed

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AlenkaMn/genai-chatbot-rag.git
   cd genai-chatbot-rag
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install and run the Ollama server:**

   Follow the installation instructions from the [Ollama documentation](https://ollama.ai/docs/installation). Once installed, start the server using:

   ```bash
   ollama server
   ```

5. **Download the necessary language models:**

   Run the following command to download the models:

   ```bash
   ollama pull <model_name>
   ```

### Usage

To start the project, open the Jupyter Notebook and run the `Modsen_full.ipynb` notebook.

### Implemented Features
- **Document Retrieval:** Using Chroma for efficient document retrieval.
- **Query Augmentation:** Enhancing user queries with relevant context.
- **Integration with Ollama:** Using local models for enhanced privacy and control.

## Development

### Running the Development Server

To run the Jupyter Notebook for development:

```bash
jupyter notebook
```

### Building the Project

This project doesn't require a typical build process as it runs directly within Jupyter Notebook.




### Deployment

Deployment is done locally through Jupyter Notebook. Ensure that all dependencies are installed and the Ollama server is running.

Please adhere to the project's coding style and ensure that all tests pass before submitting a pull request.



This project was inspired by various chatbot and RAG implementations across the open-source community. Key resources include the [LangChain documentation](https://langchain.com/) and tutorials on integrating OLLaMA models with custom pipelines.
```

>>>>>>> f83d5631f78f51b649089bfa8930b2b48cd814e5
