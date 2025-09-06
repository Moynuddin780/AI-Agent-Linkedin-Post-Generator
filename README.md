# AI LinkedIn Post Generator
# 📸[ Click Here to see live ](https://www.linkedin.com/posts/moynuddin-al-masum-683102375_ai-openai-langchain-activity-7370021032008581120-INVM?utm_source=share&utm_medium=member_android&rcm=ACoAAFy97UMBvYCDuI65RXVqWNIg-pbSkPfXBng)


[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gradio](https://img.shields.io/badge/Gradio-Interface-orange.svg)](https://gradio.app/)

A simple AI-powered tool built with LangChain, OpenAI, and Gradio to generate professional LinkedIn posts on any topic in multiple languages. This app allows users to input a topic and select a language, then generates a structured, engaging, and professional post ready for LinkedIn.

![Demo Screenshot](Frontend%20Image.jpg)



## Features

- **AI-Generated Content**: Uses OpenAI's GPT-4o-mini (or similar models) via LangChain to create high-quality LinkedIn posts.
- **Multi-Language Support**: Generate posts in English, Bengali, Spanish, or easily extend to more languages.
- **User-Friendly Interface**: Powered by Gradio for a simple web-based UI.
- **Customizable Prompts**: Structured prompts ensure posts are professional, engaging, and 2-4 paragraphs long.
- **Easy Setup**: Minimal dependencies and quick installation.
- **Secure API Handling**: Uses environment variables to store sensitive API keys.

## Requirements

- Python 3.8 or higher
- An OpenAI API key (sign up at [platform.openai.com](https://platform.openai.com/))
- Internet connection for API calls

## Installation

1. **Clone the Repository** (if applicable, or create a new project folder and save the code as `app.py`):
   ```
   git clone https://github.com/Moynuddin780/AI-Agent-Linkedin-Post-Generator.git
   cd ai-linkedin-post-generator
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python packages using pip:
   ```
   pip install langchain openai python-dotenv gradio
   ```

   Note: If you're using an older version of LangChain, ensure compatibility. This code uses `langchain.chat_models.ChatOpenAI` and `langchain.chains.LLMChain`.

## Configuration

1. **Create a `.env` File**:
   In the project root, create a file named `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Replace `your_openai_api_key_here` with your actual key from OpenAI. This keeps your API secure and out of the code.

2. **Optional: Customize Model and Base URL**:
   - The code defaults to `gpt-4o-mini` with temperature 0.7 for balanced creativity.
   - If needed, uncomment and set `BASE_URL` in the code (e.g., for custom endpoints), but it's not required for standard OpenAI usage.
   - You can change the model to `gpt-3.5-turbo` or others in the `ChatOpenAI` initialization.

## Usage

1. **Run the Application**:
   Save the provided code as `app.py` (or use the cloned file). Then run:
   ```
   python app.py
   ```

   This will launch a Gradio web interface, usually at `http://127.0.0.1:7860/`. Open this URL in your browser.

2. **Interact with the Interface**:
   - Enter a **Topic** (e.g., "AI in Healthcare").
   - Select a **Language** from the dropdown (English, Bengali, or Spanish).
   - Click **Submit** to generate the post.
   - The generated LinkedIn post will appear in the output textbox.

3. **Command-Line Usage (Optional)**:
   If you prefer not to use the Gradio UI, you can call the `generate_linkedin_post` function directly in Python:
   ```python
   result = generate_linkedin_post("AI in Healthcare", "English")
   print(result)
   ```

## Examples

### Input:
- Topic: "The Future of Remote Work"
- Language: "English"

### Output (Sample Generated Post):
```
In today's fast-paced world, the future of remote work is not just a trend—it's a transformation reshaping how we collaborate and innovate. With advancements in technology like AI-driven tools and virtual reality meetings, teams can now operate seamlessly across continents, boosting productivity and work-life balance. Companies that embrace this shift are seeing reduced overhead costs and access to global talent pools, making remote work a strategic advantage.

However, challenges remain, such as maintaining company culture and addressing digital fatigue. Leaders must prioritize mental health initiatives and foster inclusive environments to ensure long-term success. As we move forward, hybrid models blending remote and in-office experiences will likely dominate, offering flexibility without isolation.

What are your thoughts on the evolution of remote work? Share in the comments below! #RemoteWork #FutureOfWork #Productivity
```

### Multi-Language Example:
- For Bengali or Spanish, the post will be generated in the selected language while maintaining a professional tone.

### Frontend Screenshot:
![AI LinkedIn Post Generator Interface](https://i.imgur.com/attachment-url-here.jpg)

## Troubleshooting

- **API Key Issues**: Ensure your `.env` file is correctly loaded and the key is valid. Test with `print(os.getenv("OPENAI_API_KEY"))`.
- **Module Not Found**: Double-check installations with `pip list`. If using a virtual env, activate it.
- **Gradio Not Launching**: Check for port conflicts or firewall issues. Try running with `--share` for public access: `interface.launch(share=True)`.
- **Code Error in `__name__` Check**: The provided code has a typo: `if _name_ == "_main_":` should be `if __name__ == "__main__":`. Correct this before running.
- **Rate Limits or Costs**: OpenAI API usage may incur costs. Monitor your usage at the OpenAI dashboard.
- **Language Support**: If the generated text in non-English languages seems off, try adjusting the model temperature or prompt for better results.

If issues persist, check the console for error messages or open an issue on the repository.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes (e.g., add more languages, improve prompts, or fix bugs).
4. Commit your changes (`git commit -m "Add feature"`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.


