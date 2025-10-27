---
website: https://canvas.anu.edu.au/courses/2781/assignments/11552 
title: Final Project Documentation
author: u8260921
---

<!-- 
it should be no more than 1980 words. 

![Caption for your image](materials/your-image.jpg)

-->

## Research Question, Plan, and Conclusions
Hey Sharks, did you know that households in Australia throw out up to $1500 a year down their bins? That is, in the form of food waste. Households discard enough food daily to provide over a billion meals, even as 1 in 11 people go hungry worldwide. 58% of high-wasting households cited food reaching their expiry date as the most common reason why they disposed of food, suggesting widespread confusion about food safety versus quality indicators and unnecessary wastage of perfectly edible food.

These metrics highlight the core of our problem: the need for better awareness on discerning food safety by our own means, understanding the difference between 'use by' and 'best-before', utilizing what we already have in our kitchens smartly, and making better use of the surplus.

In light of these challenges, this study explores an innovative approach: integrating AI assistance into food management systems to encourage sustainable household behaviors. I believe digitalization and use of AI can help make inventory-tracking a more engaging and efficient experience that covers all the bases.

This leads to my research question: “What are students’ perceptions of usability, usefulness, and sustainability impact in an AI-assisted food management prototype for reducing food waste?”

### Evaluation Plan
Consent to be recorded was requested beforehand and identifying information have been anonymized. The study starts with a pre-task survey to probe awareness on food waste and responsible consumption, related to the 12th SDG. 

Participants were briefed on the functionality of the website, then asked to input 3 food objects as database entries. The food items provided were bread, a carton of eggs, and a can of black pepper. In order to improve immersion, participants were asked to roleplay as if they had shopped for the groceries themselves. The site also comes pre-filled with other ingredients to simulate a moderately pre-stocked kitchen environment. The means by which participants decided to input the ingredients were left up to individual exploration to encourage independent evaluation of the UI/UX. Participants were then asked what they'd do with the food they now had in their "kitchen" (current database state), and how they'd deal with surplus. Afterwards, a semi-structured interview was conducted to obtain qualitative data. Lastly, participants were to fill a post-task survey comprising the SUS scale, a short NASA-TLX index, and another post-task probe on responsible consumption. 

## Conclusions 

## Prototype Design and Features

WasteWise is a website that utilizes computer vision to easily keep track of inventory and when they will soon expire. It's a generalized tool that covers the problems we unearthed in the beginning of this story.

You can input a food item into your digital inventory by scanning it with the camera. This app is built on Django and uses YOLO11, a state-of-the-art object detection model trained on a manually-labelled, homemade dataset of 100 pictures of my previous grocery run. You can either take a snapshot of the detected objects via the 'Save Snapshot' button, or do a fun little thumbs-up gesture (non-standard interaction). Look, ma, no hands!

You can then input the storage, dietary details, and expiry date and this will go into your digital inventory - which you're free to edit and delete as you please. The inventory is sorted by priority on which foods will expire soon, which are already past expiry, and which are still fresh. 

Of course, you can look into the expiry info of each food to see whether they could still be salvaged even if they've passed their expiry date. The app shows information about the quality indicators to look out for in each type of food, so you can think twice before throwing it out.

It doesn't stop here, the app is designed to be your one-stop for tackling the problems of a high-waste household. The 'Generate Recipes' button matches what you have in your digital inventory with a database of recipes to help you prep your meals and really use up what you already have in your kitchen. 

Still have a surplus even after that? Scroll down to 'Donate Your Food', and you'll see where you can go to spread the joy of eating to others in need. :)

Due to lack of financing, I haven't been able to get WasteWise hosted on a public domain. You can find instructions on how to run it locally in materials/HCI_prototype/README.md.

## Research Data, Analysis and Findings

### Quantitative Analysis 

#### SUS Score

In benchmarking the SUS, we compare the  mean to the “golden standard” benchmark of 68:

Null hypothesis (H₀): The system usability is less than or equal to the benchmark.

* H0:μ ≤ 68

Alternative hypothesis (H₁): The system usability is better than the benchmark.

* H1:μ > 68

Significance level: α = 0.05

We obtain the following: 
Mean SUS: 85.50
Std SUS: 11.91
T-statistic: 3.29
One-sided p-value: 0.0152

Since p=0.0152 < α=0.05, we reject the null hypothesis. 
We also obtain the Cohen's d value vs benchmark as 1.47, indicating the usability improvement is substantial, not just statistically significant.


#### NASA-TLX index
The mean RAW NASA-TLX index approximates to 2 (out of 7), which indicates a low workload in using the task. Dimensions which scored the highest workloads were Mental Demand (2.6), Temporal Demand and Effort (2.4). Implications further discussed in 'Practical Usefulness in Everyday Life'.

