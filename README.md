
- **LINE Developers**: To create and configure the LINE Bot.
- **Google Cloud Functions**: To deploy the Python code and generate a webhook for the LINE Bot.

- **Channel type**: Set to Messaging API (mandatory).
- **Provider**: Use an existing one or create a new one if you haven't used it before.
- **Other options**: Fill in the details as required.
- **Bot profile image**: Upload a custom image.
- **Privacy policy URL, Terms of use URL**: These can be left blank.

After creating the bot, find the Channel secret on the Basic Setting page and the Channel access token on the Messaging API page. These will be used in the code.

**Note**: If you issue or reissue these credentials, remember to update them in your code.

Set aside the bot for now. Once the program is deployed, paste the URL back into the Webhook URL field on the Messaging API page.

Google Cloud offers a suite of cloud computing services, including computing, data storage, data analytics, and machine learning.

Click on 'Console' or 'Start a Free Trial' on the website.

Find Cloud Functions in the menu or under the 'Serverless' category.

Set the environment to the first generation and the region to `asia-east1` (Taiwan). Set the trigger to HTTP and allow unauthenticated invocations.

Add four runtime environment variables:

- `ChannelAccessToken`: Your LINE Developers Channel access token.
- `ChannelSecret`: Your LINE Developers Channel secret.

After setting up the function, deploy it. Once deployed, you'll find a 'Trigger URL' that you'll paste back into your LINE Bot.
