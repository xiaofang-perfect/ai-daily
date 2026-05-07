---
title: "Chrome’s AI features may be hogging 4GB of your computer storage"
source: The Verge AI
url: https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features
date: 2026-05-07
published_at: 2026-05-06T06:13:09-04:00
tag: 行业动态
item_id: 69c76c175dd5f571
---
Google Chrome may be taking up more of your storage than expected thanks to a large on-device AI model file that, in some cases, is being automatically downloaded to the browser’s system folders. Users who have noticed unexplained drops in their available desktop device storage are now discovering that Chrome is installing a 4GB weights.bin file inside their browser directory when certain AI features are enabled.

# Chrome’s AI features may be hogging 4GB of your computer storage

Here’s how you can find out, and get that storage back if you need it.

Here’s how you can find out, and get that storage back if you need it.

![Illustration of the Chrome logo on a bright and dark red background.](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/24418650/STK114_Google_Chrome_01.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Illustration of the Chrome logo on a bright and dark red background.](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/24418650/STK114_Google_Chrome_01.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

The weights.bin file in question is connected to [Google’s Gemini Nano AI model](https://www.theverge.com/2023/12/6/23989591/google-gemini-ai-model-pixel-8-pro-recorder-smart-reply), which powers Chrome AI tools like scam detection, writing assistance, autofill, and suggestion features. As the Gemini Nano model is designed to run locally, it needs to use training parameters stored on your device rather than pulling information from cloud-based models. That provides some privacy benefits, but isn’t ideal if you’re low on storage — especially as users aren’t being clearly notified about the file size requirements.

If you have certain Gemini AI features enabled on Chrome, it’s likely that the 4GB file has already been downloaded to your system. You can check by opening your Chrome data folders and inspecting the OptGuideOnDeviceModel directory for the weights.bin file.

You can’t simply delete this to free up space, however — if you still have AI features enabled, Chrome may re-download it again in the future. That means you’ll need to head to Settings>System and [toggle off the On-Device AI option](https://support.google.com/chrome/answer/16961953?visit_id=639136487924121801-2123957226&p=on_device_genAI&rd=1) to remove those features and prevent the file from coming back.

Google does specify that “Gemini Nano’s exact size may vary as the browser updates the model,” but this information is presented in a [lengthy guide for built-in AI](https://developer.chrome.com/docs/ai/get-started) features rather than at the point of enabling them in Chrome. If Google had made the storage requirements clearer to users — or provided an option to power Chrome AI features with cloud-based models — this confusion could have been avoided.

”We’ve offered Gemini Nano for Chrome [since 2024](https://developer.chrome.com/blog/web-at-io24) as a lightweight, on-device model,” Google spokesperson Scott Westover tells *The Verge*. “It powers important security capabilities like [scam detection](https://blog.google/innovation-and-ai/technology/safety-security/how-were-using-ai-to-combat-the-latest-scams/) and developer APIs without sending your data to the cloud. While this requires some local space on the desktop to run, the model will automatically uninstall if the device is low on resources. In February, we began rolling out the ability for users to easily turn off and remove the model directly in Chrome settings. Once disabled the model will no longer download or update. More details in our [help center](https://support.google.com/chrome/answer/16961953?visit_id=639136735497958488-2544580539&p=on_device_genAI&rd=1) article.”

**Update, May 6th**: Added statement from Google.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.

## Most Popular

- Apple agrees to pay iPhone owners $250 million for not delivering AI Siri
- Here’s what Microsoft is offering long-serving employees to voluntarily retire
- Nintendo announces a new Star Fox for the Switch 2
- Google shuts down Project Mariner
- The Remarkable Paper Pure is the best digital notepad I’ve ever used
