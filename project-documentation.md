---
website: https://canvas.anu.edu.au/courses/2781/assignments/11552 
title: Final Project Documentation
author: u8260921
---

<!-- 
Write your final project documentation here under the provided subheadings, it should be no more than 1980 words. 
Please delete commented text in this document before the submission deadline. 

to include an image, use this syntax:

![Caption for your image](materials/your-image.jpg)

-->

## Research Question, Plan, and Conclusions
Hey Sharks, did you know that households in Australia throw out up to $1500 a year down their bins? That is, in the form of food waste. Households discard enough food daily to provide over a billion meals, even as 1 in 11 people go hungry worldwide. 58% of high-wasting households cited food reaching their expiry date as the most common reason why they disposed of food, suggesting widespread confusion about food safety versus quality indicators and unnecessary wastage of perfectly edible food.

These metrics highlight the core of our problem: the need for better awareness on discerning food safety by our own means, understanding the difference between 'use by' and 'best-before', utilizing what we already have in our kitchens smartly, and making better use of the surplus.

In light of these challenges, this study explores an innovative approach: integrating AI assistance into food management systems to encourage sustainable household behaviors.

This leads to my research question: “What are students’ perceptions of usability, usefulness, and sustainability impact in an AI-assisted food management prototype for reducing food waste?”

### Evaluation Plan
Participants chosen were between the ages of 19-25 and adept in English. Consent to be recorded was requested beforehand and all participants' personal information have been anonymized. The study starts with a pre-task survey to probe awareness on food waste and responsible consumption, related to the 12th SDG. 

Participants were briefed on the functionality and features of the website, then asked to input 3 food objects as database entries in the website (while thinking aloud). The food items provided were bread, a carton of eggs, and a can of black pepper. In order to satisfy immersion, participants were asked to roleplay as if they had shopped for the groceries themselves. The site also comes pre-filled with other ingredients to simulate a moderately pre-stocked kitchen environment. The means by which participants decided to input the ingredients were left up to individual exploration to encourage independent evaluation of the UI/UX. Participants were then asked what they'd do with the food they now had in their "kitchen" (current database state), and whether the prototype helps them in making these decisions. Afterwards, a semi-structured interview was conducted to obtain qualitative data. Lastly, participants were to fill a post-task survey comprising the SUS scale, a short NASA-TLX index, and another post-task probe on responsible consumption. 

## Conclusions 

## Prototype Design and Features

WasteWise is a website that utilizes computer vision to easily keep track of inventory and when they will soon expire. It's a generalized tool that covers the problems we unearthed in the beginning of this story.

You can input a food item into your digital inventory by scanning it with the camera. This app is built on Django and uses YOLO11, a state-of-the-art object detection model trained on a manually-labelled, homemade dataset of 100 pictures of my previous grocery run. You can either take a snapshot of the detected objects via the 'Save Snapshot' button, or do a fun little thumbs-up gesture (non-standard interaction). Look, ma, no hands!

You can then input the storage, dietary details, and expiry date and this will go into your digital inventory - which you're free to edit and delete as you please. The inventory is sorted by priority on which foods will expire soon, which are already past expiry, and which are still fresh. Of course, you can look into the expiry info of each food to see whether they could still be salvaged even if they've passed their expiry date. The app shows information about the quality indicators to look out for in each type of food, so you can think twice before throwing it out.

It doesn't stop here, the app is designed to be your one-stop for tackling the problems of a high-waste household. The 'Generate Recipes' button matches what you have in your digital inventory with a database of recipes to help you prep your meals and really use up what you already have in your kitchen. 

Still have a surplus even after that? Scroll down to 'Donate Your Food', and you'll see where you can go to spread the joy of eating to others in need. :)

Due to lack of financing, I haven't been able to get WasteWise hosted on a public domain. You can find instructions on how to run it locally in materials/HCI_prototype/README.md.

## Research Data, Analysis and Findings

### Impact on Users' Behaviours and Mental Model

### Usability and Interface Experience

### Practical Usefulness in Everyday Life

### AI Limitations and Suggested Improvements

## Acknowledgements

ChatGPT - Writing skeletons, cleaning transcripts, Junior Software Engineer
Claude - Lead Software Engineer
Otter AI - Voice to Text transcription
Me - SCRUM Master

## References

<!-- 
Make sure to add at least two external references in ACM format. 

Note that serious errors in referencing including fake or incorrect references comes under the N category in the marking rubric and can be a breach of academic integrity. 
-->

