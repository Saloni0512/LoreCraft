# LoreCraft
![Lore](https://github.com/user-attachments/assets/7af98697-d07e-4c13-be33-8b893c201dce)


An AI poetry generator app that lets you craft poems based on simple text prompts using the Anthropic API.
You can choose from different poem styles, select the number of lines as per your choice
and more.
 Channelise your inner Maya Angelou with LoreCraft!


## Setup

1. Clone this repository
   >Note: The root project directory name is `SonnetVerse`. So keep that in mind while setting up the project
2. Install the required packages:
   ```sh
   pip install anthropic python-dotenv streamlit
   ```
3. For creating a virtual environment run the following command.This ensures that the project runs with the exact versions of packages it requires.
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

4. Create a `.env` file in the root project directory and add your Anthropic API key .Visit [Anthropic](https://console.anthropic.com/dashboard) to get the API key.
   ```sh
   ANTHROPIC_API_KEY = your-api-key
   ```

5. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```


## Demo



https://github.com/user-attachments/assets/ad322c1e-b241-40a4-bdcb-c16d5eecb37b




## License
 This project is licensed under MIT.


