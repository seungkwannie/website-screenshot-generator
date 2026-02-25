from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_KEY = "scr_live_zvHOivSlwSdtQSqjU9JZaSslc6gUH1Eqi7OEWkbP"
SCREENSHOTBASE_BASE_ENDPOINT = "https://api.screenshotbase.com/v1/take"

@app.route('/', methods=['GET', 'POST'])
def home():
    screenshot_url = None

    if request.method == 'POST':
        target_url = request.form.get('url')

        params = {"url": target_url}
        headers = {"apikey": API_KEY}

        try:
            # Send GET request to ScreenshotBase API
            response = requests.get(SCREENSHOTBASE_BASE_ENDPOINT, params=params, headers=headers, timeout=30)
            response.raise_for_status()

            # Save the returned image
            image_path = os.path.join('static', 'screenshot.png')
            with open(image_path, 'wb') as f:
                f.write(response.content)

            screenshot_url = image_path

        except requests.exceptions.RequestException as e:
            print(f"Error capturing screenshot: {e}")

    return render_template('index.html', screenshot=screenshot_url)

if __name__ == '__main__':
    app.run(debug=True)

# scr_live_zvHOivSlwSdtQSqjU9JZaSslc6gUH1Eqi7OEWkbP