#### Pre/Post-Task Comparisons
#### Inventory Awareness
| Short Label | Original Question |
|------------|-----------------|
| Q1 | I am aware of the expiry dates of the food I have in my kitchen. |
| Q3 | I know where I can donate leftover food in my local area. |
| Q6 | I can distinguish which foods are still safe to eat after the printed expiry date, and which are not. |

#### Food Management
| Short Label | Original Question |
|------------|-----------------|
| Q2 | I am likely to throw food away if it has reached the expiry date. |
| Q4 | I know how to make good use of all the food I have in my kitchen. |
| Q5 | I feel confident in planning meals to minimize food waste. |
| Q7 | I often forget about items in my kitchen until they go bad. |

#### Impact
| Short Label | Original Question |
|------------|-----------------|
| Q8 | The app helps me become more aware of how much food I have and what might go to waste. |
| Q9 | The app makes food management feel more complicated than it should be. |
| Q10 | Using the app would help me reduce my overall food waste in the long term. |

After reverse scaling and taking the mean of each subheading, the pre- vs post-task results suggest that the prototype had a strong impact on inventory awareness while changes in broader food management behaviors were positive but less conclusive. For Inventory Awareness, the mean score increased from 1.90 to 4.2, and the paired t-test shows t = 7.667, p = 0.002, indicating a statistically significant improvement in students’ awareness of expiry dates, donation options, and ability to distinguish safe foods. The Wilcoxon signed-rank test, a non-parametric test that does not assume the data follows a normal distribution, gives p = 0.062, suggesting a similar trend but slightly weaker evidence under the non-parametric assumption. For Food Management, the mean rose from 3.65 to 4.0, with the t-test yielding t = 2.746, p = 0.052, a marginally non-significant result, and the Wilcoxon p = 0.125, confirming no strong evidence of change when relaxing normality assumptions. 

The post-task Impact questions shows a high mean score of 4.5 out of 5, indicating that participants perceived the AI-assisted food management prototype as highly effective in raising their awareness and guiding their behavior regarding food waste.

### Qualitative Analysis 
Thematic analysis was conducted following the methodology outlined in Naeem et al. (2023) , the full process visible on the Miro link in materials/README.md. All interviews were first recorded then transcribed. Themes discussed below.

#### Impact on Users' Behaviours and Mental Model
The prototype fostered meaningful cognitive shifts in participants’ attitudes toward food management and waste. 3 out of 5 users reported a newfound understanding of expiry dates, realizing that “some foods are still safe to eat after their expiry date” and that “best before” labels might sometimes relate to quality rather than safety. In P4's words: “It's an eye-opener—it helps me think more about managing food before it expires.” The app also raises awareness towards lesser known methods of dealing with surplus, as P5 says, "I didn’t even know donating was an option, and this app even includes the places I can go to if I ever want to donate."  

On a behavioral level, participants said the app would increase confidence and intentionality in managing food. The recipe generation feature empowered less experienced cooks to creatively utilize ingredients they already had. According to P5: “I’m not a good cook. This helps a lot for making meals with what I already have.” The inventory and prioritization tools prompted proactive planning, with users noting how the app “helped them keep track of what to use first (P3)” and “think twice before throwing out expired food. (P1)”  It should be of note that the quantitative analysis showed non-significant (but positive) differences for changes in Food Management Behaviour. The observed behavioral shifts are promising but require further study with a larger sample to confirm their statistical robustness.

#### Usability and Interface Experience

Participants said that the interface was easy to use and pick up, and had engaging methods of input. According to P5, the way the application picks up on human gestures (thumbs-up) during the scanning process makes input a lot funner. Participants also noted that the inventory page had descriptive labels that helped them notice which foods to prioritize in one look (P1).

#### Practical Usefulness in Everyday Life

Users noted the prototype offered tangible benefits beyond food organization. A participant highlighted sustainable behaviours would help them save more money (P1). Users also described a psychological or emotional satisfaction associated with using the system, with one remarking that it “felt generally good for (my) conscience (P4).” Despite these advantages, some barriers to adoption were identified: consistent use requires temporal investment and motivation, meaning that the app’s full potential hinges on routine use. These are consistent with the results of the NASA-TLX, which showed that the app required higher mental and temporal demand and efforts.

#### AI Limitations and Suggested Improvements

In terms of computer vision, issues such as inaccurate object detection and misidentification were noted, prompting suggestions for better model training, improved datasets, and automatic scanning of expiry dates. Users also requested additional features to enhance practical utility, including displaying nutritional information, offering a more diverse range of recipe suggestions, enabling offline use, and providing notifications or reminders.

## Acknowledgements

* ChatGPT - Writing skeletons, cleaning transcripts, Junior Software Engineer
* Claude - Lead Software Engineer
* Otter AI - Voice to Text transcription
* Me - SCRUM Master

## References

<!-- 
Make sure to add at least two external references in ACM format. 

Note that serious errors in referencing including fake or incorrect references comes under the N category in the marking rubric and can be a breach of academic integrity. 
-->

