# VoiceChatGPT

Voice Chat with ChatGPT

## Setup
1. Create a new virtual environment

   ```bash
   $ conda create -n openai python
   $ conda activate openai
   ```

2. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

3. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

4. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

5. Run the app

   ```bash
   $ python main.py
   ```

## Todo-List

- [x] text chat
- [ ] speech to text
- [ ] text to speech