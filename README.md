# Local ChatGPT with Real-Time Reasoning Display

This project demonstrates how to build a **local ChatGPT-like application** using **Ollama** to serve a local LLM (e.g., LLaMA 2) and **Streamlit** for the user interface. The application not only generates responses but also displays the model's **step-by-step reasoning process** in real-time.

## Features
- **100% Local**: No internet required after setup.
- **Real-Time Reasoning**: Displays the model's thought process as it generates responses.
- **Interactive UI**: Built with Streamlit for a seamless user experience.
- **Customizable**: Easily swap models or modify the interface.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.7+
- [Ollama](https://ollama.ai/) (for serving the local LLM)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/local-chatgpt.git
   cd local-chatgpt
   ```
2. Install the required Python packages:
   ```bash
    pip install streamlit ollama
    Pull the desired model using Ollama (e.g., LLaMA 2):
   ```
   
   ```bash
    ollama pull llama2
   ```
3. Run the Streamlit application:

   ```bash
    streamlit run app.py
   ```
   
Open your browser and navigate to the URL provided in the terminal (usually http://localhost:8501).

Interact with the chatbot by typing your message in the input box. The model will display its reasoning process in real-time before providing the final answer.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
