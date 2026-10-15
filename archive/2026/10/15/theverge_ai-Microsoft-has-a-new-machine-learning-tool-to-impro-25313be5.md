---
title: "Microsoft has a new machine learning tool to improve weather forecasts"
source: The Verge AI
url: https://www.theverge.com/science/1011127/ai-weather-forecast-microsoft
date: 2026-10-15
published_at: 2026-10-14T12:05:21-04:00
tag: 论文研究
item_id: 25313be506d47105
---
Old-school physics-based weather forecasting and even new AI models typically become less reliable beyond two weeks, a problem Microsoft claims to have solved using machine learning.

# Microsoft has a new machine learning tool to improve weather forecasts

New open-source software could make AI-enhanced weather forecasting more affordable.

![STK438\_CLIMATE\_CHANGE\_G](https://platform.theverge.com/wp-content/uploads/sites/2/2025/02/STK438_CLIMATE_CHANGE_G.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![STK438\_CLIMATE\_CHANGE\_G](https://platform.theverge.com/wp-content/uploads/sites/2/2025/02/STK438_CLIMATE_CHANGE_G.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Justine Calma](https://platform.theverge.com/wp-content/uploads/sites/2/2025/01/Justine_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

[**Hell or High Water: When Disaster Hits Home**](https://www.audible.com/podcast/Hell-or-High-Water-When-Disaster-Hits-Home/B0C15QVQLM), a podcast from Vox Media and Audible Originals.

Researchers with the company say they’ve found a new, cost-effective way to make more accurate weather forecasts two to six weeks in advance — allowing farmers and emergency responders to plan ahead with greater certainty. The findings were [published](https://www.nature.com/articles/s41586-026-11126-x) today in the journal *Nature*, and the tool is now [open-source software](https://github.com/mouatadid/pbc).

Microsoft joins [Google](https://www.theverge.com/tech/988921/weather-forecast-ai-model-google-satellite-update), [Nvidia](https://www.bloomberg.com/news/articles/2026-01-26/nvidia-launches-ai-technologies-to-aid-weather-forecasting?embedded-checkout=true), and other [companies developing AI tools](https://www.fastcompany.com/91548095/ai-just-changed-everything-about-how-we-forecast-the-weather) for weather forecasting. Instead of creating a new standalone weather model, Microsoft’s latest research in this realm uses machine learning to correct bias in existing models. It’s a more accessible way for resource-strapped weather agencies to improve accuracy using AI, the researchers hope.

It’s a more accessible way for resource-strapped weather agencies to improve accuracy using AI

While physics-based modeling is a resource-intensive endeavor running on supercomputers and generative AI depends on [powerful GPUs](https://www.theverge.com/cs/features/937356/ai-data-center-gpu-environmental-impact), Microsoft Research New England senior principal researcher Lester Mackey says the new tool can run just on CPUs. “I have a lot of hope both for the increased resource efficiency of weather forecasting and the extended reliability of forecasts, especially for extreme weather,” Mackey tells *The Verge*.

Physics-based and AI-based models run into similar problems when they start predicting the weather two weeks or more in advance. Traditional models attempt to simulate the complex physics of Earth’s atmosphere, while AI models look for patterns in historical data to make forecasts. In both approaches, models rely on approximations to fill data gaps, whether from regions with sparse weather stations or complex atmospheric phenomena that scientists are still working to understand. The ways in which these models make up for those gaps in data can become a type of systematic bias. The resulting errors compound when making forecasts further ahead in time, making these predictions less precise.

Microsoft calls its method Probabilistic Bias Correction (PBC). The tool uses machine learning to identify systematic bias in a model and make corrections. One example Mackey gives is to correct for changes in climate. Greenhouse gas emissions from fossil fuels are heating up the planet, but a weather model might make predictions based on historical records that can bias it toward colder temperatures than the world is actually experiencing today.

The researchers found that PBC improved the accuracy of a leading physics-based weather model by the European Centre for Medium-Range Weather Forecasts (ECMWF) for 98 percent of precipitation and 92 percent of temperature targets. The machine learning framework also doubled the accuracy of ECMWF’s new AI forecasting system in the study’s analysis. Before the paper was published, the ECMWF had already awarded the authors’ research on PBC in its [AI Weather Quest competition](https://www.ecmwf.int/en/about/media-centre/science-blog/2026/ai-weather-quest-2026).

The new paper on PBC published by researchers at Microsoft, MIT, ECMWF, and other institutions “is a good example of new ideas being developed for the benefit and consideration of the community,” Matthew Chantry, ECMWF’s strategic lead for machine learning, said in an emailed comment to *The Verge*.

“As always, turning ideas into reality \[in\] an operational process is a most challenging step,” Chantry added.

The amount of compute and infrastructure needed for weather forecasting has often left technological advances out of reach for many agencies in economically developing countries. The paper’s authors, however, think PBC can be different. “One of the things that’s really exciting to me about models like PBC is how lightweight they are, how easy to train, that scientists without huge pools of resources can work on trying to configure \[these\] models and make them perform better in specific localities,” says Genevieve Flaspohler, one of the authors of the paper.

Flaspohler worked on PBC as an intern at Microsoft with Mackey, and now she’s the executive director of the nonprofit Rhiza Research, which is working with the Kenya Meteorological Service Authority — with [funding](https://www.gatesfoundation.org/ideas/media-center/press-releases/2025/11/smallholder-farmers-investment-cop30) from the Gates Foundation — to see whether AI can help get more accurate early warnings out to people. PBC is one of the methods they’re testing ahead of what’s expected to be a more extreme rainy season during a [record-breaking El Niño](https://www.bbc.com/weather/articles/cmlye0d7q7zno).

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
