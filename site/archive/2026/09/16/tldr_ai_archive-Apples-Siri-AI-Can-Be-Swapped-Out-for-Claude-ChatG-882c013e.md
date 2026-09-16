---
title: "Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows"
source: TLDR AI · 2026-09-15
url: https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude?utm_source=tldrai
date: 2026-09-16
published_at: 2026-09-15T12:00:00+00:00
tag: 产品发布
item_id: 882c013e9bf7e832
---
Code sleuth "pdfu" has uncovered iOS 27 and macOS Golden Gate private frameworks that show Apple has designed its new Siri architecture to work with third-party AI models at what appears to be a surprisingly deep level.

![macOS iOS 27 Siri App Feature](https://images.macrumors.com/t/iwIllyfONk3Cy6W_Z_MxFcuS9e0=/400x0/article-new/2026/06/macOS-iOS-27-Siri-App-Feature.jpg?lossy)


One mechanism called Model Delegation allows Claude to appear as a Siri extension in the same way as the existing built-in ChatGPT extension. In pdfu's video, [shared on X](https://x.com/itspdfu/status/2099122424209916015?s=20), the macOS user brings up the "Search or Ask" bar and chooses Claude as the AI model via an "Ask..." contextual menu. 

After enabling the Claude extension, the user asks Siri to "Ask Claude" to set a reminder in Apple's Reminders app. Claude then interprets the natural language reminder request and Siri subsequently creates the reminder. The implication is that if the request requires access to an Apple system feature, Claude hands the task back to Siri.

In another example, Claude can be seen in a Siri app conversation window receiving a request to create a CSV file – something Siri itself cannot handle – and successfully returning the result.

What's more intriguing is the second protocol demonstrated in the video that appears to go considerably further, and could really open up the AI landscape for Apple software requests.

An inference provider in "Model Manager Services" apparently allows Apple's own server-side Siri model to be completely replaced by another model, such as GPT-5.6. In this scenario, ChatGPT receives Apple's Siri planner prompt and tool definitions, which enables it to request system actions, receive the resulting personal data, and formulate an answer that Siri presents using its own interface and voice.

And here's an app extension replacing Siri AI's server model with GPT-5.6 Terra. It uses the Inference Providing protocol in Model Manager Services.
GPT-5.6 receives Apple's native Siri planner prompt and tool definitions. It can make tool calls that perform system actions, and... [pic.twitter.com/cz88kyq3io](https://t.co/cz88kyq3io)
— pdfu (@itspdfu) [September 13, 2026](https://x.com/itspdfu/status/2099122424914592012?ref_src=twsrc%5Etfw)


In the demonstration video, the user asks the ChatGPT model (within the Siri app) to find emails about a specific topic, summarize their contents and action points, then send a message to a person in the user's contacts via the Messages app. The response is then shown as logged in OpenAI's platform web interface.

The European Union's Digital Markets Act may have helped shape Apple's approach here, as it requires Apple to give third parties effective access to iOS hardware and software features available to Apple's own services, and the European Commission has specifically said this principle extends to Siri.

The "Ask..." implementation is currently limited to the ChatGPT extension in the macOS 27 Golden Gate Release Candidate (which is effectively the final version of the software set to be released later today), so Claude is not yet available. Meanwhile, Apple has not yet opened up the model delegation entitlement to third parties and it isn't front-facing to users, but it at least shows how extensively Apple has engineered Siri for future model interoperability.

[iOS 27](https://forums.macrumors.com/forums/ios-27.251),

[macOS Golden Gate](https://forums.macrumors.com/forums/macos-golden-gate.253)
